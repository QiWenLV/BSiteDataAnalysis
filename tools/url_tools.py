import json
import requests

from config.setting import *

setting = Setting()

def http2json(url, header):
    response = requests.get(url, header)
    if requests is None:
        print(f"{__name__}: 请求错误")
    return json.loads(response.text)


def http2json(url, header, cookies):
    response = requests.get(url, headers=header, cookies=cookies)
    if requests is None:
        print(f"{__name__}: 请求错误")
    response.encoding = 'utf-8'
    return json.loads(response.text)


def headers():
    return {
        ':authority': 'api.vc.bilibili.com',
        ':scheme': 'https',
        ':path': '/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=' + setting.get(Group.config, Key.myid) + '&type_list=8&jsonp=jsonp',
        'accept': 'pplication/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        "content-type": 'application/json;charset=utf-8',
        'cookie': "l=v; " + setting.get(Group.config, Key.cookie),
        'origin': 'https://space.bilibili.com',
        # 'origin': 'https://t.bilibili.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        # 'Referer': 'https://t.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }


def user_agent():
    return {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }


def cookies():
    return {
        'cookie': setting.get(Group.config, Key.cookie)
    }

