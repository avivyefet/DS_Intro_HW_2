
# Assignment 1

# Aviv Yefet

# Q1
def reverse(sentence, reverse_word):
    if isinstance(reverse_word, str) and isinstance(sentence, str):
        if reverse_word in sentence:
            start_po = sentence.find(reverse_word)
            end_index = start_po + len(reverse_word)
            return sentence[0:start_po] + reverse_word[::-1] + sentence[end_index:]
        else:
            return "The word was not found"
    else:
        return "invalid input"


# Tests:
# print(reverse("I like apples and I also, like bananas","also"))               # excepted return: I like apples and I osla, like bananas
# print(reverse("I like apples and I also like bananas", "oranges"))            # excepted return: The word was not found
# print(reverse("I like apples and I also like bananas", "Bananas"))            # excepted return: The word was not found
# print(reverse("I like apples and I also like bananas", 3))                    # excepted return: invalid input

