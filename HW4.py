# -*- coding: utf-8 -*-
''' Define two lists at the top of your file (you can make them anything, feel free to be creative)
These lists should match up, so Alice’s age is 20, Bob’s age is 21, and so on.
- Use the zip function to merge these lists into a dictionary. (What data type does zip() return? How do you coerce that to the right data type?)
- The names should be the keys, and the age should be the value.
- Ask the user to input an age
- Use a while loop to keep asking the user to input a number until they find a number that is in the dictionary
- Find all people in your dictionary who have the input age, and print out their names and a count ("There are three people with that age; Alice, Frank and Gary.")
'''

names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank",
    "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
results = []
i = 0

if __name__ == "__main__":
    zipList = zip(names, ages)
    print(len(zipList), zipList, zipList[0][1])
    request = int(input('What age of student are you looking for? Enter a single integer. '))

    while( request not in ages ):
            request = int(input('There are no students who meet that criteria. What other age of student would you like to search for? Enter a single integer. '))

    for i in range (0, len(zipList)):
        if request == zipList[i][1]:
            results.append(zipList[i][0])
        i += 1

if(results == {} ):
    print("There are no students who meet that criteria.")
else:
    print("There are {r} students who meet that criteria. They are: {s}.".format(r=len(results), s=", ".join(results)))
