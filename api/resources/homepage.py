#!/usr/bin/python
# -*- coding: utf-8 -*-

# from api import settings
from raven import Client as Sentry
from flask_restful import Resource

# Connect Sentry
# SENTRY = Sentry(
#     dsn=settings.SENTRY_DSN
# )


class Homepage(Resource):
    def __init__(self, app):
        self.app = app

    def get(self):
        """
            Homepage

        :return:
        """

        return "Code by MinhVu", 200
