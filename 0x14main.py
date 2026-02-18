paragraph = """ Python is powerful. Python is easy to learn. Python is loved by developers because Python is readable and flexible. """
words = paragraph.lower().split()
unique_words = set(words)
word_freq = {word: words.count(word) for word in unique_words}
sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
top_3 = sorted_freq[:3]
single_occurrence = [word for word, count in word_freq.items() if count == 1]
slice_words = words[5:10]
print("Top 3 Frequent Words:", top_3)
print("Words with Single Occurrence:", single_occurrence)
print("Slice [5:10]:", slice_words)