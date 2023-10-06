from fastapi import FastAPI
from routes.controller import filters, dashboard, orders
app = FastAPI()

# different routes to create
# /dashboard - total number of orders and total sales
# how the filter works for dashboard
# product - show the total number of orders and total sales 
# state - product on this state - show the total number of orders and total sales
# city - state, city - show the total number of orders and total sales
# from and to - state, city, fromandto - show the total number of orders and total sales

# /order - shows all the orders - will have filters
# how will filters work
# product - 
# state - show all the orders in this state
# city - show all the order in this city and state
# fromandto show all the orders between two dates and from specified city and state
# /filters - product, state, city and from and to  total number of order and sales

app.include_router(filters.router)
app.include_router(dashboard.router)
app.include_router(orders.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}