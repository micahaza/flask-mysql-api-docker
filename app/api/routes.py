from . import api
# from flask import request
# from flask import jsonify
from flask_restful import Resource
# reqparse


@api.route('/last', methods=['GET'])
def index():
    return 'last hhh'


@api.route('/grab_and_save', methods=['POST'])
def grab_and_save():
    return 'grab and save datas'


class ExchangeData(Resource):
    def post(self):
        pass
