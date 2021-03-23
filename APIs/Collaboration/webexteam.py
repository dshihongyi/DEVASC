import requests
import json

token = 'NjE5NmRkY2UtOGZiMi00NWY4LTkxN2QtMWEwN2MxMjE3ZjdjZTQyODRmY2EtMmVk_PF84_0198f08a-3880-4871-b55e-4863ccf723d5'

url = 'https://api.ciscospark.com/v1/teams'
headers = {'Authorization': f'Bearer {token}',
           'Content-Type': 'application/json'}

body = {'name': 'Monitor Team'}

post_response = requests.post(
    url, headers=headers, data=json.dumps(body)).json()
# print(post_response)

get_response = requests.get(url, headers=headers).json()
# print(get_response)

teams = get_response['items']
for team in teams:
    if team['name'] == 'Monitor Team':
        teamId = team['id']

room_url = 'https://api.ciscospark.com/v1/rooms'
room_body ={
    'title': "Monitor Room",
    'teamId': teamId
}

room_post = requests.post(room_url, headers=headers, data=json.dumps(room_body)).json()
# print(room_post)

get_room = requests.get(room_url, headers=headers).json()
rooms = get_room['items']
for room in rooms:
    if room['title'] == 'Monitor Room':
        roomId = room['id']


msg_url = 'https://api.ciscospark.com/v1/messages'
msg_body ={
    'roomId': roomId,
    'text':'ALERT MESSAGE: Interface on Device 0006 is Down' 
}

message_response = requests.post(msg_url, 
                    headers=headers, data=json.dumps(msg_body)).json()
            

