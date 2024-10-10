from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dataclasses import dataclass

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Replace with a specific domain for better security.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.).
    allow_headers=["*"],  # Allows all headers.
)

@dataclass
class Pool:
    id: int
    opening_hours: list[int]
    data: list[int]

pools = [
    Pool(0, [8,9,10,11,12,13,14,15,16,17,18,19,20], [3,15,40,50,63,44,32,23,12,5,2,1,0]),
]

@app.get("/predictions/{id}")
async def graph(id: int):
    return pools[id]


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
