'''
Create a script called hw2.py
Using a single function, gather the following user input and store each item as a variable:
Purchaser name
Purchaser address
Purchaser phone number (entered as 503-555-1211)
Car Make and Model
Purchase Price
After the user inputs the above information, your program should add the following values to the sale price:
Sales tax as a percent of sale price (10.1% combined rate for ZIP 98101)
Licensing fee
Dealer prep fee
Calculate total cost (as a float)
Assign the transaction a unique ID composed of the last four letters of the purchaser's last name and their area code, separated by an underscore
Print out the information to the screen, with the same line breaks as shown in the example below
Make sure your script runs and submit it to canvas as a .py file.
'''
def carBuyer():
    name = input('What is the client\'s full name? ') # we want the last four letters of the client's last name.
    # if the last name is shorter than four letters we need to add filler
    nameSplit = name.split(" ")
    last = nameSplit[1]
    if len(last) < 4:
        filler = 4 - len(last)
        last = last + (filler * "$")

    last4 = last[-4:]

    address = input('What is the client\'s ZIP code? ')

    phone = input('What is the client\'s phone number? (###-###-#### format')
    areaCode = phone.split("-")[0]

    userID = last4 + "_" + areaCode

    carMake = input('What make of car is the buyer interested in? ')
    carModel = input('What model of car is the buyer interested in? ')

    purchPrice = float(input('What is the sticker price of this car? '))
    salesTaxRate = 0.101 # this will let us show the buyer the amount of tax they're paying
    salesTaxCollected = purchPrice * salesTaxRate
    licenseFee = 200.00
    prepFee = 25.00
    totalCost = purchPrice + salesTaxCollected + licenseFee + prepFee

    print(f"Greetings, {name}. Your userID for this purchase is {userID}.",
          f"The purchase price of your {carMake} {carModel} is ${purchPrice:.2f}, plus ${salesTaxCollected:.2f} sales tax, ${licenseFee:.2f} licensing fee and ${prepFee:.2f} dealer prep fees.",
          f"The total price is ${totalCost}.")


carBuyer()

