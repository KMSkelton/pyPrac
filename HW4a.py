names = ["Aliyah", "Bob", "Cathy", "Dan", "Ed", "Frank", "Darnell",
    "Gary", "Shanice", "Irene", "Jack", "Kelly", "Demetrius"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19, 30]

name_dict = dict(zip(names, ages))
print(name_dict)

guesses_used = 0
guesses_avail = 5
while True:
    guesses_used += 1
    if guesses_used > guesses_avail:
        print("You are out of guesses")
        break
    name_requested = input("Whose name are you interested in?")
    if (name_requested in name_dict):
        print(f"Great! {name_requested} is in the dictionary. They are {name_dict[name_requested]} years old.")
        break
    else:
        print(f"Sorry, {name_requested} is not in the dictionary. Please try again")