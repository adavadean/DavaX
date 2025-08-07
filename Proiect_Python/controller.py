from model import Operation, Result
from service import pow_op, fibonacci, factorial

cache = {}

def process_operation(op_data: Operation) -> Result:
    key = (op_data.operation, op_data.x, op_data.y)
    if key in cache:
        return cache[key]

    if op_data.operation == "pow":
        result = pow_op(op_data.x, op_data.y)
    elif op_data.operation == "fibonacci":
        result = fibonacci(op_data.x)
    elif op_data.operation == "factorial":
        result = factorial(op_data.x)
    else:
        raise ValueError("Unknown operation")

    res = Result(operation=op_data.operation, x=op_data.x, y=op_data.y, result=result)
    cache[key] = res
    return res