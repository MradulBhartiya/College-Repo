#Q1 write a programme t0 store age

age = input("Enter your age : ") # age is stored in integer datatype
print("Your age is sucessfully stored that is :-",age)

#Q2 swap variables without using third variables
a = 10 
b = 20

a = a + b
b = a - b # b = a
a = a - b # a = b

#Q3 Take two numbers from users and print their sum,difference product and divison
print("Apply arithmatic operations: ")
a = int(input("Enter first no.: "))
b = int(input("Enter second no.: "))
print("sum of two numbers", a + b)
print("difference of two numbers", b - a)
print("product of two numbers", a*b)
print("division of two numbers", a/b)

#Q4 Take a number form user and check is it even or odd
print("Check weather your number is even or odd")
x = int(input("Enter a number : "))
if(x%2 == 0): print("Number is EVEN") 
else: print("Number is ODD") 

#Q5 Find largest Number among three numbers
print("Find largest number among three numnbers")
p = input("Enter First Number: ")
q = input("Enter Second Number: ")
r = input("Enter Third Number: ")

if(p > q and p > r): print(p, "is largest")
if(q > p and q > r): print(p, "is largest")
else : print(r, "is largest")

#Q6 Calculate your age by date of birth
from datetime import date
dob_input = input("Enter your DOB(YYYY-MM-DD): ")

year,month,day = map(int,dob_input.split("-"))
dob = date(year,month,day)
today = date.today()

#calculate age
currAge = today.year - dob.year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (dob.month, dob.day): currAge -= 1

print("Your age is:", currAge)