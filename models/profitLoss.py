from db import db

class ProfitLossModel(db.Model):
    __tablename__ = 'ProfitLoss'

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(4))
    price = db.Column(db.Float(precision=2))
    volume = db.Column(db.Integer)
    trade_fee = db.Column(db.Float(precision=2))
    purchase_date = db.Column(db.String(10))

    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('StoreModel')

    def __init__(self, ticker, price, volume, trade_fee, purchase_date):
        self.ticker = ticker
        self.price = price
        self.volume = volume
        self.trade_fee = trade_fee
        self.purchase_date = purchase_date

    def json(self):
        return {'ticker': self.ticker, 'price': self.price, 'volume': self.volume, 'trade_fee': self.trade_fee, 'purchase_date': self.purchase_date}

    @classmethod
    def find_by_name(cls, ticker):
        return cls.query.filter_by(ticker=ticker).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()