from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

userRouter= APIRouter()

@userRouter.get('/users', tags=["users"])
def find_all_user()-> list[User]:
    return usersEntity(conn.local.user.find())

@userRouter.post('/users', tags=["users"])
def create_user(user: User)->User:
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)

@userRouter.get('/users/{id}', tags=["users"])
def find_user(id: str)->User:
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@userRouter.put('/users/{id}', tags=["users"])
def update_user(id: str, user: User)->User:
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@userRouter.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
        userEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))
        return Response(status_code=HTTP_204_NO_CONTENT)
