import asyncio
import aiohttp
import json
from random import choice

# List of sample prompts
prompts = [
    "Write a short story about a robot that learns to love.",
    "Describe a futuristic city in the year 2100.",
    "Explain the theory of relativity in simple terms.",
    # Add more prompts as needed
]

# List of sample texts for summarization
texts = [
    "This is a long text about the history of artificial intelligence...",
    "Here's another text describing the latest advancements in machine learning...",
    # Add more texts as needed
]

# List of sample questions and contexts for question answering
qa_pairs = [
    {
        "question": "What is the capital of France?",
        "context": "Paris is the capital and most populous city of France..."
    },
    {
        "question": "Who invented the telephone?",
        "context": "The telephone was invented by Alexander Graham Bell in 1876..."
    },
    # Add more question-context pairs as needed
]

async def send_request(session, url, payload):
    headers = {"Content-Type": "application/json"}
    async with session.post(url, data=json.dumps(payload), headers=headers) as response:
        print(f"Response status: {response.status}")
        print(await response.text())

async def main():
    url_generate_text = "https://YOUR_API_ID.execute-api.YOUR_AWS_REGION.amazonaws.com/prod/generate-text"
    url_summarize_text = "https://YOUR_API_ID.execute-api.YOUR_AWS_REGION.amazonaws.com/prod/summarize-text"
    url_answer_question = "https://YOUR_API_ID.execute-api.YOUR_AWS_REGION.amazonaws.com/prod/answer-question"

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(10):  # Number of concurrent users
            task_type = choice(["generate_text", "summarize_text", "answer_question"])
            if task_type == "generate_text":
                prompt = choice(prompts)
                payload = {"prompt": prompt}
                task = asyncio.create_task(send_request(session, url_generate_text, payload))
            elif task_type == "summarize_text":
                text = choice(texts)
                payload = {"text": text}
                task = asyncio.create_task(send_request(session, url_summarize_text, payload))
            else:  # answer_question
                qa_pair = choice(qa_pairs)
                payload = {"question": qa_pair["question"], "context": qa_pair["context"]}
                task = asyncio.create_task(send_request(session, url_answer_question, payload))
