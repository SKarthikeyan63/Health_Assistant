from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow frontend requests

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get("message")

    payload = {"sender": "user", "message": message}
    response = requests.post(RASA_URL, json=payload)

    return jsonify(response.json())


if __name__ == '__main__':
    app.run(port=5000, debug=True)


