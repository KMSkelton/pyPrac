def cheeseInfo():
    name = input("What is your name?  ")
    phone = input("what is your phone number in xxx-xxx-xxxx format?  ")
    cheese = input("What's your favorite cheese, {} ?  ".format(name))
    funds = int(input("How much do you spend each month on {} ?  ".format(cheese)))

    daily = funds / 30
    lastFourNum = phone.split("-")[2]
    firstThreeLetter = name[:3]
    accountID = firstThreeLetter + lastFourNum
    accountID = accountID.replace(accountID[0], "Z")

    print("Wow User {}, you spend ${:.2f} every day on {}. You might want to think about financial planning.".format(accountID, daily, cheese))

cheeseInfo()
