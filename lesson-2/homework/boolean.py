#Question 1
username = input("Enter your username: ")
password = input("Enter your password: ")
if username and password:
    print("Login successful.")
else:
    print("Username and password cannot be empty.")

#Question 2
a,b=map(float,input("2 numbers: ").split())
if a==b:
    print("Message")

#Question 3
n=int(input("Number: "))
if n>0 and n%2==0:
    print(f"{n} is positive and even")
else:
    print(f"{n} is not positive and even")

#Question 4
a,g,d=map(float,input('3numbers: ').split())
if a!=g and a!=d and g!=d:
    print(f"{a}, {g} and {d} are different numbers")
else:
    print("They all are not different")

#Question 5
str,d =map(str,input("2 strings: ").split())
if len(str)==len(d):
    print("=")
else:
    print("!=")

#Question 6
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

#Question 7

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if (a + b) > 50.8:
    print("The sum of the two numbers is greater than 50.8.")
else:
    print("The sum of the two numbers is not greater than 50.8.")
num = int(input("Enter a number: "))
if 10 <= num <= 20:
    print("The number is between 10 and 20 (inclusive).")
else:
    print("The number is not between 10 and 20.")
