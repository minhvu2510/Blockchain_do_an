#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request
from api.common import api
from flask_restful import Resource, reqparse
import random
from api.model import db
PARSER = reqparse.RequestParser()
PARSER.add_argument('Authorization',
                    type=str,
                    required=True,
                    location='headers')
PARSER.add_argument('question',
                    type=str,
                    required=True,
                    location='form')
PARSER.add_argument('answer',
                    type=str,
                    location='form')
PARSER.add_argument('trueAnswer',
                    type=str,
                    required=True,
                    location='form')
# PARSER.add_argument('rate', type=int, help='Rate cannot be converted')
# PARSER.add_argument('name')
class SetExam(Resource):
    def __init__(self, app):
        self.app = app
    def post(self):
        """
                   API khởi tạo

               :return:

                       """
        # creat exam
        print (request.remote_addr)
        args = PARSER.parse_args(strict=True)
        # remote_addr - [CREATE_DRIVE] - status - drive_id - customer_id -
        # max_number_of_users - storage_quota - domain - cert_name - cert_crt -
        # cert_key - cert_passphrase - logo - favicon
        log_msg = request.remote_addr + ' [CREATE_EXAM] - %s - %s - %s ' \
                                        '- %s - %s - %s - %s - %s - %s - %s ' \
                                        '- %s - %s'

        # Authenticate
        secret_key = args['Authorization']
        remote_addr = request.remote_addr
        if api.check_authen_header(secret_key) == False:
            self.app.logger.warning(log_msg % (403,
                                               remote_addr,
                                               args['question'])
                                    + ' (Permission denied)')

            return {'status': 'error',
                    'description': 'IP %s is not in whitelist.' % remote_addr
                    }, 403
        question = args['question']
        answer = args['answer']
        TrueAnswer = args['trueAnswer']
        ind = random.randint(1, 1000)
        print(question)
        print(answer)
        print(TrueAnswer)
        list_answer = answer.split(',')
        print(list_answer)
        print(ind)
        print(type(answer))
        drive = db.English()
        # # {id: 1, question: 'mv', answer: [], TrueAnswer: ''}
        drive.idi = ind
        drive.question = question
        drive.answer = list_answer
        drive.TrueAnswer = TrueAnswer

        drive.save()

        return {'status': 'ok', 'description': 'Request is enqueued.'}, 200