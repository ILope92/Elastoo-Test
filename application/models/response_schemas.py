from marshmallow import Schema, fields


class ResultSchema(Schema):
    num = fields.Integer(
        required=True,
        description="num",
    )


class NestedQueueWorkSchema(Schema):
    date_created = fields.String(description="num")
    num = fields.Integer(description="num")
    timeout = fields.Integer(description="num")


class ResultQueueWorkSchema(Schema):
    tasks = fields.Nested(nested=NestedQueueWorkSchema())
