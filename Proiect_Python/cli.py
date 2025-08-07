import click
from model import Operation
from worker import task_queue, start_worker
from storage import init_db

@click.group()
def cli():
    init_db()

@cli.command()
@click.argument("operation", type=click.Choice(["pow", "fibonacci", "factorial"]))
@click.argument("x", type=int)
@click.argument("y", type=int, required=False)
def compute(operation, x, y):
    op = Operation(operation=operation, x=x, y=y)
    task_queue.put(op)

@cli.command()
def run():
    print("Worker started")
    start_worker()
    task_queue.join()

if __name__ == "__main__":
    cli()
