import json

with open('convert_json_to_obj_dict.json') as f:
    python_obj = json.loads(f.read())
    print(python_obj['name'])
