pairs = [
    ("car", "automobile"),
    ("big", "large"),
    ("happy", "joyful"),
    ("teacher", "educator"),
    ("smart", "intelligent")
]

similar_words = {
    "car": "automobile",
    "big": "large",
    "happy": "joyful",
    "teacher": "educator",
    "smart": "intelligent"
}

for w1, w2 in pairs:
    if similar_words.get(w1) == w2:
        print(w1, "-", w2, ": Similar meaning")
    else:
        print(w1, "-", w2, ": Not similar")