from flask import render_template,request
from SaleApp import dao
from SaleApp import app


# định tuyến ở trên đặt là gì ở dưới dùng @ đó
@app.route('/')   # trang chủ
def index ():
    categories = dao.load_categories()
    kw = request.args.get('keyword')
    cate_id = request.args.get('category_id')
    products = dao.load_products(cate_id=cate_id, kw = kw)
    return render_template('index.html', categories= categories, products = products)

@app.route('/products/<int:product_id>')
def details(product_id):
    p = dao.get_product_by_id(product_id)
    return render_template('details.html', product=p)
if __name__ == '__main__':
    app.run(debug=True)