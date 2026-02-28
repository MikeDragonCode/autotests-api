import json

json_data = '{"name": "Mike", "age": 31, "isQA": true}'
parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))


data = {
    "name": "Mike",
    "age": 31,
    "isQA": True
}

new_data = json.dumps(data, indent=4)
print(new_data, type(new_data))

with open('json_ex.json', 'r', encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

with open('json_ex_write.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=2)
