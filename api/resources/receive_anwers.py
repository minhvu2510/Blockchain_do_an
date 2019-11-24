#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygments.lexer import default

from api.model import db
from flask import request
import ast
import json
import random
from api.common import api
import requests
# from api.common import common_utils
from flask_restful import Resource, reqparse
PARSER = reqparse.RequestParser()
PARSER.add_argument('Authorization',
                    type=str,
                    required=True,
                    location='headers')
PARSER.add_argument('Tokenotp',
                    type=str,
                    required=True,
                    location='headers')
PARSER.add_argument('account_id',
                    type=str,
                    required=True)
PARSER.add_argument('list_ans',
                    type=str,
                    required=True)

class ReceiveAnswers(Resource):
    def __init__(self, app):
        self.app = app
    def post(self):
        args = PARSER.parse_args()
        log_msg = request.remote_addr + ' [SEVE_ANS] - %s - %s - %s '
        # secret_key = args['Authorization']
        username = request.remote_addr
        secret_key = args['Authorization']
        account_id = args['account_id']
        list_ans = args['list_ans']
        author_token = args['Authorization']
        author_otp = args['Tokenotp']
        # return {'status': False, 'description': 'Permission denied.'}, 403
        if api.check_authen_2step(author_token, author_otp) == False:
            return {'status': False, 'description': 'Permission denied.'}, 403
        # print(list_ans.split(',')[0])
        print('+++++++++++++++++++++++++')
        # print(ast.literal_eval(list_ans))
        # --------------------
        arr_ans = list_ans.split('-')
        for i in arr_ans:
            print(i.split('|')[1])
        eng = db.English.objects()
        arr_question = []
        # {id: 1, question: 'mv', answer: [], TrueAnswer: ''}
        for i in eng:
            obj = {'idi': i['idi'], 'question': i['question'], 'answer': i['answer'], 'TrueAnswer': i['TrueAnswer']}
            arr_question.append(obj)
        dem = 0
        print('----------------------------------------------')
        for i in arr_ans:
            print(i)
            for j in arr_question:
                print(i.split('|')[0])
                if(int(i.split('|')[0]) == j['idi']):
                    if((i.split('|')[1]) == j['TrueAnswer']):
                        dem += 1
                    # print('vudeptrai')
                # if(int(j['idi']) == int(i['idi'])):
                #     if(i['TrueAnswer'] == j['result']):
                #         dem = dem + 1

        print('-------------', dem)

        return {'status': 'ok', 'description': 'Request is enqueued.', 'data': dem}, 200