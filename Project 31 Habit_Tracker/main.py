# For checking please comment down first the last response which has delete method then one by one from beginning comment out the reponse blocks.
import requests
import datetime as dt
Username="pratyushjha"
TOKEN="cdwndcnw123sncn"
today=dt.datetime.now()

pixela_endpoint="https://pixe.la/v1/users"
user_parameters={
    "token":TOKEN,
    "username":Username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint,json=user_parameters)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{Username}/graphs"
graph_id="acbjabcb1"
graph_parameter={
    "id":graph_id,
    "name":"Running",
    "unit":"km",
    "type":"float",
    "color":"sora"
}
headers={
    "X-USER-TOKEN":TOKEN,
    "agreeTermsOfService":"yes"
}
# response=requests.post(url=graph_endpoint,json=graph_parameter,headers=headers)
# print(response.text)
pixel_endpoint=f"{graph_endpoint}/{graph_id}"
pixel_parameters={
    "date":today.strftime("%Y%m%d"),
    "quantity":"5"
}
# response=requests.post(url=pixel_endpoint,json=pixel_parameters,headers=headers)
# print(response.text)
update_parameters={
    "quantity":"4"
}
# response=requests.put(url=f"{pixel_endpoint}/20240721",json=update_parameters,headers=headers)
# print(response.text)

response=requests.delete(url=f"{pixel_endpoint}/20240721",headers=headers)
print(response.text)
