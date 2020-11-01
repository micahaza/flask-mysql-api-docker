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

    def __repr__(self):
        return f'{self.amount} USD equals {self.price} {self.currency}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'currency': self.currency,
            'amount': self.amount,
            'rate': self.rate,
            'price': self.price,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
