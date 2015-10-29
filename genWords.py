import matplotlib.pyplot as plt

top_100k_f = "top100k.txt"
pronunciations_f = "cmudict.txt"

with open(top_100k_f) as f:
    top_100k_raw = f.readlines()

with open(pronunciations_f) as f:
    pronunciations_raw = f.readlines()

# Strip out invalid words
top_words = []
for line in top_100k_raw:
    word = line.strip()
    if word[0] != "#" and  word.lower() == word and word.isalpha():
        top_words.append(word)

# Prune to top 10k words
top_words = top_words[:10000]

'''
# Calculate length distribution
max_len = 20
lengths = [0] * max_len
for word in top_words:
    lengths[len(word)] += 1

# Graph common word lengths
plt.title("Lengths of Common Words")
plt.xlabel("Length (characters)")
plt.xticks(range(max_len))
log_h_histogram = plt.bar(range(max_len), lengths, width=1, color='gray')
plt.show()
'''

print top_words
