from flask_admin.contrib.sqla import ModelView

from Sales_App_Demo.models import Category,Products
from Sales_App_Demo import app,db
from flask_admin import Admin

admin = Admin(app=app,name = "E-COMMERCES's ADMIN")


class ProductView(ModelView):
    column_list = ['id', 'name','active','category_id']
    column_searchable_list = ['name']
    can_export = True
    edit_modal = True
    column_editable_list = ['name']
    column_filters = ['name','price']

admin.add_view(ModelView(Category, db.session ))
admin.add_view(ProductView(Products, db.session))

