import json
from difflib import get_close_matches

# Load your knowledge base
with open("ml/finance_kb.json", "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)  # this must be a list of dicts

# Ensure data is correct
assert isinstance(knowledge_base, list), "Knowledge base must be a list of Q&A objects."

# Convert to a dict {question: answer}
kb_data = {item["question"].lower(): item["answer"] for item in knowledge_base}

def get_kb_response(user_message: str, threshold: float = 0.6) -> str:
    user_message = user_message.lower().strip()
    questions = list(kb_data.keys())

    match = get_close_matches(user_message, questions, n=1, cutoff=threshold)
    if match:
        return kb_data[match[0]]
    
    return None
