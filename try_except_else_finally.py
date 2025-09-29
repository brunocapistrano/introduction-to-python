import json

def load_data_key(data, key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]
    
json_data = '{"name": "Alice", "age": 30}'

print(load_data_key(json_data, 'city'))