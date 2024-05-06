from flask import Flask, request, jsonify
import tasks

app = Flask(__name__)

@app.route('/generate-text', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    generated_text = tasks.generate_text(prompt)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
