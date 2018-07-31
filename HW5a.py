# Print a sentence using format with the total number of words and the unique number of words (hint: use a set)

txt_list = []
list_of_words = []
with open("./land_time_forgot.txt", "r") as land_time_forgot:
  txt_list = land_time_forgot.readlines()

for word in txt_list:
    split_words = word.strip().split(" ")
    # I guess stripping is important so all instances of 'the' are captured, whether they have trailing
    # punctuation or not
    for split_word in split_words:
        # remove the empty lines, which cuts down on total number of words and unique words
        if split_word == '':
            continue
        list_of_words.append(split_word)


# print(list_of_words)
list_length = len(list_of_words)
list_words_set_length = len(set(list_of_words))
print(f"The total number of words is {list_length}")
print(f"The total number of unique words is {list_words_set_length}")

# Calculate the word count for each word. (hint: see the section "Counting with Dictionaries")
word_counts = {}
for word in list_of_words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# print(word_counts)

# Calculate the word with the maximum count (hint: use max (Links to an external site.)Links to an external site.)
most_common_word = max(word_counts, key=word_counts.get)
# print(most_common_word)
print(f"'{most_common_word}' is the most common word. How often does '{most_common_word}' appear? ", word_counts[most_common_word])

# Get the minimum frequency (hint: use values (Links to an external site.)Links to an external site.)
word_counts_values_sorted = sorted(word_counts.values())
# print("word counts values, sorted: ", word_counts_values_sorted[0])

# Store all of the words that have the minimum frequency in a list (hint: use a for loop and items (Links to an external site.)Links to an external site.)
minimum_count_words = []
lowest_accepted_value = int(1)
for words, count in word_counts.items():
    if count == lowest_accepted_value:
        minimum_count_words.append(words)
    else:
        continue
print(minimum_count_words)

# Print a sentence including the minimum word count and the number of words with that count
print(f"The fewest times a word appears is {word_counts_values_sorted[0]}, and there are {len(minimum_count_words)} words that appear {word_counts_values_sorted[0]} times/s")

# Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
percent_unique = list_words_set_length / list_length * 100
print(f"The percentage of unique words is {list_words_set_length} / {list_length} = {percent_unique:.1f}%")
