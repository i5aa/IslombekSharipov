#Question 1
n=float(input(" "))
print(f"{n:.2f}")

#Question 2
a,b,c=map(float,input("Three numbers: ").split())
largest=max(a,b,c)
smallest=min(a,b,c)
print(f"The largest: {largest} \nThe smallest: {smallest}")

#Question 3
km=float(input("Km= "))
metr=km*1000
cm=km*100000
print(f"{km} km equals to {metr} metres or {cm} cantimeters")

#Question 4
e,f=map(float,input("Two numbers: ").split())
div,r=divmod(e,f)
print(f'The result: {int(div)} \nThe remainder: {int(r)}')

#Question 5
cel=float(input("C= "))
print(f"{cel}C equals to {cel*(9/5)+32}F")


#Question 6
g=float(input("Number: "))
print(f"{int(g[-1])} is the last digit")


#Question 7
ch=float(input("Number: "))
if ch%2==0:
    print(f"{ch} is even")
else:
    print(f"{ch} is odd")