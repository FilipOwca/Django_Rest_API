import requests

#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"  #http://127.0.0.1:8000/

get_response = requests.get(endpoint, params={"product_id": 123}) # HTTP Request
# print(get_response.text) # print text response
# print(get_response.status_code)

# Http Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json())
# print(get_response.status_code)