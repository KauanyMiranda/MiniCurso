import requests 
import json

response = requests.get("https://httpbin.org/get")

print("Código da Resposta: ", response.status_code)
print("Resposta: ", json.dumps(response.json()))
