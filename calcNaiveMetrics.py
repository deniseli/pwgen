diceware_f = "diceware_word_list.txt"

with open(diceware_f) as f:
    mappings = f.readlines()

length_sum = 0.0
lengths = [0] * 7
for word_map in mappings:
    split = word_map.split("\t")
    length_sum += len(split[1].strip())
    lengths[len(split[1].strip())] += 1

print length_sum / len(mappings)
print lengths
