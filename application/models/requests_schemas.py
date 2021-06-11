from marshmallow import Schema, fields


class POST(Schema):
    num = fields.Integer(
        required=True,
        description="num",
    )
    timeout = fields.Integer(
        required=True,
        description="timeout",
    )
