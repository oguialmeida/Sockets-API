from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    message = request.json['message']
    # Aqui você processa a mensagem recebida do cliente

    response = "Olá cliente"
    return {'response': response}

if __name__ == '__main__':
    app.run()
