import json

my_dict = {"foo": {"a": 123, "b": "as'df", "c": 1.3}}
print(json.dumps(my_dict))
print(json.dumps(my_dict, indent=2))
print(f"MY_VAR='{json.dumps(my_dict)}'")
