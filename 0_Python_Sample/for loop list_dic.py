mylist =[{"id": 1, "status": "new", "date_created": "09/13/2013"}, {"id": 2, "status": "pending", "date_created": "09/11/2013"}, {"id": 3, "status": "closed", "date_created": "09/10/2013"}]

for item in mylist:
    print (item)

{'status': 'new', 'date_created': '09/13/2013', 'id': 1}
{'status': 'pending', 'date_created': '09/11/2013', 'id': 2}
{'status': 'closed', 'date_created': '09/10/2013', 'id': 3}

for item in mylist:
    print (item['id'])

# Print Value in single Dictionary
dic = {'status': 'closed', 'date_created': '09/10/2013', 'id': 3}
for key, value in dic.items():
    if key == 'status':
        print(value)