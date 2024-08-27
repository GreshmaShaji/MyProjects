def reverse_words(sentence):
    words = sentence.split()
    list_of_words = []
    for word in words:
        list_of_words.append(word[::-1])
    return " ".join(list_of_words)

sentence = input("Enter a sentence: ")

print(reverse_words(sentence))