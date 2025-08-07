from pydantic import BaseModel
from typing import Literal

class Operation(BaseModel):
    operation: Literal["pow", "fibonacci", "factorial"]
    x: int
    y: int | None = None

class Result(BaseModel):
    operation: str
    x: int
    y: int | None
    result: int
