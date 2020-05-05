def is_pangram(sentence):
    letters = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.replace(" ", "")
    sentence = sentence.replace(".", "")
    sentence = sentence.replace('\"', '')
    if len(sentence) < 26:
        return False
    sentence = set(sentence.lower())
    alphabets = set(letters)
    if len(sentence&alphabets) != 26:
        return False
    return True
