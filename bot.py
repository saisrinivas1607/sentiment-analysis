import nltk
from textblob import TextBlob

nltk.download('punkt')

def preprocess_text(text):
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    return " ".join(words)

    def get_sentiment(text):
    text = preprocess_text(text)
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "+ve"
    elif analysis.sentiment.polarity < 0:
        return "-ve"
    else:
        return "neutral"

def chatbot():
    print("Chatbot: Hi! How can I assist you today?")

    while True:
        text_input = input("You: ")

        if text_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        sentiment = get_sentiment(text_input)

        if sentiment == "+ve":
            print("Chatbot: That sounds positive!")
        elif sentiment == "-ve":
            print("Chatbot: I'm sorry to hear that.")
        else:
            print("Chatbot: I'm not sure about the sentiment.")

chatbot()