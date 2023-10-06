from fastapi import APIRouter

router = APIRouter()

@router.post("/filters")
async def filters():
    return {
        "data": "Successfully reached filters"
    }