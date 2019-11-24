#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request
import random
import pyotp
from uuid import uuid4
# from api.common import common_utils
from flask_restful import Resource, reqparse
from api.model import db
PARSER = reqparse.RequestParser()
PARSER.add_argument('Authorization',
                    type=str,
                    required=True,
                    location='headers')
PARSER.add_argument('otp',
                    type=str,
                    location='form')
class Otp(Resource):
    def __init__(self, app):
        self.app = app
    def post(self):
        # args = parser.parse_args(strict=True)
        # print (args)
        args = PARSER.parse_args()
        log_msg = request.remote_addr + ' [CREATE_EXAM] - %s - %s '
        print (log_msg)
        remote_addr = request.remote_addr
        print (remote_addr)
        username = None
        user = args['username']
        passw = args['password']
        if username is None:
            self.app.logger.warning(log_msg % (403,
                                               args['drive_id'])
                                    + ' (Permission denied)')

            return {'status': 'error', 'description': 'Permission denied.'}, 403

        drive = db.User.objects(username=user).first()
        if not drive:
            return {'status': 'error', 'description': 'Can not find user.'}, 403
        # account = get_account_by_id(account_id)
        # totp = pyotp.TOTP(drive['secret_key'])
        drive_log = db.User.objects(username=user, password= passw).first()
        if not drive_log:
            return {'status': 'error', 'description': 'Username or password not incorrect.'}, 403
        else:
            token = str(uuid4())
            drive_log.token = token
        return {'status': 'ok', 'description': 'Please input OTP', "token": token}, 200
        if request.method == "POST":
            print
            "POST"
            data = json.loads(request.data)
            message = {"status": True}
            if "step_1" in data and data["step_1"] == "yes":
                message = helper.check_require(["username", "password"], data)
                if message["status"]:
                    username = data["username"]
                    password = data["password"]
                    print
                    username
                    print
                    password
                    response_login = db.get_document(
                        "tbl_manage_account",
                        {"username": username, "password": password}
                    ).get("data")
                    print
                    response_login
                    if not response_login:
                        message = {"status": False, "message": "Username or password not incorrect."}
                    else:
                        token = str(uuid4())
                        message = db.update_document("tbl_manage_account", {"username": username}, {"token": token})
                        if message["status"]:
                            message = {"status": True, "message": "Please input OTP.", "token": token}
                        else:
                            message = {"status": False, "message": "Server busy."}
            if "step_2" in data and data["step_2"] == "yes":
                message = helper.check_require(["otp"], data)
                if message["status"]:
                    otp = data["otp"]
                    token = data["token"]
                    print
                    token
                    response_login = db.get_document(
                        "tbl_manage_account",
                        {"token": token}
                    ).get("data")
                    print
                    response_login
                    if not response_login:
                        message = {"status": False, "message": "Token is expired."}
                    else:
                        totp = pyotp.TOTP(response_login[0]["secret_otp"])
                        print
                        totp
                        print
                        print
                        totp.verify(otp)
                        if totp.verify(otp):
                            message = {"status": True, "message": "OTP is correct."}
                        else:
                            message = {"status": False, "message": "OTP is incorrect."}
            if not message["status"]:
                raise InvalidUsage(message, status_code=400)
            print
            simplejson.dumps(message)
            return simplejson.dumps(message)

        return "False"

        return {'status': 'ok', 'description': 'Request is enqueued.'}, 200
    def get(self):
        args = PARSER.parse_args()
        secret_key = args['Authorization']
        print(secret_key)
        eng = db.English.objects()
        arr_question = []
        # {id: 1, question: 'mv', answer: [], TrueAnswer: ''}
        for i in eng:
            obj = {'idi': i['idi'], 'question': i['question'], 'answer': i['answer'], 'TrueAnswer': i['TrueAnswer']}
            arr_question.append(obj)
            print(i['idi'])
            print(type(i))
        # print(obj)
        # random.shuffle(arr_question)
        return {'status': 'ok', 'description': 'Request is enqueued.', 'data': arr_question}, 200