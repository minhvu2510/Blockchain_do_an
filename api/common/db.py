#! coding: utf-8
from bson import ObjectId
from redis import Redis
from pymongo import MongoClient
from api.setting import *
import json
import time
from datetime import datetime, timedelta
client = MongoClient(MONGO_CLIENT)
client_report = MongoClient(MONGO_REPORT)
db = client[MONGO_DATABASE]
r = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
r2 = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB_LOG)


def save_to_db(collection,dictionary,field_unique = None):

    col = db[collection]
    if field_unique:
        col.create_index(field_unique, unique=True)
    try:
        item = col.insert_one(dictionary)
        if item.inserted_id:
            return True
        else:
            return False
    except:
        return False
    
def delete_key(key):
    try:
        r.delete(key)
        # col = db['config']
        # col.remove({'account': key})
        return True
    except:
        return False
def get_all_key():
    """
    author: quanghungleo@gmail.com
    description: get all key in Redis
    time: 17/04/2019 14:10
    """
    keys = r.keys()
    # print ('--' , keys)
    # for i in keys:
    #     print(i)
    # print(type(keys))
    return keys
def get_all_route_used():
    routes = []
    k = get_all_key()
    for i in k:
        item = get_item(i)
        item_js = json.loads(item)
        other = item_js['route']['other']
        if other not in routes:
            routes.append(other)
        vt = item_js['route']['vt']
        if vt not in routes:
            routes.append(vt)
        vn = item_js['route']['vn']
        if vn not in routes:
            routes.append(vn)
        mb = item_js['route']['mb']
        if mb not in routes:
            routes.append(mb)
    return routes

def get_item(key):

    item = r.get(key)
    # print(item.decode('utf-8'))
    return item


def set_item(key, value):

    item = r.set(key, json.dumps(value))
    return item


def check_collection_exist(collection):

    if collection in db.list_collection_names():
        return True
    else:
        return False




def find_one_by_dict(collection, dictionary=None):

    if check_collection_exist(collection):
        col = db[collection]
        result = col.find_one(dictionary)
        return result


def count_by_dict(collection, dictionary=None):

    if check_collection_exist(collection):
        col = db[collection]
        result = col.count_documents(dictionary)
        return result


def find_by_dict(collection, dictionary=None):

    if check_collection_exist(collection):
        col = db[collection]
        result = col.find(dictionary)
    else:
        result = None
    return result


def update_one_by_dict(collection, query, dictionary):
    col = db[collection]
    result = col.update_one(query, {"$set": dictionary})
    print(result)
    return result
# 6.60 db_report-sms
def get_dbs():
    k = client_report.list_database_names()
    key_redis = get_all_key()
    result = []
    for i in k:
        if i in key_redis:
            result.append(i)
    return result
def get_tbl_report(name_db, dictionary=None):
    this_db = client_report[name_db]
    col = this_db['tbl_report']
    return col.find(dictionary)
def get_count_dbl_report(name_db):
    this_db = client_report[name_db]
    col = this_db['tbl_report']
    return col.count()
# --------------------------dashboard--------------------
def get_total_accoutn():
    keys = r.keys()
    total = len(keys)
    list_active = []
    list_block = []
    for i in keys:
        item = get_item(i)
        item_js = json.loads(item)
        # print(item_js['state_sms'],type(item_js['state_sms']))
        if (str(item_js['state_sms']) == 'true'):
            list_active.append(i)
        else:
            list_block.append(i)
    return {'total':total,'active': len(list_active),'block':len(list_block)}
def count_route():
    this_db = client['sms-manage']
    col = this_db['supplier']
    return col.count({'status':True})
def count_campaign():
    this_db = client['sms-manage']
    col = this_db['campaign']
    return col.count({'status':True})
def get_all_sms():
    list_acc = get_dbs()
    total = 0
    for i in list_acc:
        this_db = client_report[i]
        col = this_db['tbl_report']
        total += col.count()
    return total
def get_route():
    k = get_dbs()
    list_route = []
    list_result = []
    for i in k:
        this_db = client_report[i]
        col = this_db['tbl_report']
        for j in col.find():
            if (j['route'] not in list_route):
                list_route.append(j['route'])
    for i in k:
        this_db = client_report[i]
        col = this_db['tbl_report']
        for j in list_route:
            total = col.count({'route': j})
            list_result.append({'route': j, 'total': total})
    list_end = []
    for i in list_route:
        k = 0
        for j in list_result:
            if (i == j['route']):
                k+= j['total']
        list_end.append({'route':i, 'total':k})
    return list_end
def get_route_by_month(month):
    k = get_dbs()
    list_route = []
    list_route_count = []
    list_result = []
    for i in k:
        list_by_month = get_route_by_month_count(i,month)
        for j in list_by_month:
            list_route_count.append(j)
            # if (j['route'] not in list_route):
            #     list_route.append(j['route'])
    for i in list_route_count:
        if i['_id'] not in list_route:
            list_route.append(i['_id'])
    # for i in k:
    #     this_db = client_report[i]
    #     col = this_db['tbl_report']
    #     for j in list_route:
    #         total = col.count({'route': j})
    #         list_result.append({'route': j, 'total': total})
    list_end = []
    for i in list_route:
        k = 0
        for j in list_route_count:
            if (i == j['_id']):
                k+= j['count']
        list_end.append({'route':i, 'total':k})
    return list_end
