from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def hello_world():
    return "hello world"