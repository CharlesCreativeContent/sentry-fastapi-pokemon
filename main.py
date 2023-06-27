# main.py
from fastapi import FastAPI, Request
from pokedex import Images, Routes, Pokemon, Items, Moves, Types, Skins, DefaultSkins

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "New"}

@app.get("/images")
async def root():
    return Images

@app.get("/routes")
async def root():
    return Routes

@app.get("/pokemon")
async def root():
    return Pokemon

@app.get("/items")
async def root():
    return Items

@app.get("/moves")
async def root():
    return Moves

@app.get("/types")
async def root():
    return Types

@app.get("/defaultSkins")
async def root():
    return DefaultSkins

@app.get("/skins")
async def root():
    return Skins

@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}