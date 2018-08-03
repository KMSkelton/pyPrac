import sys
import math


def calcNumPizzas(PizzaSlices, pizzaEaterList):
    totalSlices = 0
    for i in range(0, len(pizzaEaterList)):
        totalSlices += pizzaEaterList[i][1]
        i += 1
    numPizzasToPurchase = int(math.ceil(totalSlices / PizzaSlices))
<<<<<<< HEAD
    print(f'Slices in this order: {totalSlices} ')
=======
>>>>>>> 0280d9aec2bca22c6c1c1f10eb888c0b0fe1e915
    print('Pizzas in this order: ', numPizzasToPurchase)
    return numPizzasToPurchase

def getPizzaInputs():
    pizzaEaterList = []
    pizzaEaterListLength = 0
    numberEaters = 0
    while numberEaters < 1:
        try:
            numberEaters = int(input('How many people are eating pizza today? Please enter a whole number.'))
            while numberEaters % numberEaters != 0:
                numberEaters = int(input('How many people are eating pizza today? Please enter a whole number.'))
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
<<<<<<< HEAD
            print(f'Adding {nameEater} to the list.') # They will pay for {numberSlices} slices.
=======
            print(f'Adding {nameEater} to the list. They will pay for {numberSlices} slices.')
>>>>>>> 0280d9aec2bca22c6c1c1f10eb888c0b0fe1e915
            pizzaEaterList.append([nameEater, numberSlices])
        pizzaEaterListLength = len(pizzaEaterList)
    return pizzaEaterList

def calcTotalCost(numPizzasToPurchase, pizzaInputs):
    totalCost = 0
    PizzaCost = float(15.99)
    TaxRate = float(0.101)
    TipRate = float(0.180)
    DeliveryFee = float(3.99)

    subTotal = (PizzaCost * numPizzasToPurchase)
    print(f"Cost for {numPizzasToPurchase} pizza(s) is ${subTotal}")
    subTotalTax = subTotal * TaxRate
    print(f"The tax on this order is ${subTotalTax:.2f}")
    subTotalTip = subTotal * TipRate
    print(f"The 18% tip is: ${subTotalTip:.2f}")
    totalCost += subTotal + subTotalTax + subTotalTip + DeliveryFee
    print(f"The grand total is: ${totalCost:.2f}")
    costEach = totalCost / len(pizzaInputs)
    print(f"The cost per person is: ${costEach:.2f}")


if __name__ == "__main__":
    '''
    static variables related to currency are defined in calcTotalCost
    These will be added to dict before final commit
    '''

    PizzaSlices = 8
    pizzaInputs = getPizzaInputs()
    numPiesToPurch = calcNumPizzas(PizzaSlices, pizzaInputs)
    totalPurchPrice = calcTotalCost(numPiesToPurch, pizzaInputs)