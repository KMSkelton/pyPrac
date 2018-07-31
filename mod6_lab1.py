# Update the code to have a function that reads in the file and returns contents as a list
def open_sample_func(sample_text):
    with open(sample_text) as file:
        lines = file.readlines()
        return lines

# Update the code to have a function that converts the list of book lines into a list of the words
def word_list_func(lines):
    word_list = []
    for line in lines:
        word_list.extend(line.strip().split(" "))
    return word_list

def word_count_func(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    return word_count

# Update the code to have a function that calculates the minum word frequency
#  and gets the list of words from the word frequency dictionary
def min_word_func(word_count):
    min_word_count = min(word_count.values())
    min_words = []
    for word, fr in word_count.items():
        if fr == min_word_count:
            min_words.append(word)
    print("The lowest word count is {} and there are {} words in "
          "the book with that word_count".format(min_word_count, len(min_words)))
    return min_words

# I made each of the given operations into its own function that returns the value(s) calculated
# This is the only function I wrote, which only calls each of the above functions
# Functions created with parameters require arguments. We can create those arguments inside the
# function that invokes all the others

# Create a main section at the bottom of the code
if __name__ == '__main__':
    # Update the main section to call the function that reads the file
    # and the function that converts the book lines into a list.
    # Remember to pass the appropriate variable into the function
    # and return the value you want and store it in a variable
    sample_text = "./land_time_forgot.txt"
    lines = open_sample_func(sample_text)
    word_list = word_list_func(lines)

    word_count = word_count_func(word_list)
    # Update the main section to call the function that calculates the word count
    # and find the word with the maximum count (hint: use max)
    max_word = max(word_count, key=word_count.get)
    print(f"The word with the most appearances is: {max_word}. It appears {word_count[max_word]} times.")

    min_word_func(word_count)

# Update the main section to create a word set and print the sentence about unique words
word_set = set(word_list)
print("There are {} words in the book and {} of them are unique".format(
    len(word_list), len(word_set)))
