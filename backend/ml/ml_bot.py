# from transformers import pipeline

# # Load the model once at startup
# chat_pipeline = pipeline("text-generation", model="gpt2")

# def get_bot_response(message: str) -> str:
#     response = chat_pipeline(message, max_length=100, do_sample=True, temperature=0.7)
#     return response[0]['generated_text']

from transformers import pipeline
from ml.kb_bot import get_kb_response

chat_pipeline = pipeline("text-generation", model="distilgpt2")

def get_bot_response(message: str) -> str:
    # Step 1: Try getting a KB-based response
    kb_reply = get_kb_response(message)
    print(f"KB Reply: {kb_reply}")  # Debugging line to check KB response
    if kb_reply:
        return kb_reply

    # Step 2: If no KB response, fallback to LLM
    result = chat_pipeline(message, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']