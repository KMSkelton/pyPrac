#list
names = ['mark', 'henry', 'matthew', 'paul', 'robert',
         'joseph', 'carl', 'luke', 'mark', 'robert', 'joseph', 'carl'
         'michael', 'mark', 'henry', 'matthew']
#add at leat 4 female name to the list
names.extend(["oury","oury","vieux","awa","annetta"])
#create an empty dictionnary
name_counts = {}
#create a loop that iterates through the names list
for name in names:
    if name in name_counts:
        name_counts[name] = name_counts[name] + 1
    else:
        name_counts[name] = 1
print(name_counts)
#print the most frequent value
max(name_counts)
max(name_counts.keys())
max(name_counts.values())
