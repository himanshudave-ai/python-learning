from collections import Counter

text = input("Enter a sentence: ").lower()

words = text.split()
word_count = Counter(words)

print("Word frequency:")

for word, count in word_count.items():
    print(word, ":", count)