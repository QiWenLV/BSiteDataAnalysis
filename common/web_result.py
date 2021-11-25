def result(data=None):
    return {"code": 0, "data": data}


def result_err(code, msg):
    return {"code": code, "msg": msg}
