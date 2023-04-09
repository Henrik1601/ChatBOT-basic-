import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["my name is (.*)", ["Hi %1, how can I assist you today?"]],
    ["(hi|hello|hey|holla|howdy)", ["Hello, how can I assist you today?"]],
    ["what is your name?", ["My name is Chatbot, how can I assist you today?"]],
    ["how are you?", ["I am doing well, thank you for asking. How can I assist you today?"]],
    ["what can you do?", ["I can assist you with tasks such as answering questions or providing recommendations. How can I assist you today?"]],
    ["bye|goodbye", ["Goodbye, have a nice day!"]],
]

chatbot = Chat(pairs, reflections)

chatbot.converse()