# dashboard
def get_acc_blocked():
    k = get_all_key()
    acc = []
    for i in k:
        item = get_item(i)
        item_js = json.loads(item)
        other = item_js['state_sms']
        if (str(other) == 'false'):
            acc.append(i)
        # if other not in routes:
        #     routes.append(other)
        # vt = item_js['route']['vt']
        # if vt not in routes:
        #     routes.append(vt)
        # vn = item_js['route']['vn']
        # if vn not in routes:
        #     routes.append(vn)
        # mb = item_js['route']['mb']
        # if mb not in routes:
        #     routes.append(mb)
    return acc
#     report to phone
def get_info_by_phonenum(phone):
    list_key = r2.keys("*%s*"%(phone))
    list_report = []
    list_key.sort(reverse=True)
    for key in list_key:
        res = r2.get(key)
        list_report.append(res)
    return list(list_report)
# ====test====
def get_record_by_date(name_db, start_time, stop_time, route):
    this_db = client_report[name_db]
    # start = datetime.strptime(start_time, "%m/%d/%Y")
    stop = datetime.strptime(stop_time, "%m/%d/%Y") + timedelta(days = 1)
    stop = str(stop.strftime("%m/%d/%Y"))
    start = int(time.mktime(datetime.strptime(str(start_time), "%m/%d/%Y").timetuple()))
    stop = int(time.mktime(datetime.strptime(str(stop), "%m/%d/%Y").timetuple()))
    col = this_db['tbl_report']
    if route=='':
        return col.find({ '$and': [ { 'datetime': {"$gte": start } }, { 'datetime': { "$lte": stop } } ] })
    else:
        return col.find({ '$and': [ { 'datetime': {"$gte": start } }, { 'datetime': { "$lte": stop } }, {'route': route} ] })


def get_record_by_route(name_db,route):
    this_db = client_report[name_db]
    col = this_db['tbl_report']
    return col.find({'route': route})
# def get_test3(name_db):
#     this_db = client_report[name_db]
#     col = this_db['tbl_report']
#     start = datetime.strptime("2019-05-08T17:10:40.787", "%Y-%m-%dT%H:%M:%S.%f")
#     # start = start.isoformat()
#     stop = datetime.strptime("2019-05-10T17:10:40.787", "%Y-%m-%dT%H:%M:%S.%f")
#     # stop = stop.isoformat()
#     return col.tbl_report.aggregate([ { "$addFields": { "date": { "$dateFromString": { "dateString": "$iso_date" } } }},
#                                       { "$match": { "date": { "$gte": datetime(2019, 5, 8),
#                                                               "$lt": datetime(2019, 5, 10) }}} ])
def get_record_by_month(name_db, month):
    this_db = client_report[name_db]
    now = datetime.now()
    year = now.year
    str_day = "1/" + str(month) + "/" + str(year)
    start_day = datetime.strptime(str_day, "%d/%m/%Y")
    str_end = "1/" + str(int(month) + 1) + "/" + str(year)
    end_day = datetime.strptime(str_end, "%d/%m/%Y")

    start = int(time.mktime(datetime.strptime(str(start_day.strftime("%d/%m/%Y")), "%d/%m/%Y").timetuple()))
    stop = int(time.mktime(datetime.strptime(str(end_day.strftime("%d/%m/%Y")), "%d/%m/%Y").timetuple()))

    col = this_db['tbl_report']
    # str_day = "01/"+str(month)+"/"+str(year)
    # start_day = datetime.strptime("2019-05-08T17:10:40.787", "%Y-%m-%dT%H:%M:%S.%f")
    # start = start.isoformat()
    # stop = stop.isoformat()
    return col.find({ '$and': [ { 'datetime': {"$gte": start } }, { 'datetime': { "$lte": stop } } ] })
def get_route_by_month_count(name_db, month):
    this_db = client_report[name_db]
    col = this_db['tbl_report']
    now = datetime.now()
    year = now.year
    str_day = "1/" + str(month) + "/" + str(year)
    start_day = datetime.strptime(str_day, "%d/%m/%Y")
    str_end = "1/" + str(int(month) + 1) + "/" + str(year)
    end_day = datetime.strptime(str_end, "%d/%m/%Y")

    start = int(time.mktime(datetime.strptime(str(start_day.strftime("%d/%m/%Y")), "%d/%m/%Y").timetuple()))
    stop = int(time.mktime(datetime.strptime(str(end_day.strftime("%d/%m/%Y")), "%d/%m/%Y").timetuple()))
    # start = start.isoformat()
    # stop = stop.isoformat()
    return col.aggregate([ { "$match": { "datetime": { "$gte": start,
                            "$lte": stop }}},{ '$group' : { '_id': '$route', 'count': { '$sum': 1 } } } ])

def test(month):
    now = datetime.now()
    year = now.year
    str_day = "1/" + str(month) + "/" + str(year)
    start_day = datetime.strptime(str_day, "%d/%m/%Y")
    str_end = "1/" + str(int(month) + 1) + "/" + str(year)
    end_day = datetime.strptime(str_end, "%d/%m/%Y") - timedelta(days=1)
    print(str_day,type(start_day))
    print(end_day,type(end_day))
    return str_day
