import json

with open('convert_json_to_obj_ex.json') as json_input:
    try:
        decoded = json.loads(json_input.read())
        for x in decoded['persons']:
            print(x['name'])
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

