import json

cat_dict={"name": "Dino", "favourite_snack": "Dreamies", "breed": "persian", "age": 10}

print(type(cat_dict))

# json.dumps() --> formatted string
#json.dump() --> stream object, file to write to (how you write json file)




# turn dicts to stron to then send it over

cat_json_str = json.dumps(cat_dict)
print(type(cat_json_str))


#with open("new_file.json", "w") as jsonfile:
    #json.dump(cat_dict, jsonfile)

with open("new_file.json", "w") as jsonfile:
    cat = json.load(jsonfile)
    print(cat["name"])
    print(type(cat))