from web.service.home import *
from web.service.black_list import *


def setup_routes(app):
    # -------------------home
    # 获取动态列表
    app.router.add_get('/api1/{date}/{limit}', get_home_table)
    # 打开动态
    app.router.add_post('/api/open', post_open_dynamic)
    # 获取初始化参数
    app.router.add_get('/api/home_param', get_home_param)

    # -------------------black_list
    # 获取关注列表
    app.router.add_get('/api/case/list', get_case_list)
    # 更改一个关注up的关注类型 [0=正常，1=特别关注，2=黑名单]
    app.router.add_post('/api/case/change', set_change_one)
