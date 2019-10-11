def wordPower(word):
    num = {v: k+1 for k, v in enumerate(string.ascii_lowercase)}
    return sum([num[ch] for ch in word])


print(wordPower("hello"))
