from fastapi import FastAPI, HTTPException, Header, Security
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from confluent_kafka import Producer
from pydantic import BaseModel
from typing import Optional, Literal
import sqlite3
from service import pow_op, fibonacci, factorial

API_TOKEN = "mysecrettoken123"

app = FastAPI(
    title="Math Operations Microservice",
    description="A secured API with Prometheus monitoring and Kafka logging",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

# Kafka Producer
kafka_producer = Producer({"bootstrap.servers": "kafka:9092"})

def send_log_to_kafka(message: str):
    kafka_producer.produce("math_logs", value=message.encode("utf-8"))
    kafka_producer.flush()

class OperationRequest(BaseModel):
    operation: Literal["pow", "fibonacci", "factorial"]
    x: int
    y: Optional[int] = None

class OperationResult(BaseModel):
    operation: str
    x: int
    y: Optional[int]
    result: int

def init_db():
    conn = sqlite3.connect("math.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT,
            x INTEGER,
            y INTEGER,
            result INTEGER
        )
    """)
    conn.commit()
    conn.close()

@app.on_event("startup")
def startup_event():
    init_db()

def authorize(token: str):
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid or missing token")

@app.post("/compute", response_model=OperationResult)
def compute_operation(req: OperationRequest, token: str = Security(api_key_header)):
    authorize(token)
    if req.operation == "pow":
        if req.y is None:
            raise HTTPException(status_code=400, detail="Missing parameter y for pow")
        result = pow_op(req.x, req.y)
    elif req.operation == "fibonacci":
        result = fibonacci(req.x)
    elif req.operation == "factorial":
        result = factorial(req.x)
    else:
        raise HTTPException(status_code=400, detail="Unknown operation")

    res = OperationResult(operation=req.operation, x=req.x, y=req.y, result=result)

    conn = sqlite3.connect("math.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO operations (operation, x, y, result) VALUES (?, ?, ?, ?)",
        (res.operation, res.x, res.y, res.result)
    )
    conn.commit()
    conn.close()

    send_log_to_kafka(f"API call: {res.operation}({res.x}, {res.y}) = {res.result}")
    return res

@app.get("/history", response_model=list[OperationResult])
def get_all(token: str = Security(api_key_header)):
    authorize(token)
    conn = sqlite3.connect("math.db")
    cur = conn.cursor()
    cur.execute("SELECT operation, x, y, result FROM operations")
    rows = cur.fetchall()
    conn.close()
    return [OperationResult(operation=row[0], x=row[1], y=row[2], result=row[3]) for row in rows]