from fastapi import FastAPI
import datetime
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    number : int
    startDate: datetime.date
    device : str
    problemType: str
    description: str
    client: str
    status : str

repo = [
    Order(
        number = 1,
        startDate = "2000-12-01",
        device = "123",
        problemType = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    )
]

@app.get("/orders")
def get_orders():
    return repo