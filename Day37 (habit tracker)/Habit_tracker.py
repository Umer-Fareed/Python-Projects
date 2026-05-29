import  requests
from datetime import datetime


USER_NAME= "umer-fareed"
TOKEN= "asdfrq5jn234n234112"
pixela_endpoint= "https://pixe.la/v1/users"
GRAPH_ID=  "graph786"


user_params= {
    "token": TOKEN,
    "username": USER_NAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response= requests.post(url=pixela_endpoint, json= user_params)
print(response.text)

graph_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config= {
    "id":GRAPH_ID,
    "name" : "Study Graph",
    "unit" : "minute",
    "type" : "int",
    "color" : "ajisai"
}

headers= {
    "X-USER-TOKEN": TOKEN
}
response= requests.post(url=graph_endpoint,json=graph_config, headers= headers)
print(response.text)


pixel_creation_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today= datetime.now()
pixel_data= {
    "date": today.strftime("%Y%m%d"),
    "quantity":input("how much time you spend on learning today: \n")
}

response= requests.post(url= pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data= {
    "quantity": "240"

}

# response= requests.put(url=update_endpoint,json=new_pixel_data, headers=headers)
# print(response.text)