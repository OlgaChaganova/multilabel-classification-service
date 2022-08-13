import typing as tp
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: tp.Optional[bool] = None

app = FastAPI()


@app.get('/hello')
def root():
    return {'message': 'hello, world!'}


@app.post('/items/{item_id}')
def create_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}
