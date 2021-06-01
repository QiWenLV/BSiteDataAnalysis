

def flat_json(json_data):
    rst_dict = {}
    for k, v in json_data.items():
        if type(v) == str:
            rst_dict[k] = v
        if type(v) == dict:
            rst_dict.update({k + "#" + ki : vi for ki, vi in flat_json(v).items()})
    return rst_dict