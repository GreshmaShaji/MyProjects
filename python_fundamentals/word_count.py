def word_count(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter sentence : ")
print(f"Number of words: {word_count(sentence)}")