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

@app.get("/moves/{move_id}")
def read_root(move_id: str):
    foundMove = Moves.get(move_id,"Not Found")
    return {move_id: foundMove}

@app.get("/skins/{skin_id}")
def read_root(skin_id: str):
    foundSkin = Skins.get(skin_id,"Not Found")
    return {skin_id: foundSkin}

@app.get("/types/{type_id}")
def read_root(type_id: str):
    foundType = Types.get(type_id,"Not Found")
    return {type_id: foundType}

@app.get("/items/{item_id}")
def read_root(item_id: str):
    foundItem = Items.get(item_id,"Not Found")
    return {item_id: foundItem}

def check_id(number):
    found = "None"
    for poke in Pokemon.values():
        if poke["id"] == number:
        return poke

@app.get("/pokemon/{pokemon_id}")
def read_root(pokemon_id: str):
    foundPokemon = Pokemon.get(pokemon_id,"Not Found")
    if foundPokemon == "Not Found":
        if pokemon_id.isnumeric():
            if 0 < int(pokemon_id) < 200:
                foundPokemon = check_id(int(pokemon_id))
    return {pokemon_id: foundPokemon}

@app.get("/routes/{route_id}")
def read_root(route_id: str):
    foundRoute = Routes.get(route_id,"Not Found")
    return {route_id: foundRoute}

@app.get("/images/{image_id}")
def read_root(image_id: str):
    foundImage = Images.get(image_id,"Not Found")
    return {image_id: foundImage}
