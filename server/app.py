#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():

    bakeries = Bakery.query.all()
    bakeries_serialized = [bakery.to_dict() for bakery in bakeries]

    response = make_response(
        jsonify(bakeries_serialized),
        200
    )
    response.headers['Content-Type'] = 'application/json'
    return response

    # return 'Hello World!'
    

@app.route('/baked_goods')
def baked_goods():
    bkrgds = BakedGood.query.all()
    bkrgds_serialized = [bkrgd.to_dict() for bkrgd in bkrgds]
    response = make_response(jsonify(bkrgds_serialized), 200)
    response.headers['Content-Type'] = 'application/json'
    return response    


@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bkr = Bakery.query.filter_by(id=id).one()
    bkr_serialized = bkr.to_dict()
    
    response = make_response(jsonify(bkr_serialized), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    bkrgds = BakedGood.query.order_by(BakedGood.price.desc()).all()
    bkrgds_serialized = [bkrgd.to_dict() for bkrgd in bkrgds]
    response = make_response(jsonify(bkrgds_serialized), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    bkrgd = BakedGood.query.order_by(BakedGood.price.desc()).first()
    bkrgd_serialized = bkrgd.to_dict()
    response = make_response(jsonify(bkrgd_serialized), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    app.run(port=555, debug=True)
