# Write a Python program to find the sum of odd and even numbers from a set of numbers.
print("***Sum of ODD/EVEn numbers***")
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

# Write a Python program to Check Triangle is Valid or Not
print("\n***Check the triangle is valid or not***")
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

# Check if the sides form a valid triangle
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("It is a valid triangle.")
else:
    print("It is not a valid triangle.")