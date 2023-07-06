# main.py
from fastapi import FastAPI, Request
from pokedex import Images, Routes, Pokemon, Items, Moves, Types, Skins, DefaultSkins
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/moves/{move_id}")
def read_root(move_id: str):
    return Moves.get(move_id,"Not Found")

@app.get("/skins/{skin_id}")
def read_root(skin_id: str):
    return Skins.get(skin_id,"Not Found")

@app.get("/types/{type_id}")
def read_root(type_id: str):
    return Types.get(type_id,"Not Found")

@app.get("/items/{item_id}")
def read_root(item_id: str):
    return Items.get(item_id,"Not Found")

def check_id(number):
    for poke in Pokemon.values():
        if poke["id"] == number:
            return poke

@app.get("/pokemon/{pokemon_id}")
def read_root(pokemon_id: str):
    foundPokemon = Pokemon.get(pokemon_id,"Not Found")
    if foundPokemon == "Not Found":
        if pokemon_id.isnumeric():
            if 0 < int(pokemon_id) < 898:
                foundPokemon = check_id(int(pokemon_id))
    return foundPokemon

@app.get("/routes/{route_id}")
def read_root(route_id: str):
    return Routes.get(route_id,"Not Found")

@app.get("/images/{image_id}")
def read_root(image_id: str):
    return Images.get(image_id,"Not Found")
