# We're going to use sets in python to analyze text.
#
# Given the following two sentences, determine:
#
# The number of unique words in each sentence
# The number of words that only appear in both sentences
# The number of words that are contained in either one sentence or the other, but not in both
s1 = "For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man — for precisely the same reasons."

s2 = "The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the message was this: So long and thanks for all the fish."

# For an extra challenge, can you figure out how to remove all the punctuation from the sentences before turning them into a set? See here (Links to an external site.)Links to an external site. for some help.

import re

s1 = re.sub('[^A-Za-z0-9 ]+', '', s1)
s2 = re.sub('[^A-Za-z0-9 ]+', '', s2)

s1 = set(s1.split(" "))
print("les s1: ", len(s1))
# print(s1)
s2 = set(s2.split(" "))
print("len s2: ", len(s2))
# print(s2)

print("len intersection: ", len(s1.intersection(s2)))
print("len symmetric difference: ", len(s1 ^ s2))