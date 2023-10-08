from fastapi import APIRouter, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.Sales import Sales
router = APIRouter()

@router.post("/orders")
async def orders():
    try:
        db = SessionLocal()
        sales_data = db.query(Sales).limit(10).all()
        db.close()
        sales_json = [{"product": sale.product, "quantity_ordered": sale.quantity_ordered} for sale in sales_data]
        return {
            "data": sales_json
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# from fastapi import APIRouter, FastAPI, HTTPException
# from database import SessionLocal
# from models.Sales import Sales
# router = APIRouter()

# @router.post("/orders")
# async def orders():
#     try:
#         db = SessionLocal()
#         sales_data = db.query(Sales).limit(10).all()
#         db.close()
#         sales_json = [{"product": sale.product, "quantity_ordered": sale.quantity_ordered} for sale in sales_data]
#         return {
#             "data": sales_json
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    