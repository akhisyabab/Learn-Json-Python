import json

with open('convert_json_to_obj_list.json') as jsonya:
    json_list = json.loads(jsonya.read())
    for lis in json_list:
        print(lis)
    print('----------------')
    for lis in json_list['drinks']:
        print(lis)
