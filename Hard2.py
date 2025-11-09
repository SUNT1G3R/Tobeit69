sentence = input()
words = sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

max_count = max(frequency.values())

for word in words:
    if frequency[word] == max_count:
        print(word)
        break
