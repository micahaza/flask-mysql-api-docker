from marshmallow import Schema, fields


class ExchangeDataSchema(Schema):
    currency = fields.Str()
    amount = fields.Decimal(as_string=True)
    rate = fields.Decimal(as_string=True)
    price = fields.Decimal(as_string=True)
    created_at = fields.DateTime()
