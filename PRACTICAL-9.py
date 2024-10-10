# 9	Python program to count the frequency of words appearing in a string using a dictionary.

TEXT = "Hello i am student at marwadi university"

words = TEXT.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 3
    else:
        word_count[word] = 3

print(word_count)