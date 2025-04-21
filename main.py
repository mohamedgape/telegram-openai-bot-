from flask import Flask, request, jsonify
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)

@app.route('/')
def index():
    return "Chatbot is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    answer = response['choices'][0]['message']['content']
    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run()
