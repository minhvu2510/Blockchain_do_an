#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request
import random
import base64
import hashlib
import pyotp
from uuid import uuid4
# from api.common import common_utils
from flask_restful import Resource, reqparse
from api.model import db
PARSER = reqparse.RequestParser()
PARSER.add_argument('username',
                    type=str)
PARSER.add_argument('password',
                    type=str)
PARSER.add_argument('step_1',
                    type=str)
PARSER.add_argument('token',
                    type=str)
PARSER.add_argument('otp',
                    type=str)
PARSER.add_argument('step_2',
                    type=str)

class Login(Resource):
    def __init__(self, app):
        self.app = app
    def post(self):
        args = PARSER.parse_args()
        print(args)
        log_msg = request.remote_addr + ' [CREATE_EXAM] - %s - %s '
        print (log_msg)
        # remote_addr = request.remote_addr
        # print (remote_addr)
        username = None
        user = args['username']
        print('------------',user)
        step_1 = args['step_1']
        print ('--------------',step_1)
        step_2 = args['step_2']
        passw = args['password']
        if step_1 and step_1 == 'yes':
            print ('------------------')
            drive = db.User.objects(username=user).first()
            if not drive:
                return {'status': 'error', 'description': 'Can not find user.'}, 403
            # account = get_account_by_id(account_id)
            # totp = pyotp.TOTP(drive['secret_key'])
            passw_end = base64.b64decode(passw)
            pass_md = hashlib.md5(passw_end).hexdigest()

            print(passw_end)
            print(pass_md)
            drive_log = db.User.objects(username=user, password= pass_md).first()
            if not drive_log:
                return {'status': False, 'description': 'Username or password not incorrect.'}, 403
            else:
                token = str(uuid4())
                drive_log.token = token
                drive_log.save()
            return {'status': True, 'description': 'Please input OTP', "token": token}, 200

        if step_2 and step_2 == 'yes':
            print('0000000000000000000000000000000000000000000')
            token = args['token']
            drive_otp = db.User.objects(token=token).first()
            print ('--------------------------------')
            if not drive_otp:
                return {'status': 'error', 'description': 'Token is expired.'}, 403
            else:
                otp = args['otp']
                totp = pyotp.TOTP(drive_otp["secret_key"])
                # totp.verify(otp)
                print(otp,'+++++++00000++++++')
                if totp.verify(otp):
                    token_otp = str(uuid4())
                    drive_otp.token_otp = token_otp
                    drive_otp.save()
                    return {"status": True, "message": "OTP is correct.", "token_otp": token_otp}, 200
                else:
                    return {'status': 'error', 'description': 'OTP not incorrect.'}, 403
        return {'status': False, 'description': 'Request is enqueued.'}, 200
