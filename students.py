"""Taking what we learned about functions, create a python script that will calculate the cost of pizza for movie night.

Get user input for the following:
Number of people who want pizza
Average number of slices per person
You can store each of these as a single integer, or use a dictionary to map names to slices, up to you
Create the following static (unchanging) variables:
Pizza cost = $15.99
Total slices = 8
Tax rate of 10.1%
Tip rate of 18%
Delivery fee of $3.99
Write functions to calculate:
How many pizzas to order based on number of people and average number of slices
Total pizza cost
Cost per person  """

#Wrap all of the following in a single function definition, then invoke the function (no parameters are needed)
def user_input_pizza():
	eaters = int(input("Please enter number of people who want pizza: "))
	avg_slices = int(input("Please enter the average number of slices per person: "))
	return eaters, avg_slices

#create variables for pizza cost, slices, tax rate, tip rate, delivery fee
pizza_cost = 15.99
slices = 8
tax_rate = .101
tip_rate = .18
delivery = 3.99

#How many pizzas to order based on number of people and average number of slices
def pizzas_to_order(eaters,avg_slices):
	pizzas = (eaters * avg_slices)/slices
	return pizzas

#Total pizza cost
def total_pizza_cost(pizzas):
	total_cost_no_tax = pizza_cost * pizzas
	tax = total_cost_no_tax * tax_rate
	tip = total_cost_no_tax * tip_rate
	overall_total_cost = round(total_cost_no_tax + tax+ tip+ delivery,2)
	return overall_total_cost

#Cost per person
def cost_per_person(overal_total_cost, eaters ):
	cost_per_eater = overal_total_cost/ eaters
	return cost_per_eater

#Final Print statement for showing how many pizzas, total cost and cost per pizza eater
if __name__ == "__main__":
	my_pizza_order = (user_input_pizza())
	pizza_numbers = round(pizzas_to_order(my_pizza_order[0], my_pizza_order[1]))
	print ("You will need to order {} pizzas for dinner".format(pizza_numbers))

	final_dinner_cost = total_pizza_cost(pizza_numbers)
	pizza_eater_cost = round(cost_per_person(final_dinner_cost, my_pizza_order[0]),2)
	print ("The total cost is ${} and the cost per person for dinner is ${}".format(final_dinner_cost, pizza_eater_cost))

#HW6 complete and works!
