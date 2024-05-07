from flask import Flask, request, jsonify
from flask_cors import CORS
import psutil
import logging
import os
import tasks

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/')
def home():
    """
    This function returns a string indicating that the Flask app is running.
    """
    return "Flask app is running"

@app.route('/generate-text', methods=['POST'])
def generate_text():
    """
    Generate text based on the provided prompt.

    Returns:
        A JSON response containing the generated text.
    """
    prompt = request.json.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # Log RAM consumption
    ram_usage = psutil.Process(os.getpid()).memory_info().rss
    # The `rss` attribute of `memory_info()` returns the Resident Set Size (RSS),
    # which represents the amount of memory currently occupied by the process.
    # This can be used to monitor the RAM consumption of the application.

    # Rest of the code...
    logging.info(f"RAM usage for generate-text request: {ram_usage} Mb")

    generated_text = tasks.generate_text(prompt)
    return jsonify({'generated_text': generated_text})

@app.route('/summarize-text', methods=['POST'])
def summarize_text():
    """
    Summarizes the provided text.

    Retrieves the text from the request JSON payload and checks if it exists.
    If the text is not provided, it returns an error response.
    Logs the RAM consumption for the summarize-text request.
    Calls the `summarize_text` function from the `tasks` module to generate the summary.
    Returns the summary as a JSON response.

    Returns:
        A JSON response containing the summary.

    """
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Log RAM consumption
    ram_usage = psutil.Process(os.getpid()).memory_info().rss
    logging.info(f"RAM usage for summarize-text request: {ram_usage} bytes")

    summary = tasks.summarize_text(text)
    return jsonify({'summary': summary})

@app.route('/answer-question', methods=['POST'])
def answer_question():
   
    """
    Answer a question based on the provided question and context.

    Returns:
        A JSON response containing the answer to the question.

    Raises:
        - 400 Bad Request if no question or context is provided.
    """
    
    question = request.json.get('question')
    context = request.json.get('context')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    if not context:
        return jsonify({'error': 'No context provided'}), 400

    # Log RAM consumption
    ram_usage = psutil.Process(os.getpid()).memory_info().rss
    logging.info(f"RAM usage for answer-question request: {ram_usage} bytes")

    answer = tasks.answer_question(question, context)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
