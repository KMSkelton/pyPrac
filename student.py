salesTaxRate = float(0.101)
licenseFee = 50.00
dealerPrepFee = 50.00

purchName = input ('Please enter your full name. ')

# purchAddress = input('Please enter your address. ')

def validNumber():
    purchPhone = input('Please enter your phone number in the format xxx-xxx-xxxx. ' )
    if len(purchPhone) != 12:
            validNumber(purchPhone)
    for i in range(12):
        if i in [3,7]:
            if purchPhone[i] != '-':
                print('That is not the correct format. Please try again.')
                purchPhone = input('Please enter your phone number in the format xxx-xxx-xxxx. ' )
        elif not purchPhone[i].isalnum():
                print('That is not the correct format. Please try again.')
                purchPhone = input('Please enter your phone number in the format xxx-xxx-xxxx. ' )
        return purchPhone
purchPhone = validNumber()

carMakeModel = input('Which vehicle are you buying? Make and model. ')

purchPrice = float(input('How much is the purchase price? '))
print("purchPrice: ", purchPrice)
salesTax = purchPrice * salesTaxRate
print("salesTax: {:.2f}".format(salesTax))

totalCost = purchPrice + salesTax + licenseFee + dealerPrepFee
totalCost = float("{:.2f}".format(totalCost))
print('totalCost: ', totalCost)

# carID = purchName[-4:] + '_' + purchPhone[:3]
# carID = carID.replace(carID[0], 'Z')

carID = purchPhone[:3] + '_' + purchName[-4:].replace(purchName[-4], 'X')
# carID = carID.replace(carID[-4], 'Z')

# basic method
print('Hello ' + purchName + ' thank you for your interest in ' + carMakeModel + ', vehicle #' + carID + '.')
# advanced, paying a lot of attention method
print('Hello {} thank you for your interest in {}, vehicle #{}.'.format(purchName, carMakeModel, carID))
print('\n\n\nThe price for this {} is {:.2f} plus ${:.2f} in sales tax, plus ${:.2f} in licensing fees.\nThere is a dealer processing fee of ${:.2f}. Your total is: ${:.2f}.\nThank you for shopping Python Motors!'.format(carMakeModel, purchPrice, salesTax, licenseFee, dealerPrepFee, totalCost) )
# named placeholders, more flexibility with list order
print('Hello {pn} thank you for your interest in {car}, vehicle #{lic}.'.format(car=carMakeModel, pn=purchName, lic=carID))

# Concatenated with inline formatting
print('The price for this ' + carMakeModel + ' is ' + "{:.2f}".format(purchPrice) + ' plus $' + "{:.2f}".format(salesTax) + ' in sales tax, plus $' + ("{:.2f}".format(licenseFee)) + ' in licensing fees. There is a dealer processing fee of $' + ("{:.2f}".format(dealerPrepFee)) + '. Your total is: $' + ("{:.2f}".format(totalCost)) + '. Thank you for shopping Python Motors!' )

# f-strings method
print("\nf-strings method:")
print(f'The price for this {carMakeModel} is ${purchPrice:.2f} plus ${salesTax:.2f} in sales tax, plus ${licenseFee:.2f} in licensing fees. There is a dealer processing fee of ${dealerPrepFee:.2f}. Your total is: ${totalCost:.2f} Thank you for shopping Python Motors!' )
