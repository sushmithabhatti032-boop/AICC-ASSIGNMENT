# Assignment (19/03/2026)
# Mini Project Proposal

# Project Title: Spam Message Detection System

# Problem Statement:
# Spam messages are unwanted messages that contain advertisements,
# fake offers, or harmful links. These messages create inconvenience
# for users. The aim of this project is to create a simple system
# that can identify whether a message is Spam or Not Spam.

# Dataset:
# A small dataset of messages is created directly in the program.

# Examples:
# "Win money now" – Spam
# "Free gift offer" – Spam
# "Hello friend" – Not Spam
# "Meeting tomorrow" – Not Spam

# Algorithm:
# This project uses the Naive Bayes algorithm.
# It is commonly used for text classification tasks such as spam detection.

# Expected Output:
# The user enters a message and the system predicts whether it is
# Spam or Not Spam.


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample messages
messages = ["Win money now", "Free gift offer", "Hello friend", "Meeting tomorrow"]
labels = ["Spam", "Spam", "Not Spam", "Not Spam"]

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train the model
model = MultinomialNB()
model.fit(X, labels)

# User input
msg = input("Enter message: ")

# Predict result
msg_vector = vectorizer.transform([msg])
result = model.predict(msg_vector)

print("Prediction:", result[0])