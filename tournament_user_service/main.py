from fastapi import FastAPI

from .models import User, Profile

app = FastAPI()


@app.get("/")
async def get_all_users():
    return {"message": "Hello World"}


@app.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"get user {user_id}"}


@app.post("/users")
async def create_user():
    return {"message": "create user"}


@app.put("/")
async def update_user(user: User):
    return {"message": f"update user {user}"}


@app.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"delete user {user_id}"}
