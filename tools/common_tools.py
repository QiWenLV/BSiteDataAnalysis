
def flat_json(json_data):
    rst_dict = {}
    for k, v in json_data.items():
        type_v = type(v)
        if type_v == dict:
            rst_dict.update({k + "#" + ki : vi for ki, vi in flat_json(v).items()})
        elif type_v == list:
            pass
        else:
            rst_dict[k] = v
    return rst_dict
