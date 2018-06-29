from random import randrange
def fizzbuzz():
    rando = randrange(50, 100)
    if rando % 15 == 0:
        print("fizzbuzz!")
    elif rando % 5 == 0:
        print("buzz")
    elif rando % 3 == 0:
        print("fizz")
    else:
        print(rando)

fizzbuzz()