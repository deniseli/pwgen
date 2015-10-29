import matplotlib.pyplot as plt
import sys

top_100k_f = "top100k.txt"
pronunciations_f = "cmudict.txt"

def get_pronunciation_from_praw(p, i):
    split = p[i].split("  ")
    return split[1].strip()

def get_word_from_praw(p, i):
    split = p[i].split("  ")
    return split[0].strip().lower()

def binary_search(p, word, lo=126, hi=133904):
    while lo < hi:
        mid = (lo + hi) // 2
        midval = get_word_from_praw(p, mid)
        if midval < word:
            lo = mid + 1
        elif midval > word: 
            hi = mid
        else:
            return mid
    return -1

if __name__ == "__main__":

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

    # Remove homophones
    for i in reversed(range(len(top_words))):
        if i % 100 == 0:
            print("."),
            sys.stdout.flush()
        for j in reversed(range(i + 1, len(top_words))):
            p_i = get_pronunciation_from_praw(pronunciations_raw, binary_search(pronunciations_raw, top_words[i]))
            p_j = get_pronunciation_from_praw(pronunciations_raw, binary_search(pronunciations_raw, top_words[j]))
            if p_i == p_j:
                del top_words[j]

    # Prints out top words as a JavaScript object
    print "var words = ['" + "', '".join(top_words) + "'];"

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
