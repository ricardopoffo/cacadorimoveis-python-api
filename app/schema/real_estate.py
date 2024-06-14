from flask_marshmallow import Schema
from marshmallow.fields import Str

class RealEstateSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["name"]
    
    message = Str()
