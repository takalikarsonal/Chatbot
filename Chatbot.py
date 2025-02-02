from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm good, thanks!", "I'm doing well!"]],
    ["what is your name?", ["I'm a chatbot!", "I am your virtual assistant."]],
    ["bye", ["Goodbye!", "See you later!"]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
