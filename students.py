
#
# Two lists defined for program - List of names and ages
#

names = ["Aliyah", "Bob", "Cathy", "Dan", "Ed", "Frank", "Darnell",
         "Gary", "Shanice", "Irene", "Jack", "Kelly", "Demetrius"]

# convert the names to lower-case for fun, profit and easy validation
l_names = [x.lower() for x in names]

ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19, 30]


#
# Variable "comment" to determine "type" of a zip
#

comment = zip(names, ages)
print('Note performing zip function on lists transforms them to a dataclass a type of:  ', type(comment))

#
# Merged zip file into a dictionary using lowercase names
#

bio_dict = dict(zip(l_names, ages))

print('So lets use the dict function and make it a dataclass a type of: ', type(bio_dict))


# Maximum number of guesses is limited to value of numTries

numTries = 5
usedTries = 0

while True:
    usedTries = usedTries + 1
    if usedTries > numTries:
        print("No more attempts allowed this round. Chow!")
        break
    u_guess = str(input("Kindly input the name of person in our realm to ascertain their age: "))
    all_lower = u_guess.lower()
    if all_lower in bio_dict:
        print(all_lower, "is the fine age of:", bio_dict[all_lower])
        continue
    else:
        print("Bonk...no person with that name is in this realm. Kindly try again: ")
        continue

