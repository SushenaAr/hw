import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=40), unique= True)


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key = True)
    title = sq.Column(sq.String(length=40), unique= True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable= True)# nullable= True, потому что у книги может быт неизвестный издатель

    publisher = relationship(Publisher, backref= 'Book')


class Shop(Base):
    __tablename__ = 'shop'
    
    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=40), unique= True)


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key = True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.Integer)

    shop = relationship(Shop, backref= 'stock')
    book = relationship(Book, backref= 'Book')

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key = True)
    count = sq.Column(sq.Integer)
    count = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))
    count = sq.Column(sq.Integer)

    publisher = relationship(Stock, backref= 'stock')

def create_tables(engine):
    Base.metadata.create_all(engine)
