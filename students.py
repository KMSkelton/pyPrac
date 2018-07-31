"""This is homework 5. I downloaded a book called Sandwiches in txt formate"""
#Save the book Sanwiches txt formate file at current directory
#Read in the file and store lines in a list
SandwichesLinesList = []
for line in open("./land_time_forgot.txt", "r"):
    line = line.strip()
    SandwichesLinesList.append(line)

print(SandwichesLinesList)

#Convert the list of book lines into a list of the words
LineWordsList = []
for line in SandwichesLinesList:
    words = line.split(" ")
    LineWordsList.extend(words)

while '' in LineWordsList:
    LineWordsList.remove('')

print(len(LineWordsList))

#Print a sentence using format with the total number of words and the unique number of words (hint: use a set)
TotalNumber = len(LineWordsList)
LineWordsSet = set(LineWordsList)
UniqueNumber = len(LineWordsSet)

print("The total number of words is {}.\nThe number of unique word is {}".format(TotalNumber, UniqueNumber))

#Calculate the word count for each word.)
WordCountDict = {}
for word in LineWordsList:
    if word in WordCountDict.keys():
        WordCountDict[word] = WordCountDict[word] + 1
    if word not in WordCountDict.keys():
        WordCountDict[word] = 1

list1 = list(WordCountDict.keys())
list2 = list(WordCountDict.values())

for x in list1:
    wordcount = list2[list1.index(x)]
    # print("the word count of '{}' is {}".format(x,wordcount))

#Calculate the word with the maximum count
MaxCount = max(list2)
WordWithMaxCount = list1[list2.index(MaxCount)]

print("The word with the maximum count is '{}'".format(WordWithMaxCount))

#Get the minimum word count
MinCount = min(list2)
print("The minimum count is '{}'".format(MinCount))

#Store all of the words that have the minimum word count in a list
list3 = []
for w in list(LineWordsSet):
    if WordCountDict[w] == MinCount:
        list3.append(w)
    else:
        pass

print(list3)


#Print a sentence including the minimum word count and the number of words with that count
NumberWithMinWordCount = len(list3)
print("The minimum word count is {} and the number of words with the minimum count is {}".format(MinCount,NumberWithMinWordCount))

#Print a sentence of the percentage of words that are unique in the book
percentage = round((UniqueNumber/TotalNumber),4)
print("The percentage of unique words over total words is {}%".format((percentage*100)))