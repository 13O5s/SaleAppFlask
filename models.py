from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from SaleApp import db, app

class BaseModel(db.Model):
    __abstract__ = True  #bật lớp trừu tượng để khi chạy không khởi tạo bảng BaseModel
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy = True)
    #backref có tác dụng khai báo ở trong Product có đối tượng category
    #lazy khi để true thì  khi nào mới lấy đc products



class Product(BaseModel):
    __tablename__ = 'product'
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default = 0)
    image = Column(String(100))
    active = Column(Boolean,default = True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)





if __name__ == '__main__':
    with app.app_context():
        c1 = Category(name='Điện thoai')
        c2 = Category(name='Máy tính bảng')
        c3 = Category(name='Laptop')

        # db.session.add_all([c1,c2,c3]) # add dữ liệu nhiều do
        # db.session.commit()
        p1 = Product(name='iPhone13-1', description = 'Apple,128GB', price=10000, image ='https://cdn.tgdd.vn/Products/Images/42/250257/s16/iphone-13-pink-1-1-2-3-4-5-650x650.png',category_id =1)
        p2 = Product(name='iPad Pro-2', description = 'Apple,128GB', price=20000, image ='https://cdn.tgdd.vn/Products/Images/42/250257/s16/iphone-13-pink-1-1-2-3-4-5-650x650.png',category_id =2)
        p3 = Product(name='Laptop 22 -3', description = 'Apple,128GB', price=30000, image ='https://cdn.tgdd.vn/Products/Images/42/250257/s16/iphone-13-pink-1-1-2-3-4-5-650x650.png',category_id =3)
        p4 = Product(name='iPhone13-1', description = 'Apple,128GB', price=10000, image ='https://cdn.tgdd.vn/Products/Images/42/250257/s16/iphone-13-pink-1-1-2-3-4-5-650x650.png',category_id =1)
        p5 = Product(name='iPhone13-2', description = 'Apple,128GB', price=20000, image ='https://cdn.tgdd.vn/Products/Images/42/250257/s16/iphone-13-pink-1-1-2-3-4-5-650x650.png',category_id =2)
        p6 = Product(name='iPhone13-3', description = 'Apple,128GB', price=30000, image ='https://cdn.tgdd.vn/Products/Images/42/250257/s16/iphone-13-pink-1-1-2-3-4-5-650x650.png',category_id =3)
        db.session.add_all([p1,p2,p3,p4,p5,p6])
        db.session.commit()
        # db.create_all() #khi cần tạo dữ liệu mới chạy dòng này
