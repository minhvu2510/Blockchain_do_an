#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request
import random
from api.common import api
from flask_restful import Resource, reqparse
from api.model import db
PARSER = reqparse.RequestParser()
PARSER.add_argument('Authorization',
                    type=str,
                    required=True,
                    location='headers')
PARSER.add_argument('Tokenotp',
                    required=True,
                    type=str,
                    location='headers')
# from flask_restful import reqparse

# parser = reqparse.RequestParser()
# PARSER.add_argument('rate', type=int, help='Rate cannot be converted')
# PARSER.add_argument('name')
class Notify(Resource):
    def __init__(self, app):
        self.app = app
    def get(self):
        args = PARSER.parse_args()
        author_token = args['Authorization']
        author_otp = args['Tokenotp']
        print('-----------', author_token)
        print('+++++++++++', author_otp)
        if api.check_authen_2step(author_token,author_otp) == False:
            return {'status': False, 'description': 'Permission denied.'}, 403
        return {'status': 'ok', 'description': 'Request is enqueued.'}, 200