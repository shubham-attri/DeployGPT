import torch

from transformers import pipeline

# Generate text using the GPT-2 model pipeline, calling it outside the function to avoid loading it every time
generator = pipeline('text-generation', model='gpt2')


#High level Pipeline helper for summarization, calling it outside the function to avoid loading it every time, using the facebook/bart-large-cnn model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#high level pipeline for question answering using the deepset/roberta-base-squad2 model
model_qa = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')


def generate_text(prompt, max_length=100): 
    '''
    Generate text using the GPT-2 model pipeline.
    Args:
        prompt (str): The input prompt for text generation.
        max_length (int): The maximum length of the generated text.'''
    
    text = generator(prompt, max_length=max_length)
    return text[0]['generated_text']

def summarize_text(text, max_length=100, min_length=30, do_sample=False):
    '''
    Summarize text using the BART model pipeline.
    Args:
        text (str): The input text to be summarized.
        max_length (int): The maximum length of the summary.
        min_length (int): The minimum length of the summary.
        do_sample (bool): Whether to use sampling for generation.'''

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text']
    

def answer_question(question, context, max_length=100, num_beams=4):
        '''
        Answer a question based on a context using the RoBERTa model pipeline.
        Args:
            question (str): The question to be answered.
            context (str): The context in which the question is asked.
            max_length (int): The maximum length of the generated answer.
            num_beams (int): The number of beams to use for beam search.'''
            
        answer = model_qa(question=question, context=context, max_length=max_length, num_beams=num_beams)
        
        return answer['answer']
    


