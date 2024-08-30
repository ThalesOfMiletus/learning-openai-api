from senha import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

link = "https://api.openai.com/v1/chat/completions"

id_model = "gpt-4o-mini"

data = {
    "model": id_model,
    "messages": [
        {"role": "user", "content": "Me dê dicas para um hackathon de 12 horas"}
    ]
}

data = json.dumps(data)

requisition = requests.post(link, headers=headers, data=data)

print(requisition)
print(requisition.text)
# resposta = requisition.json()

# resposta_gpt = resposta["choices"][0]["message"]["content"]

# print(resposta_gpt)
