# Assignment (20/03/2026)
# Assignment Name: Text Challenges

# Description:
# In real-world text data, sentences often contain slang words,
# emojis, spelling mistakes, and extra symbols. These are called
# messy sentences. Before using this data in machine learning,
# we must clean the text using preprocessing.

# Example messy sentences and their issues

sentences = [
"Hey bro, whr r u going? 😂", 
"OMG!! This movie is sooo gud 🔥",
"I cant beleive this happend!!",
"Pls send the doc ASAP 🙏",
"Thx for ur help 😊",
"LOL that was funny 😂",
"Im sooo tired today 😴",
"Wat r u doing tmrw?",
"Gud mrng everyone ☀",
"I luv this song ❤️",
"U coming to party?",
"That game was awsm!!!",
"IDK what to do now 🤔",
"Plz call me later",
"OMG this is gr8 news 🎉",
"Im gonna sleep now 😴",
"Heyyyy how r uuuu?",
"Thnks alot bro",
"See u soon 👍",
"This food is yummm 😋"
]

# Explanation of preprocessing needed

print("Text Preprocessing Needed:\n")

print("1. Remove emojis like 😂 😴 👍")
print("2. Correct spelling mistakes like 'beleive' -> 'believe'")
print("3. Convert slang words like 'u' -> 'you', 'thx' -> 'thanks'")
print("4. Remove extra letters like 'sooo' -> 'so'")
print("5. Convert text to lowercase")
print("6. Remove punctuation and special symbols")

print("\nTotal messy sentences collected:", len(sentences))