import datetime
from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Optional, Annotated
from fastapi.middleware.cors import CORSMiddleware


class Order(BaseModel):
    number : int
    startDate: datetime.date
    device : str
    problemType : str
    description : str
    client : str
    status : str
    master : Optional[str] = "Не назначен"

class UPDOrder(BaseModel):
    number: int
    status: Optional[str] = ""
    description: Optional[str] = ""
    master: Optional[str] = ""

repo = [
    Order(
        number = 1,
        startDate = "2000-12-01",
        device = "123",
        problemType = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    ),
    Order(
        number = 2,
        startDate = "2000-12-01",
        device = "123",
        problemType = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    ),
    Order(
        number = 3,
        startDate = "2000-12-01",
        device = "123",
        problemType = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    )
]

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_methods = ["*"],
  allow_headers = ["*"]
)

msg = ""

@app.get("/orders")
def get_orders(param = None):
    global msg
    buffer = msg
    msg=""
    if(param):
        return {"repo": [o for o in repo if o.number == int(param)], "msg": buffer}
    return {"repo": repo, "msg": buffer}

@app.post("/orders")
def create_order(dto : Annotated[Order, Form()]):
    repo.append(dto)

@app.post("/upd")
def upd_order(dto : Annotated[UPDOrder, Form()]):
    global msg
    for o in repo:
        if o.number == dto.number:
            if dto.status != o.status and dto.status != "":
                o.status = dto.status
                msg += f"Статус заявки №{o.number} изменен\n"
            if dto.description != "":
                o.description = dto.description
            if dto.master != "":
                o.master = dto.master
                return o
    return "Не найдено"