import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/signup/{email}/{password}")
async def signup(email, password):
    #
    return "sign up"
