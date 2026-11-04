from Sales_App_Demo import app
from Sales_App_Demo.models import Category, Products

def load_categories():
    return Category.query.order_by('id').all()

def load_products(kw = None, cate_id=None, page=1):
    query = Products.query
    if kw:
        query= query.filter(Products.name.contains(kw))

    if cate_id:
        query = query.filter(Products.category_id.__eq__(cate_id))

    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    return query.order_by('id').slice(start,start + page_size).all()

def count_products():
    return Products.query.count()