def validNumber(startNum):
    if startNum <= 0 or not startNum:
        startNum = int(input('Please enter two numbers. The first must be a whole number that is 1 or greater.  '))
    if startNum < 1:
        validNumber()
    endNum = int(input('Please enter your second number. It must be at least five times larger than the first number.  '))
    if endNum < (startNum * 5):
        [starNum, endNum] = validNumber(startNum)
    return [startNum, endNum]

if __name__ == "__main__":
    startNum = 0
    numList = validNumber(startNum)
    oddTotal = 0
    odderList = []
    print(numList[0])
    print(numList[1])
    #create range of ints
    numRange = list(range(numList[0], numList[1]+1))
    print('The number range is: ', numRange)

    for num in numRange:
        if num % 2 == 0:
            print ('Number: ', num, ' at index: ', numRange.index(num))
        else:
            oddTotal += num
    print('The total of odd values is: ', oddTotal)
    print("\n\n\n\n\n or save one function call with built in methods: ")
    for idx, x in enumerate(numRange):
        if x % 2 == 0:
            print("value: ", x, "index: ", idx)
        else:
            odderList.append(x)
    print("Odd total: ", sum(odderList), " odd values: ", odderList)
