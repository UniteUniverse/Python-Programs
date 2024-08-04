pixel_endpoint=f"{graph_endpoint}/{graph_id}"
pixel_parameters={
    "date":"20240722",
    "quantity":"2.5"
}
response=requests.post(url=pixela_endpoint,json=pixel_parameters,headers=headers)
print(response.text)
