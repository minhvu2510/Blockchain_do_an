#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from mongoengine import *
from api import setting

connect(db='contest',
        host=setting.MONGODB_HOST
)


class User(Document):
    username = StringField(unique=True, required=True)
    token = StringField(required=True)
    token_otp = StringField(required=True)
    password = StringField(required=True)
    secret_key = StringField(unique=True, required=True)
    whitelist_ip = ListField(default=[])
    create_time = FloatField(default=time.time())
class English(Document):
    # {id: 1, question: 'mv', answer: [], TrueAnswer: ''}
    idi = IntField(unique=True)
    question = StringField(required=True)
    answer = ListField(required=True)
    TrueAnswer = StringField(required=True)
    Select = StringField(required=True)

class Drive(Document):
    id = StringField(primary_key=True)
    customer_id = StringField(required=True)
    status = StringField()
    default_admin_name = StringField(default='admin',
                                     required=True)
    default_admin_password = StringField(required=True)
    max_number_of_users = IntField(required=True)
    storage_quota = IntField(required=True)
    domain = StringField()
    sys_domain = StringField()
    cert_name = StringField(required=True)
    cert_crt = StringField(required=True)
    cert_key = StringField(required=True)
    cert_passphrase = StringField()
    logo = StringField()
    favicon = StringField()
    replicas = IntField(default=1)
    is_deleted = BooleanField(default=False)
    delete_time = FloatField()
    last_modified = FloatField()
    create_time = FloatField(default=time.time())
