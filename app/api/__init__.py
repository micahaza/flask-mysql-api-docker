from flask import Blueprint
from flask_restful import Api
from .resources import ExchangeDataResource, LastOperationsResouce

api_blueprint = Blueprint('api', __name__)

api = Api(api_blueprint)

api.add_resource(ExchangeDataResource, '/grab_and_save')
api.add_resource(LastOperationsResouce, '/last')
