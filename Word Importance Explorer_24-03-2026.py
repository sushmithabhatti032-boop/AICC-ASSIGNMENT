from sklearn.feature_extraction.text import TfidfVectorizer

# 5 sample documents
docs = [
    "Artificial intelligence is transforming technology",
    "Machine learning is part of artificial intelligence",
    "Deep learning improves machine learning models",
    "Data science uses machine learning techniques",
    "Artificial intelligence helps robotics and automation"
]

# TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Calculate TF-IDF
tfidf = vectorizer.fit_transform(docs)

words = vectorizer.get_feature_names_out()

# Show top 3 keywords from each document
for i in range(len(docs)):
    scores = tfidf[i].toarray()[0]
    top = scores.argsort()[-3:][::-1]

    print("\nDocument", i+1)
    print("Top Keywords:")
    for j in top:
        print(words[j])