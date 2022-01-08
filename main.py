# https://huggingface.co/albert-base-v2
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

unmasker = pipeline('fill-mask', model='albert-base-v2')


# print(unmasker("I am a [MASK].")[0]['sequence'])

class Item(BaseModel):
    text: str


app = FastAPI()


@app.post("/predict/")
def predict(item: Item):
    return unmasker(item.text)[0]['sequence']
