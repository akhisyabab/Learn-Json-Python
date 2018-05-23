import json
from decimal import Decimal

with open('convert_json_to_obj_float.json') as number:
    python_obj = json.loads(number.read(), parse_float=Decimal)
    print(python_obj['number'])
    print(type(python_obj['number']))
