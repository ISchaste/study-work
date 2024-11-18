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


@app.get("/")
def read_root():
    return "Hello"