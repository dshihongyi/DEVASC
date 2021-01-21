import yaml

with open("address_list.yaml") as f:
    
    yaml_dic = yaml.safe_load(f)

with open("test.yaml", "w") as f:
    yaml.dump(yaml_dic, f)


print(type(yaml_dic['addresses'][2]))
print(type(yaml_dic['addresses']))
print(yaml_dic)
print(yaml_dic['addresses'][1])