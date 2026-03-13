def get_long_words(words):
    long_words = []
    for word in words:
        if len(word) > 3:
            long_words.append(word)
    return long_words

words = ["semicolon", "chibuzor", "advantage", "hovering", "determination", "agility"]
print(get_long_words(words))
