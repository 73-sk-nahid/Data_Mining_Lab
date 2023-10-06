# Exercise 4.2
# Write a python program to find the largest number between two numbers using function
def maximum(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    elif x == y:
        return 0
    else:
        return 1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = maximum(num1, num2)

if result == num1:
    print(f"{num1} is largest number")
elif result == num2:
    print(f"{num2} is largest number")
elif result == 0:
    print(f"{num1} & {num2} both equal")
elif result == 1:
    print("Result invalid")
else:
    print("Enter valid number")

# Write a python program to find the sum of the numbers passed as parameters
def sum(x):
    sum = 0
    for i in str(x):
        sum=sum+int(i)
        x = sum
    return x
number = int(input("Enter numbers: "))
result = sum(number)
print("Summation of numbers is:", result)

