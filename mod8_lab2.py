try:
    open("nonexistent.txt")
except FileNotFoundError:
    print("Sorry, that file doesn't exist.")
except:
    print("I'm not sure what you're trying to do")