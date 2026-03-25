import string

text = input("Enter text: ")

# convert to lowercase
text = text.lower()

# remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# remove stopwords
stopwords = ["is", "a", "the", "and", "to", "in", "of"]

words = text.split()
clean_words = [word for word in words if word not in stopwords]

clean_text = " ".join(clean_words)

print("Cleaned text:", clean_text)