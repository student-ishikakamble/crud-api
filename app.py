from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="CRUD API")

users = []

class User(BaseModel):
    id: int
    name: str
    email: str


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")

