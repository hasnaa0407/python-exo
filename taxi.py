# Program to calculate the number of taxis required

# Prompt the user for the number of people
people = int(input("How many people need a ride? "))

# Prompt the user for the capacity of one taxi
capacity = int(input("How many people fit in one taxi? "))

# Calculate the number of full taxis needed
full_taxis = people // capacity

# Check if there are remaining people requiring an extra taxi
if people % capacity != 0:
    full_taxis += 1  # Add one extra taxi for the remaining people

# Print the total number of taxis required
print("Number of taxis needed:",full_taxis)

