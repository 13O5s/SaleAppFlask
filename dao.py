import json
from SaleApp import app
from SaleApp.models import Category, Product


def load_categories():
    # mở db thông qua json file
    # with open('%s/data/categories.json'% app.root_path, encoding ='utf-8') as f:
    #     return json.load(f)

#     kết nối db thông qua mysql
    return Category.query.all()


def load_products(cate_id = None, kw = None):
    # with open('%s/data/products.json' % app.root_path, encoding='utf-8') as f:
    #     products = json.load(f)

    # if cate_id:
    #     products = [p for p in products if p['category_id'] == int(cate_id)]
    #
    # return products

    products = Product.query
    # khúc này chưa truy vấn dữ liệu
    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
    if kw:
        products = products.filter(Product.name.contains(kw))
    return products.all()
#     khúc này mới truy vấn dữ liệu


def get_product_by_id(product_id):
    return Product.query.get(product_id)
