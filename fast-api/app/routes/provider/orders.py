from fastapi import APIRouter, Depends, Request, HTTPException
from database import SessionLocal
from models.Filters import Filters
from models.Products import Products
from models.Sales import Sales
import pandas as pd
import uuid
from sqlalchemy.orm import Session


def createNewOrder(order_details, db: Session = None):
    unique_id = uuid.uuid4()
    products = order_details.get("products")
    street = order_details.get("street")
    city = order_details.get("city")
    state = order_details.get("state")
    # try:
    for product in products:
        print(unique_id)
        print(product["product"])
        print(product["quantity_ordered"])
        print(product["price"])
        print(product["order_date"])
        print(street+", "+city+", "+state)
        print(city)
        print(state)
        print("345346")
        order = Sales(
            order_id = unique_id,
            product = product["product"],
            quantity_ordered = product["quantity_ordered"],
            price_each = product["price"],
            order_date = str(product["order_date"]),
            purchase_address = street+", "+city+", "+state,
            city = city,
            state = state,
            zip_code = "34534"
        )
        db.add(order)
    db.commit()
    return {"message": f"{len(products)} sales records created successfully"}
    # except Exception as e:
    #     db.rollback()
    #     raise HTTPException(status_code=500, detail=str(e))
    


def get_details():
    try:
        db = SessionLocal()
        states = db.query(Filters.state).distinct().all()
        streets = db.query(Filters.address).distinct().limit(100).all()
        list_states = [state[0] for state in states]
        cities = db.query(Filters.city, Filters.state).filter(Filters.state.in_(list_states)).distinct().all()
        products = db.query(Products).all()
        db.close()
        list_street = [{ "label": street[0], "value": street[0] } for street in streets]
        def format_city(city):
            return {"label": city, "value": city}
        df = pd.DataFrame(cities, columns=['City', 'State'])
        cities_by_state = df.groupby('State')['City'].apply(lambda x: x.apply(format_city).tolist()).to_dict()
        # print([state[0] for state in states])
        # distinct_states = [{"label": state[0], "value": state[0]} for state in states]
        # distinct_cities = [{"label": city[0], "value": city[0]} for city in cities]
        # all_products = [product.__dict__ for product in products]
        # print(distinct_states)
        # print(distinct_cities)
        # print(all_products)
        return {
            "products": products,
            "state": [{"label": state, "value": state} for state in list_states],
            "city": cities_by_state,
            "address": list_street
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    