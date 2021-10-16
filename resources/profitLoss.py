from flask_restful import Resource, reqparse
from models.profitLoss import ProfitLossModel


class Stock(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='Price cannot be left blank'
        )
    # parser.add_argument('ticker',
    #     type=str,
    #     required=True,
    #     help='The stock needs a ticker'
    #     )
    parser.add_argument('volume',
        type=int,
        required=True,
        help='The volume of the stock needs to be entered'
        )
    parser.add_argument('trade_fee',
        type=float,
        required=True,
        help='Trade fee needs to be included'
        )
    parser.add_argument('purchase_date',
        type=str,
        required=True,
        help='Trade date needs to be included'
        )

    def post(self, ticker):

        data = Stock.parser.parse_args()
        
        stocks = ProfitLossModel(ticker, **data)

        try:
            stocks.save_to_db()
        except:
            return{"message": "An error occured inserting the item."}, 500

        return stocks.json(), 201

    # def delete(self, name):
    #     item = ProfitLossModel.find_by_name(name)
    #     if item:
    #         item.delete_from_db()
        
    #     return {'message': 'Item deleted'}

    def put(self, ticker):
        data = Stock.parser.parse_args()
        
        stocks = ProfitLossModel.find_by_name(ticker)

        # if stocks is None:
        #     stocks = ProfitLossModel(ticker, **data)
        # else:
        #     Stock.price = data['price']
        stocks = ProfitLossModel(ticker, **data)

        stocks.save_to_db()
        return stocks.json()

    def get(self, ticker):
        stocks = ProfitLossModel.find_by_name(ticker)
        # if stocks:
        #     return stocks.json()
        # return {'message': 'Item not found'}, 404
        return stocks.json()


class StockList(Resource):
    def get(self):
        return {'items': [item.json() for item in ProfitLossModel.query.all()]}