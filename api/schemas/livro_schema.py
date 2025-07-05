from marshmallow import Schema, fields

class LivroSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True)
    autor = fields.Str(required=True)
    ano = fields.Int(required=True)
    isbn = fields.Str(required=True)
