import sys
import math


def calcNumPizzas(PizzaSlices, pizzaEaterList):
    totalSlices = 0
    for i in range(0, len(pizzaEaterList)):
        totalSlices += pizzaEaterList[i][1]
        i += 1
    numPizzasToPurchase = int(math.ceil(totalSlices / PizzaSlices))
    print('pizzas to purchase: ', numPizzasToPurchase )
    return numPizzasToPurchase

def getPizzaInputs():
    pizzaEaterList = []
    pizzaEaterListLength = 0
    numberEaters = 0
    while numberEaters < 1:
        try:
            numberEaters = int(input('How many people are eating pizza today? Please enter a whole number.'))
            while numberEaters % numberEaters != 0:
                numberEaters = input('How many people are eating pizza today? Please enter a whole number.')
        except:
            print('Please only enter a whole number.')

    # while dict length is shorter than numberEaters continue asking
    while pizzaEaterListLength < numberEaters:
        print(pizzaEaterListLength <= numberEaters)
        # ask for names of eaters
        nameEater = input('Please enter the name of the person eating pizza: ')
        # ask how many slices they are going to eat
        numberSlices = int(input('How many slices will this person eat? '))
        if type(nameEater) == str and type(numberSlices) == int:
            print('Adding {e} to the list. They will pay for {s} slices.'.format(e=nameEater, s=numberSlices))
            pizzaEaterList.append([nameEater, numberSlices])
        pizzaEaterListLength = len(pizzaEaterList)
    return pizzaEaterList

def calcTotalCost(numPizzasToPurchase):
    totalCost = 0
    PizzaCost = float(10.00)
    TaxRate = float(0.096)
    TipRate = float(0.150)
    DeliveryFee = float(3.99)

    subTotal = (PizzaCost * numPizzasToPurchase)
    print(subTotal)
    subTotalTax = subTotal * TaxRate
    print(subTotalTax)
    subTotalTip = subTotal * TipRate
    print(subTotalTip)
    totalCost += subTotal + subTotalTax + subTotalTip + DeliveryFee
    print('$' + "%.2f" % totalCost)


if __name__ == "__main__":
    '''
    static variables related to currency are defined in calcTotalCost
    These will be added to dict before final commit
    '''

    PizzaSlices = 8
    pizzaInputs = getPizzaInputs()
    numPiesToPurch = calcNumPizzas(PizzaSlices, pizzaInputs)
    totalPurchPrice = calcTotalCost(numPiesToPurch)
