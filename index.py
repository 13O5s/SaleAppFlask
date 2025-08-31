from flask import render_template,request
from SaleApp import dao
from SaleApp import app


# định tuyến ở trên đặt là gì ở dưới dùng @ đó
@app.route('/')   # trang chủ
def index ():
    categories = dao.load_categories()
    cate_id = request.args.get('category_id')
    products = dao.load_products(cate_id)
    return render_template('index.html', categories= categories, products = products)

if __name__ == '__main__':
    app.run(debug=True)