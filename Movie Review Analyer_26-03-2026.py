reviews = [
    "The movie was amazing",
    "I loved the acting",
    "The film was boring",
    "Terrible movie waste of time",
    "It was okay"
]

positive_words = ["amazing", "loved", "good", "great", "interesting"]
negative_words = ["boring", "terrible", "bad", "waste"]

for review in reviews:
    review_lower = review.lower()

    score = 0

    for word in positive_words:
        if word in review_lower:
            score += 1

    for word in negative_words:
        if word in review_lower:
            score -= 1

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(review)
    print("Sentiment:", sentiment)
    print()