import json
import os

my_dict = {"foo": {"a": 123, "b": "as'df", "c": 1.3, "d": 'qw"rt', "e": "line1\nline2"}}
print(json.dumps(my_dict))
print(json.dumps(my_dict, indent=2))
print(f"MY_VAR2={json.dumps(my_dict)}")
with open(os.environ['GITHUB_OUTPUT'], 'a') as outfile:
    print(f"MY_VAR2={json.dumps(my_dict, indent=2)}", file=outfile)
