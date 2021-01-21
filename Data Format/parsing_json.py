import json
from pprint import pprint

from xmltodict import ParsingInterrupted

with open("address_list.json") as f:
    json_dic = json.load(f)
pprint(json_dic)

print("")

str_dic = """{"people": [{"key_1": "value_1", "key_2": "value_2"}, {"key_3": "value_3", "key_4": "value_4"}]}"""
json_dic = json.loads(str_dic)
pprint(json_dic)
print(json_dic['people'][0])
print(json_dic['people'][1])
print(type(json_dic))
print(type(json_dic["people"]))
print("""############
         #          #
         #          #
         ############""")


with open("sample.json") as f:
    json_dic2 = json.load(f)

pprint(json_dic2)
print(json_dic2["menu"]['popup']['menuitem'][1])

with open("test.json", "w") as f:
    json.dump(json_dic, f,sort_keys=True, indent = 4, ensure_ascii=False)  # Presents the data in proper json format
