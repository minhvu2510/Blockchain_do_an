#!/usr/bin/python
# -*- coding: utf-8 -*-
import pathmagic
import time
from api.model import db
def savew():
    # drive = db.English.objects(idi='300').first()
    drive = db.User.objects(username='minhvu').first()
    drive.save()

    return True
if __name__ == '__main__':
    savew()