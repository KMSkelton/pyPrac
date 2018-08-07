# Get user input for the following:
# Number of people who want pizza
# Average number of slices per person

import math
people=int(input("Enter number of people eating pizza: "))
people_pizza={}
for i in range(1,people+1):
    people_name=input("Who wants Pizza? ")
    slice_count=int(input("How many slices do you want? "))
    people_pizza[people_name]=slice_count
print(people_pizza)

# How many pizzas to order based on number of people and average number of slices

def total_pizza_order(pizza):
    pizza=math.ceil(sum(people_pizza.values())/8)
    return pizza

# Create the following static (unchanging) variables:
pizza_cost = 15.99
tax_rate = 0.101
tip_rate = 0.18
delivery_fee = 3.99

# Write functions to calculate:

def cost(pizza):
    totalcost=((tax_rate+tip_rate)*(pizza_cost*pizza))+delivery_fee+(pizza_cost*pizza)
    return totalcost

def cost_per_person(totalcost):
    splitcost=totalcost/people
    return splitcost

# Total pizza to order
pizza=total_pizza_order(people)
print("The total number of pizza to order: {}".format(pizza))

# Total pizza cost
totalcost=cost(pizza)
print("The total cost of Pizza is: ${}".format(totalcost))

# Cost per person
splitcost=cost_per_person(totalcost)
print("The total cost per person is: ${}".format(splitcost))