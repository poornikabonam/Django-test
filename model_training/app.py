from flask import Flask, request, jsonify
from llm_model import LLMModel

app = Flask(__name__)  
model = LLMModel()

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    response = model.generate_text(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
