from . import db
from datetime import datetime


class ExchangeData(db.Model):

    __tablename__ = 'exchange_data'

    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3), index=True, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Numeric(20, 8), nullable=False)
    price = db.Column(db.Numeric(20, 8), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self, currency, amount, rate, price):
        self.currency = currency
        self.amount = amount
        self.rate = rate
        self.price = price

    def __repr__(self):
        return "<{}{} at price {}>".format(self.amount, self.currency, self.price)

    def save(self):
        db.session.add(self)
        db.session.commit()
