from flask import render_template,request
import math
from Sales_App_Demo import app,dao


@app.route('/')
def index():

    products=dao.load_products(kw=request.args.get('kw'),cate_id=request.args.get('category_id')
                               , page=request.args.get('page',1,type=int))

    page_size = app.config['PAGE_SIZE']

    return render_template("index.html",products = products, pages = math.ceil(dao.count_products()))

@app.route('/signin')
def signin_view():
    return render_template("signin.html")

@app.route('/signup')
def signup_view():
    return render_template("signup.html")

@app.context_processor
def common_responses():
    return {
        'categories': dao.load_categories()
    }
if __name__ == '__main__':
    with app.app_context():
        from Sales_App_Demo import admin
        app.run(debug=True)
