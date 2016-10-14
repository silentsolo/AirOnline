# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'TheOne'
__mtime__ = '2016/10/12'
# eveytime i know myself better
"""
import torndb
from collections import defaultdict
import json
db = torndb.Connection("192.168.229.134", "air", user="root", password="root")

def  get_all_geo():
    geo_data = defaultdict(list)
    sql = """select city_real, lng, lat
          from allcityaddress"""
    data = db.query(sql)
    for i in  data:
        geo_data[i['city_real']] = [float(i['lng']), float(i['lat'])]
    return geo_data

def get_top_one_data():
    res = []
    sql = """select avg(AQI) as AQI, monthd
             FROM
                    (select AQI, MONTH(datetime) AS monthd
                              from aqidata
                              where city_real='和田'
                              ORDER by datetime) as topone
              GROUP by monthd ORDER by monthd
          """
    data = db.query(sql)
    for i in  data:
        res.append(int(i['AQI']))
    return res

def get_top_aqi_data():
    num = 0
    top5_data = []
    all_data = []
    geo_data = get_all_geo()
    sql = """select city_real ,avg(AQI) as aqi
          from aqidata GROUP BY city_real order by aqi DESC limit 50"""
    data = db.query(sql)
    for i in  data:
        aqi_data = {}
        aqi_data['name'] = i['city_real']
        lng = geo_data[i['city_real']][0]
        lat = geo_data[i['city_real']][1]
        aqi_data['value'] = [float(lng), float(lat) , int(i['aqi'])]
        num += 1
        all_data.append(aqi_data)
        if num  < 6:
            top5_data.append(aqi_data)
    res = {'top5': top5_data, 'alldata': all_data}
    return res

def get_city_data():
    num = 0
    top5_data = []
    all_data = []
    geo_data = get_all_geo()
    sql = """select city_real, AQI as aqi
          from aqidata where city='beijing'"""
    data = db.query(sql)
    for i in  data:
        aqi_data = {}
        aqi_data['name'] = i['city_real']
        lng = geo_data[i['city_real']][0]
        lat = geo_data[i['city_real']][1]
        aqi_data['value'] = [float(lng), float(lat) , int(i['aqi'])]
        num += 1
        all_data.append(aqi_data)
        if num  < 6:
            top5_data.append(aqi_data)
    res = {'top5': top5_data, 'alldata': all_data}
    return res


def distrit_data(req):
    print req
    if req == 'geo':
        return get_all_geo()
    if req == 'topone':
        return get_top_one_data()
    if req == 'top':
        return get_top_aqi_data()
    if req == 'city':
        return get_city_data()
# print get_all_geo()
# print  get_top_aqi_data()
# print get_top_one_data()
print get_city_data()