#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import json
import datetime

import inserter
import config


def req_to_list():
    
    html_raw = requests.get(config._DATA_URL)
    html_parsed = BeautifulSoup(html_raw.text, 'html.parser')
    json_raw = html_parsed.find('div', attrs={'class': 'json'}).text
    json_list = json.loads(json_raw)

    return json_list


def prnt_list():

    json_dict = req_to_list()
    i = 0
    print("\n")
    for x in json_dict:
        i = i + 1
        print(x)
        print("\n")
    
    print(i)


def prntNice(prnt=False, n=99):

    json_dict = req_to_list()
    length = len(json_dict)
    
    if not isinstance(n, int) or n < 0 or n > 24:
        m = length - 1
    else:
        m = n
        
    lastitem = json_dict[m]
    
    nice = json.dumps(lastitem, sort_keys=True, indent=4, separators=(',', ': '))

    if prnt:
        print(nice)

    return nice


def writeJson(text):

    path = config._DATAPATH
    
    now = "default"
    now = datetime.datetime.now().strftime("%Y%m%d%H")

    with open(path + "wm_" + now + "00.json",'w',encoding = 'utf-8') as f:
        f.write(text)
        
def writeToDB(text):
    
    now = datetime.datetime.now().strftime("%Y%m%d%H%M")
    inserter.from_string(text, now)

text = prntNice()
writeJson(text)
writeToDB(text)

