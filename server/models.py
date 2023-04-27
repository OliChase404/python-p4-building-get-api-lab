from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

# This is required for the SerializerMixin to work
    serialize_rules = ('-baked_goods.bakery',)
# without it you will get an error like this: RecursionError: maximum recursion depth exceeded

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    baked_goods = db.relationship('BakedGood', backref='bakery')
    

    def __repr__(self):
        return f'<Bakery {self.name}>'


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

# This is required for the SerializerMixin to work
    serialize_rules = ('-bakery.baked_goods',)
# without it you will get an error like this: RecursionError: maximum recursion depth exceeded

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

    def __repr__(self):
        return f'<Baked Good {self.name}, ${self.price}>'
