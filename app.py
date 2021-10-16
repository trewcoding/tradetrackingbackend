from flask import Flask
from flask_restful import Api

# from resources.user import UserRegister
# from resources.item import Item, ItemList
# from resources.store import Store, StoreList
from resources.profitLoss import Stock, StockList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Stock, '/stock/<string:ticker>')
api.add_resource(StockList, '/stocklist/')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
