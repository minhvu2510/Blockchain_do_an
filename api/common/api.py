#! coding: utf-8

from api.common.db import *
from json import loads as load_json
import json
# import urllib2,json
# from urllib2 import HTTPError
from uuid import uuid4
from flask import session, redirect, url_for, render_template
import hashlib
from functools import wraps
import pyotp
import datetime
from api.model import db
# import ConfigParser
# Config = ConfigParser.ConfigParser()
# Config.read("config.ini")

def set_exam(subjects,exam_dict):
    save_to_db(subjects, exam_dict)
    return True

def check_authen_header(authen):
    if (authen == '20fb05713e46ca7ed1b1e3675f35a52b'):
        return True
    return False
def check_authen_2step(token, otp):
    drive_log = db.User.objects(token=token, token_otp=otp).first()
    if not drive_log:
        return False
    return True
def check_auth(secret_key=None, remote_addr=None):
    """
        API xác thực user dựa theo secret key và whitelist ip

    :param secret_key:
    :param remote_addr:
    :return: Username nếu thành công. False nếu lỗi.
    """

    if not secret_key or not remote_addr:
        return None

    user = db.User.objects(secret_key=secret_key).first()

    if user:
        if remote_addr != '127.0.0.1' and remote_addr not in user.whitelist_ip:
            return False
        else:
            return user.username
    else:
        return None


def md5_decrypt(code):
    result = str(hashlib.md5(code.encode('utf-8')).hexdigest())
    return result

def login(email, password):
    account = find_one_by_dict("account", {"email": email})
    if account:
        de_password = md5_decrypt(password)
        if de_password == account['password']:
            if account['two_factor']:
                session['account_id'] = str(account['_id'])
                return 0
            else:
                return 1
    return -1
def login_required(f):

    @wraps(f)
    def wrap(*args, **kwargs):
        # print("=========",session)
        if 'access_token' in session:
            return f(*args, **kwargs)
        return redirect(url_for('login_account'))
    return wrap
def logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'account_id' in session:
            return render_template('auth/verification.html')
        return f(*args, **kwargs)
    return wrap
def two_step_verification(account_id, otp):

    account = get_account_by_id(account_id)
    totp = pyotp.TOTP(account['secret_key'])
    if otp == totp.now():
        session['access_token'] = str(uuid4())
        return True
    else:
        return False


def get_account_by_id(account_id):
    return find_one_by_dict('account', {'_id': ObjectId(account_id)})

def get_list_user():

    keys = get_all_key()
    list_name = []
    for name in keys:
        list_name.append(name.decode('utf-8'))
    return list_name


def get_info_by_username(username):

    info = get_item(username)
    if info:
        return load_json(info)


def set_info(username, info):

    set_item(username, (info))
    return True


def update_info_username(username, new_info):

    res = get_info_by_username(username)
    if res:
        # print('new-info', new_info)
        # print('new-info-------',str(res).replace("'", '"'))
        # print('=======',str(new_info),type(new_info))
        res.update(new_info)
        # print('info new update-----', res, type(res))

        # print('info new update-----',get_info_by_username(username))
        # print('==info after rectfy== update_info==',res,type(res),type(res['route']))
        set_item(username, res)
        update_config(username,new_info)
        return True


def set_supplier(name, route, api, info):
    dict = {"name": name, "route": route, "api": api, "info": info, "status": True}
    save_to_db('supplier', dict)
    return True


def get_supplier():
    suppliers = find_by_dict('supplier', {'status': True})
    list_parse = []
    for x in list(suppliers):
        supplier = {}
        supplier['id'] = str(x['_id'])
        supplier['name'] = x['name']
        supplier['route'] = x['route']
        supplier['api'] = x['api']
        supplier['info'] = x['info']
        list_parse.append(supplier)
    return list_parse
# =======================================================
def update_info_file(username, field, val):
    Config.set(username, field, val)
    with open('config.ini', 'wb') as configfile:
        Config.write(configfile)
    return "True"
# def update_info_username(username, new_info):
#     res = get_info_by_username(username)
#     if res:
#         res.update(new_info)
#         red_user.set(username, json.dumps(res))
#         rtime = datetime.datetime.now().isoformat()
#         log_path = get_log_path()
#         red_check.set(rtime, '0' ,86400)
#         message_log = "%s\t%s\tUpdate Info:%s\t0\n" % (rtime, username, new_info)
#         open("%s/%s"%(log_path,"log_access.log"),'a').write(message_log)
#         return True
#     else:
#         return False

#     ================================================
def update_supplier(id, dict):
    if update_one_by_dict('supplier', {'_id': ObjectId(id)}, dict):
        return True
    return False
