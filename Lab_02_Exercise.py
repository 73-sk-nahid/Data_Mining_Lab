# Exercise 3.1.2
# Write a python program to find the sum of odd and even numbers from a set of numbers
print("***Find the sum of ODD & EVEN Numbers***")
numbers = [5, 4, 3, 2, 1]
even_sum = 0
odd_sum = 0
for i in numbers:
    if i % 2 == 0:
        print(f"{i} is Even number")
        even_sum = even_sum + i
    else:
        print(f"{i} is Odd number")
        odd_sum = odd_sum + i

print(f"Sum of Even_numbers are: {even_sum} \nSum of Odd_numbers are: {odd_sum}")

# Write a python program to find the smallest number from a set of numbers
print("\n***Find the smallest number***")
small = 0
for i in numbers:
    if small == 0:
        print(f"Small is null. So, Small number is {small}")
        small = i
    elif i<small:
        print(f"{i}is smaller then {small}")
        small = i
print(f"So, Smallest number is: {small}")

# Write a python program to find the sum of all numbers between 50 and 100, which are divisible by 3 and not divisible by 5
print("***\nSum of 50-100 which is divisible by 3 but not divisible by 5***")
sum = 0
for i in range(50, 101):
    if(i % 3 == 0 and i % 5 != 0):
        sum += i
print(f"Sum is: {sum} ")

# Write a python program to find the second highest number from a set of numbers
print("\n***Find the second sortest number***")
sorted_numbers = sorted(numbers)
print(f"Sorted numbers are: {sorted_numbers}")
print(f"The second highest numbe is: {sorted_numbers[-2]}")

# Write a python program to find the factorial of a number using for loop.
print("\n***Find the factorial of a number***")