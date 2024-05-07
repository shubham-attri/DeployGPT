from flask import Flask, request, jsonify
from flask_cors import CORS
import tasks

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask app is running"

@app.route('/generate-text', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    generated_text = tasks.generate_text(prompt)
    return jsonify({'generated_text': generated_text})

@app.route('/summarize-text', methods=['POST'])
def summarize_text():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    summary = tasks.summarize_text(text)
    return jsonify({'summary': summary})

@app.route('/answer-question', methods=['POST'])
def answer_question():
    question = request.json.get('question')
    context = request.json.get('context')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    if not context:
        return jsonify({'error': 'No context provided'}), 400

    answer = tasks.answer_question(question, context)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
