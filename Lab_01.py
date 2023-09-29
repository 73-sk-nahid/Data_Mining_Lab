# ****** Variable and String ******
print("Hello World")   # print using print function

msg = 'Hello World'
print(msg)  # print from variable

first_msg = 'Hello Word'
second_msg = 'Welcome to Reality'
combine_msg = first_msg+' '+second_msg  # concatenation strings
print(combine_msg)

# 3.3.5 exercise
# 1st question
first_name = input("Enter your first name: ")
second_name = input("Enter your 2nd name: ")
full_name = first_name+''+second_name
print('Hello '+full_name)

# 2nd question
n = int(input("Enter an integer number: "))
result = n + n*n + n*n*n
print('Result: ',result)

# 3rd question
r = float(input("Enter the value of radius: "))
pie = 3.1416
area = pie*(r*r)
print("The area of circle is: ",area)

# 4th question
#num = int(input("Enter a random number: "))
num = n
if num % 2 == 0:
    print(num,"is EVEN number")
else:
    print(num, "is ODD number")

# 3.4.25 exercise
# 1st question
best_xi = input("Best 11 of Ban XI in CWC-2023: ")
#best_xi = "Litton, Jr. Tamim, Shanto, Sakib, Hridoy, Musfiq, Mahmudullah, Miraz, Shafiul, Taskin, Mustafiz"
x = best_xi.split(",")
print(x)
# 2nd question
colorList = ["Red", "Green", "White", "Black"]
print(colorList[-1])
print(colorList[0])

# exercise 3.5.7
