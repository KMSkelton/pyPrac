txt_list = []
list_of_words = []
title_scrape = []
author_scrape = []
with open("./land_time_forgot.txt", "r") as land_time_forgot:
  txt_list = land_time_forgot.readlines()

for word in txt_list:
    split_words = word.split(" ")
    for split_word in split_words:
        list_of_words.append(split_word)

print(list_of_words)
list_length = len(list_of_words)
print(f"The total number of words is {list_length}")


line = txt_list[0].strip()
title, author = line.split(",")
title_scrape.append(title)
author_scrape.append(author)

print("author: ", author_scrape)
print("title: ", title_scrape)

