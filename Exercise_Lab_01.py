# Write a Python program to find the largest among three numbers.
print("***Enter three number for finding the largest one among them***")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1 > num2 & num1 > num3:
    print(num1, "is the largest number among three.")
elif num2 > num1 & num2 > num3:
    print(num2, "is the largest number among three.")
else:
    print(num3, "is the largest number among three.")

# Write a Python program to display student grades.
'''grade sheet of GUB:
80-100 = A+
75-79 = A
70-74 = A-
65-69 = B+
60-64 = B
55-59 = B-
50-54 = C+
45-49 = C
40-44 = D
0 -39 = F'''
print("\n \n***Enter mark to display grade***")
while True:
    mark = int(input("Enter your mark(<100):"))
    if (mark>=0 and mark<=100):
        if mark>=80:
            print("You got A+ in this subject")
        elif (mark>=75 and mark<80):
            print("You got A in this subject")
        elif (mark>=70 and mark<75):
            print("You got A- in this subject")
        elif (mark>=65 and mark<70):
            print("You got B+ in this subject")
        elif (mark>=60 and mark<65):
            print("You got B in this subject")
        elif (mark>=55 and mark<60):
            print("You got B- in this subject")
        elif (mark>=50 and mark<55):
            print("You got C+ in this subject")
        elif (mark>=45 and mark<50):
            print("You got C in this subject")
        elif (mark>=40 and mark<45):
            print("You got D in this subject")
        elif mark<40:
            print("You got F in this subject")
        break
    else:
        print("Enter valid mark")

# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum. 
# is even or odd, print out an appropriate message to the user.
print("\n\n***Sum of 3 number and check equal and odd/even***")
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

#calculate the sum of three
sum = a + b + c
print(f"The sum of three number is: {sum}")
#check if the numbers are equal
if a == b == c:
    multiply = a*b*c
print(f"Numbers are equal. Three times of their sum is: {multiply}")
#check the sum is even or odd
if sum % 2 ==0:
    print("Sum is Even number")
else:
    print("Sum is ODD number")