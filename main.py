from fastapi import FastAPI
from typing import Union, Annotated, List 
from .auth import router as auth_router
from db import engine 
from sqlmodel import SQLModel
from dotenv import load_dotenv

load_dotenv()
base_prompt = "Given what you know about me, my strengths and weaknesses, goals, fears, desires, accomplishments, hobbies, past, present, vices and virtues, can you generate a profile of me as an anime character, i.e powers, stats, abilities, biography, personality, fashion sense, etc? Feel free to draw on all categories of anime to do so, and, while remaining true to what you know about me, take creative liberty as you wish!"


app = FastAPI()
app.include_router(auth_router)
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]= None):
    return {"item_id": item_id, "q": q}
def main():
    print("Hello from mythikal-api!")
      
