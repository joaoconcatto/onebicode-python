import json

# 1- Strings para dicionários
person = '{"name":"Joao", "linguagens":["Python", "Javascript"]}'
person_dict = json.loads(person)

print(person_dict)
print(person_dict['linguagens'])


# 2- Convertendo dicionário para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_dict))


# 3- Formatando json
print(json.dumps(person_dict, indent=4, sort_keys=False))


# 4- Salvando json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)
