import requests
import json

data = {
    "Nome" : "Kauany",
    "Idade" : 20
}

response = requests.post("https://httpbin.org/post", data = data)
print("Código da Resposta: ", response.status_code)
print("Resposta: ", json.dumps(response.json()))