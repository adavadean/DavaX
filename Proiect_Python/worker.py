import threading
from queue import Queue
from controller import process_operation
from storage import save_result
from confluent_kafka import Producer

task_queue = Queue()

kafka_producer = Producer({'bootstrap.servers': 'kafka:9092'})

def send_kafka_log(message: str):
    kafka_producer.produce("math_logs", value=message.encode("utf-8"))
    kafka_producer.flush()

def worker():
    while True:
        op_data = task_queue.get()
        if op_data is None:
            break
        result = process_operation(op_data)
        save_result(result)
        send_kafka_log(f"Worker processed: {result.operation}({result.x}, {result.y}) = {result.result}")
        task_queue.task_done()

def start_worker():
    t = threading.Thread(target=worker, daemon=True)
    t.start()
    return t