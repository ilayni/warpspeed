from abc import abstractmethod

from marshmallow import Schema, fields


class BaseSchema(Schema):
    schema_namespace = fields.Str()

    @abstractmethod
    def make_obj(self, data, **kwargs):
        ...
