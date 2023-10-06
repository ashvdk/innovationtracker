from fastapi import APIRouter

router = APIRouter()

@router.post("/orders")
async def orders():
    return {
        "data": "Successfully readhed orders"
    }