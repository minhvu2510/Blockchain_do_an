#!/usr/bin/python
# -*- coding: utf-8 -*-
import pathmagic
import time
from api.model import db
def savew():
    # drive = db.English.objects(idi='300').first()
    drive = db.User.objects(username='B15DCAT195').first()
    # print(drive['token_otp'])
    # drive = db.User()
    # drive = db.Select
    # drive.username = 'B15DCAT195'
    drive.token_otp = 'uvhnimssss'
    # drive.secret_key = 'BFUYEGSLKJFGOIUY'
    # drive.password = '20fbaver3e46c2esr1b1e3675f35a52b'
    # drive.create_time = time.time()
    # drive.secret_key = '20fb05713e46ca7ed1b1e3675f35a52b'
    # drive.whitelist_ip = ['10.5.20.34']

    myquery = {"username": "minhvu"}
    newvalues = {"$set": {"whitelist_ip": "['10.5.20.34', '10.5.20.35']"}}

    # drive.update()

    drive.save()

    return True
if __name__ == '__main__':
    savew()