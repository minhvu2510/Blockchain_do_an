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
PARSER.add_argument('drive_id',
                    type=str,
                    location='form')
PARSER.add_argument('customer_id',
                    type=str,
                    location='form')
PARSER.add_argument('customer_id2',
                    type=str,
                    location='form')
# from flask_restful import reqparse

# parser = reqparse.RequestParser()
# PARSER.add_argument('rate', type=int, help='Rate cannot be converted')
# PARSER.add_argument('name')
class GetQuetstions(Resource):
    def __init__(self, app):
        self.app = app
    def post(self):
        # args = parser.parse_args(strict=True)
        # print (args)
        print ('mv2222222')
        print ('mv333333333333')
        args = PARSER.parse_args()
        print (args)
        log_msg = request.remote_addr + ' [CREATE_EXAM] - %s - %s '
        print (log_msg)
        secret_key = args['Authorization']
        remote_addr = request.remote_addr
        print (remote_addr)
        username = None
        drive_id = args['drive_id']
        if username is None:
            self.app.logger.warning(log_msg % (403,
                                               args['drive_id'])
                                    + ' (Permission denied)')

            return {'status': 'error', 'description': 'Permission denied.'}, 403

        return {'status': 'ok', 'description': 'Request is enqueued.'}, 200
    def get(self):
        args = PARSER.parse_args()
        author_token = args['Authorization']
        author_otp = args['Tokenotp']
        print('-----------', author_token)
        print('+++++++++++', author_otp)
        # return {'status': False, 'description': 'Permission denied.'}, 403
        if api.check_authen_2step(author_token,author_otp) == False:
            return {'status': False, 'description': 'Permission denied.'}, 403
        eng = db.English.objects()
        arr_question = []
        for i in eng:
            obj = {'idi': i['idi'], 'question': i['question'], 'answer': i['answer'], 'TrueAnswer': i['TrueAnswer']}
            arr_question.append(obj)
            print(i['idi'])
            print(type(i))
        # print(obj)
        # random.shuffle(arr_question)
        return {'status': 'ok', 'description': 'Request is enqueued.', 'data': arr_question}, 200