# Write a Python program to find the sum of odd and even numbers from a set of numbers.
# Input a set of numbers separated by spaces
numbers = input("Enter a set of numbers separated by comma: ")

# Split the input string into a list of numbers
number_list = [int(x) for x in numbers.split(",")]
#number_list = numbers.split(",")
print(number_list)
# Initialize variables to store the sum of odd and even numbers
sum_even = 0
sum_odd = 0

# Iterate through the numbers and add them to the appropriate sum
for num in number_list:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

# Print the sum of even and odd numbers
print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")


