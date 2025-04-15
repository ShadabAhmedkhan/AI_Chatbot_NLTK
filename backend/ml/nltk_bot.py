from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey|yo|good (morning|afternoon|evening)", 
     ["Hello there!", "Hey!", "Hi! How can I help you?"]],
    
    [r"how (are|r) (you|u)\??", 
     ["I'm doing great, thanks for asking!", "Feeling fantastic. You?"]],
    
    [r"(what('| i)?s|tell me) (your|ur) name\??", 
     ["I'm NLTKBot, your friendly assistant."]],
    
    [r"(.*)(help|assist)(.*)", 
     ["Sure, I'm here to help. What do you need assistance with?"]],
    
    [r"(.*)(weather|temperature)(.*)", 
     ["Sorry, I can't check the weather yet. But I can chat with you!"]],
    
    [r"(bye|quit|exit|see you)", 
     ["Goodbye! Have a nice day!", "Bye! Come back soon!"]],
    
    [r"(.*)", 
     ["Interesting... Tell me more!", "Why do you say that?", "Let's talk more about that."]]
]

chatbot = Chat(pairs, reflections)

def get_bot_response(message: str) -> str:
    return chatbot.respond(message)
