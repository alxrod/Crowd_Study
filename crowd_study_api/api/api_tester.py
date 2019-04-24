from requests import Session, Request
import json

base_url = "http://127.0.0.1:8000/api/"
data = {"name": 'Hales Programming', 'password': 'gcrap to do'}
json_data = json.dumps(data)
headers = {'Content-type': 'application/json'}
# print json_data
# response = requests.get(base_url+"all-groups/")
s = Session()
response = Request('POST', base_url+"make-group/", params=data).prepare()
# response2 = Request('GET', base_url+"all-groups/").prepare()
print response.url
print s.send(response)
