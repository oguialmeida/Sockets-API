import requests

def send_request(message):
    url = 'http://localhost:5000/api'
    payload = {'message': message}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        received_response = response_data['response']
        print("Resposta do servidor:", received_response)
    else:
        print("Erro ao enviar a solicitação:", response.status_code)

if __name__ == '__main__':
    send_request("Hello")
