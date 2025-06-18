import ast
import json

with open("returned_output.txt", "r") as file:
    content = file.read()
    # print(content)
    res = ast.literal_eval(content)
    # print(type(res))
    # content = dict(content)
    
with open("expected_output.json", "w") as file:
    json.dump(res, file, indent=4)