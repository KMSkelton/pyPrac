# Dictionaries are great data structures to use for grouping and counting information.
# For this lab, we're going to create a list of names to group by length, and then count how many names occur in each group.
#
# Create the following name list and add in at least five female names (with repeats) to support women in tech!  Use append or extend.
# names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl',
#  'luke', 'robert', 'joseph', 'carl', 'michael', 'mark', 'henry', 'matthew']
# Create an empty dictionary to store your values
# Create a for loop that iterates through the names to add each one to the dictionary along with a count

names = ['mark', 'henry', 'matthew', 'paul', 'robert',
'joseph', 'carl', 'luke', 'mark', 'robert', 'joseph', 'carl',
'michael', 'mark', 'henry', 'matthew']

names.extend(['Denise', 'Summer', 'Jemma', 'Audra', 'Susan'])
# print(names)
names_dict = {}

for name in names:
    if name in names_dict:
        names_dict[name] = names_dict[name] + 1
    else:
        names_dict[name] = 1

# print(names_dict)

print(max(names_dict.values()))
max_value = max(names_dict.values())
# sssstrrrreeeeetch gooooooaaaaaaalllllllll
names_dict_list = list(names_dict.values())
# print(max_index.index(2))
max_index = names_dict_list.index(max_value)
name_dict_keys = list(names_dict.keys())
print(name_dict_keys[max_index])