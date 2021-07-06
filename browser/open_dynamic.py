import webbrowser as web
from datetime import datetime
from tools import url_tools
from common.constant import *

def to_obtain_dynamic_list(last_time: datetime):
    data = url_tools.http2json(b_url[MYSELF_DYNAMIC].format("22966665"), url_tools.headers())



def open_myself_dynamic():
    web.register("edge", None, web.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
    web.get("edge").open("www.baidu.com")
