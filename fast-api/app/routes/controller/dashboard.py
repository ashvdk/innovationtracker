from fastapi import APIRouter

router = APIRouter()


@router.post("/dashboard")
async def dashboard():
    return {
        "data": "Successfully reached dashboard"
    }