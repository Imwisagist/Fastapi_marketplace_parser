import requests
from fastapi import FastAPI, status, Response
from fastapi.middleware.cors import CORSMiddleware

from db import session
from models import Goods

app = FastAPI(title='Legsy')
app.add_middleware(CORSMiddleware, allow_origins=['*'])


@app.post('/goods/{nm_id}', status_code=status.HTTP_201_CREATED)
async def add_goods(nm_id):
    db_session = session()
    goods_exists = db_session.get(Goods, nm_id)
    if goods_exists:
        return goods_exists

    response = requests.get(f'https://card.wb.ru/cards/detail?nm={nm_id}')

    product_data = response.json().get('data').get('products')[0]
    current_goods = Goods(
        nm_id=product_data.get('id'),
        name=product_data.get('name'),
        brand=product_data.get('brand'),
        brand_id=product_data.get('brandId'),
        site_brand_id=product_data.get('siteBrandId'),
        supplier_id=product_data.get('supplierId'),
        sale=product_data.get('sale'),
        price=str(product_data.get('priceU'))[:-2],
        sale_price=str(product_data.get('salePriceU'))[:-2],
        rating=product_data.get('rating'),
        feedbacks=product_data.get('feedbacks'),
        colors=product_data.get('colors')[0],
    )
    db_session.add(current_goods)
    db_session.commit()
    db_session.refresh(current_goods)
    return current_goods


@app.get('/goods/')
async def get_all_goods():
    db_session = session()
    return db_session.query(Goods).all()


@app.get('/goods/{nm_id}')
async def get_goods(nm_id, response: Response):
    db_session = session()
    goods_exists = db_session.get(Goods, nm_id)
    if not goods_exists:
        response.status_code = status.HTTP_404_NOT_FOUND
        return 'Not found'
    return goods_exists


@app.delete('/goods/{nm_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_goods(nm_id):
    db_session = session()
    goods_exists = db_session.get(Goods, nm_id)
    if goods_exists:
        db_session.delete(db_session.get(Goods, nm_id))
        db_session.commit()
