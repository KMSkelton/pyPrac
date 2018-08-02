"""
Print a sentence using format with the total number of words and the unique number of words (hint: use a set)
Calculate the word count for each word. (hint: see the section "Counting with Dictionaries")
Calculate the word with the maximum count (hint: use max (Links to an external site.)Links to an external site.)
Get the minimum word count (hint: use values (Links to an external site.)Links to an external site.)
Store all of the words that have the minimum word count in a list (hint: use a for loop and items (Links to an external site.)Links to an external site.)
Print a sentence including the minimum word count and the number of words with that count
Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
"""

f = open("./land_time_forgot.txt")

story_list = list(f.readlines())

# print(story_list)

# #sentence_num = int()
#
# #sentence_num = print(input("Which sentence would you like a word count from? Please enter any sentence number: "))
#
#
# print(story_list[0:-1])
#
# for index, story in enumerate(story_list):
#     print("sentence: '{}' is line {}".format(story, str(index)))
#
# print()
#
# sentence = (story_list[3836])
# #words = sentence.strip('.,?')
# words = sentence.split(' ')

word_count = {}
for x in words:
    if x in word_count:
        word_count[x] = word_count[x] + 1
    else:
        word_count[x] = 1

print(word_count)


#Print a sentence including the minimum word count and the number of words with that count

print("")

#Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
#percent =
#print("This book contains ", percent, "% wrods that are unique.")


#for line in open("./land_time_forgot.txt"):
   # line = line.strip()
 #   print(line)