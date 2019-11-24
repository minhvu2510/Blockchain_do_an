#!/usr/bin/python
# -*- coding: utf-8 -*-

import pathmagic

import logging
from flask import Flask
from api.resources import *
from flask_restful import Api
from flask_cors import CORS

APP = Flask(__name__)
CORS(APP)
APP.config['ERROR_404_HELP'] = False
API = Api(APP)

# Logging
formatter = logging.Formatter('(%(asctime)-6s) - %(message)s')
file_handler = logging.FileHandler(filename='./log/resource.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
APP.logger.addHandler(file_handler)
API.add_resource(Homepage, '/', resource_class_kwargs={'app': APP})
API.add_resource(GetQuetstions, '/get_quetstions', resource_class_kwargs={'app': APP})

# Create Drive
API.add_resource(ReceiveAnswers,
                 '/receive_answers',
                 resource_class_kwargs={'app': APP})
API.add_resource(SetExam,
                 '/set_exam',
                 resource_class_kwargs={'app': APP})
API.add_resource(CheckOtp,
                 '/check_otp',
                 resource_class_kwargs={'app': APP})
API.add_resource(Login,
                 '/login',
                 resource_class_kwargs={'app': APP})
API.add_resource(Notify,
                 '/notify',
                 resource_class_kwargs={'app': APP})


if __name__ == '__main__':
    APP.run(debug=True,
            host='127.0.0.1',
            port=8000,
            threaded=True)