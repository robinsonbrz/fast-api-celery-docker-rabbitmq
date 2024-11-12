from fastapi import APIRouter


router = APIRouter()

@router.get("/", )
async def list_users():
    data = {"data":"ok"}
    return data