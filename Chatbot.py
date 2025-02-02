from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm good, thanks!", "I'm doing well! How about you?"]],
    ["what is your name?", ["I'm a chatbot!", "I go by Chatbot."]],
    ["bye", ["Goodbye!", "See you later!"]],
    ["what can you do?", ["I can chat with you, answer questions, and tell jokes!"]],
    ["tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]],
    ["what is your favorite color?", ["I like all colors, but blue is nice!"]],
    ["where are you from?", ["I'm from the cloud! I don't have a physical location."]],
    ["how old are you?", ["I don't age! I'm timeless."]],
    ["can you help me?", ["Sure! What do you need help with?"]],
    ["who created you?", ["I was created by a developer using Python."]],
    ["tell me a fact", ["Did you know honey never spoils? Archaeologists have found pots of honey in ancient tombs that are still edible!"]],
    ["what time is it?", ["Sorry, I can't check the time right now."]],
    ["what is your purpose?", ["My purpose is to chat with you and make your day better!"]],
    ["do you like music?", ["I think music is wonderful! It can be so relaxing or energizing."]],
    ["can you play music?", ["I can't play music, but I can recommend some! What genre do you like?"]],
    ["what is the weather like?", ["I can't check the weather, but you can use a weather app or website to find out."]],
    ["do you know any trivia?", ["Sure! Did you know that the Eiffel Tower can grow by 6 inches in the summer due to the expansion of iron?"]],
    ["what is Python?", ["Python is a popular programming language used for web development, data analysis, machine learning, and much more!"]],
    ["are you real?", ["I am a program, so not quite 'real,' but I can still have a conversation with you!"]],
    ["can you speak other languages?", ["I can understand and respond in many languages! What language would you like to chat in?"]],
    ["do you have feelings?", ["I don't have feelings like humans, but I am here to listen and help you!"]]
]


chatbot = Chat(pairs, reflections)

print("Welcome to Simple Chatbot! Say bye to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response if response else "I'm not sure how to respond to that.")
