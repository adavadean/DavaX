# Math Operations Microservice

A microservice that provides basic math operations over HTTP and CLI:
- Power 
- Fibonacci
- Factorial

## Selected Architecture

This project was implemented using a **modular microservice architecture** with the following components:

- **FastAPI** as the main web framework for exposing HTTP APIs
- **SQLite** as the persistent storage for all computation requests
- **Kafka** as a log platform for publishing every operation as an event
- **Prometheus** for collecting metrics from the FastAPI server
- **Tailwind-based HTML frontend** for user interaction
- **Threaded worker** that pulls computation requests from a queue
- **In-memory cache** to prevent redundant recalculations
- **Token-based authentication** to secure the endpoints
- **Docker Compose** to manage all services

This architecture allows for extensibility (adding new operations), observability (through Prometheus + Kafka), and flexibility (CLI + HTTP API + UI).

---

## How to Run

### 1. With Docker Compose 

```bash
docker-compose up --build
```

Starts:
- FastAPI app
- Kafka
- Zookeeper
- Prometheus

### 2. Locally 

```bash
uvicorn math_api:app --reload
```

Kafka must be running separately for full functionality.

---

## CLI Usage

Start the worker:

```bash
python cli.py run
```

Send tasks to queue:

```bash
python cli.py compute pow 2 5
python cli.py compute fibonacci 10
python cli.py compute factorial 5
```

---

## API Authentication

Token: `mysecrettoken123`

Add it to requests via `Authorization` header.

---

## Interfaces

### Swagger (FastAPI docs)
[http://localhost:8000/docs](http://localhost:8000/docs)

### HTML Frontend (index.html)
Run:
```bash
python -m http.server 8080
```
Then open: [http://localhost:8080](http://localhost:8080)

---

## Operation History

### Through API
```
GET /history
```

### Through CLI
```bash
python query_db.py
```

---

## Monitoring with Prometheus

Metrics available at:
[http://localhost:9090](http://localhost:9090)

---

## Kafka Logging

To consume Kafka logs:
```bash
docker-compose exec kafka kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic math_logs \
  --from-beginning
```

---

## Project Structure

- `math_api.py` – FastAPI main entry point
- `controller.py` – Operation logic and cache
- `cli.py`, `worker.py` – CLI interface and threaded worker
- `storage.py` – SQLite DB handler
- `index.html` – Web frontend interface
- `query_db.py` – DB inspection tool
- `prometheus.yml`, `Dockerfile`, `docker-compose.yml` – Monitoring and containerization