# def send_sms_bk(username, password, brandname, msg, sdt):
#     #url = 'http://api.bipbip.vn/api/send'
#     url = "http://api.bipbip.vn/api/send"
#     postdata = {"username": username,"password": password,"message": msg,"brandname": brandname,"recipients":
#         [{"message_id": "%s" % (str(uuid4())), "number": "%s"%(sdt)}]}
#     #if True:
#     try:
#       req = urllib2.Request(url)
#       req.add_header('Content-Type', 'application/json')
#       data = json.dumps(postdata)
#       response = urllib2.urlopen(req, data, 300)
#       res = response.read()
#       print ("RESPONSE TRA VE:")
#       return  res
#     except HTTPError as e:
#       content = e.read()
#       return content
def logout():
    session.clear()

def check_route_use(rote):
    k = get_all_route_used()
    if rote in k:
        return False
    return True
# =--------------------------funtions campaigns vunm---------------------------
def get_list_campaigns():
    suppliers = find_by_dict('campaign', {'status': True})
    list_campaig = []
    for x in list(suppliers):
        supplier = {}
        supplier['id'] = str(x['_id'])
        supplier['name'] = x['name']
        supplier['info'] = x['info']
        supplier['account'] = x['account']
        list_campaig.append(supplier)
    return list_campaig
def set_campaign(name, info, account):
    dict = {"id": str(uuid4()),"name": name, "info": info, "status": True, "account": account}
    save_to_db('campaign', dict, field_unique= 'name')
    return True
def update_campaign(id, dict):
    if update_one_by_dict('campaign', {'_id': ObjectId(id)}, dict):
        return True
    return False
# ------------synch---------------

def update_config(account, dict):
    if update_one_by_dict('config', {'account': account}, dict):
        return True
    return False
def set_config( dict):
    save_to_db('config', dict)
    return True
# ----------------------------report------------------------------------
def get_acct_and_records():
    list_acc = get_dbs();
    list_campaigns = get_list_campaigns()
    list_result = []
    for i in list_acc:
        for j in list_campaigns:
            if i in j['account']:
                result = {'account':i , 'campaign': j['name']}
                list_result.append(result)
    list_used = list(map(lambda x: x['account'], list_result))
    for i in list_acc:
        if i not in list_used:
            list_result.append({'account':i , 'campaign': ''})
    for i in list_result:
        total = get_count_dbl_report(i['account'])
        i.update({'total' : total})
    return list_result
def get_acct_and_records_to_date(start_date,stop_date,rote):
    list_acc = get_dbs();
    list_campaigns = get_list_campaigns()
    list_result = []
    for i in list_acc:
        for j in list_campaigns:
            if i in j['account']:
                result = {'account':i , 'campaign': j['name']}
                list_result.append(result)
    list_used = list(map(lambda x: x['account'], list_result))
    for i in list_acc:
        if i not in list_used:
            list_result.append({'account':i , 'campaign': ''})
    for i in list_result:
        list_re = list(get_record_by_date(i['account'],start_date,stop_date,rote))
        total = len(list_re)
        i.update({'total' : total})
    return list_result
def get_acct_and_records_by_route(route):
    list_acc = get_dbs();
    list_campaigns = get_list_campaigns()
    list_result = []
    for i in list_acc:
        for j in list_campaigns:
            if i in j['account']:
                result = {'account': i, 'campaign': j['name']}
                list_result.append(result)
    list_used = list(map(lambda x: x['account'], list_result))
    for i in list_acc:
        if i not in list_used:
            list_result.append({'account': i, 'campaign': ''})
    for i in list_result:
        list_re = list(get_record_by_route(i['account'],route))
        total = len(list_re)
        i.update({'total': total})
    return list_result
def get_record_bymonth(month):
    list_acc = get_dbs();
    list_campaigns = get_list_campaigns()
    list_result = []
    for i in list_acc:
        for j in list_campaigns:
            if i in j['account']:
                result = {'account': i, 'campaign': j['name']}
                list_result.append(result)
    list_used = list(map(lambda x: x['account'], list_result))
    for i in list_acc:
        if i not in list_used:
            list_result.append({'account': i, 'campaign': ''})
    for i in list_result:
        list_re = list(get_record_by_month(i['account'], month))
        total = len(list_re)
        i.update({'total': total})
    return list_result
def get_record_detail(name,start_date,stop_date,rote):
    list_re = list(get_record_by_date(name,start_date,stop_date,rote))
    return list_re
def get_detail_acc(acc):
    list_result = get_tbl_report(acc)
    return list_result
# ----------------------------get acc block--------------------------------