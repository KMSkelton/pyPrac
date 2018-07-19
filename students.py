test_string_a = "For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man — for precisely the same reasons"

# strings
a = set(test_string_a.split(" "))

test_string_b = "The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the message was this: So long and thanks for all the fish"

b = set(test_string_b.split(" "))

# The number o unique words in each sentence
c = a.difference(b)
print(c)
print(len(c))

e = b.difference(a)
print(e)
print(len(e))

# The number of words that appear in oth sentences
f = a.intersection(b)
print(f)
print(len(f))

# The number of words that are contained in either one sentence or the other, but not in both
g = a.symmetric_difference(b)
print(g)
print(len(g))

h = b.symmetric_difference(a)
print(h)
print(len(h))


