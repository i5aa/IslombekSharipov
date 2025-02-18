#Question 1
my_list = input("Enter elements separated by space: ").split()
element_to_count = input("Enter element to count: ")
count = 0
for item in my_list:
    if item == element_to_count:
        count += 1
print(count) 

#Question 2
a = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
print("Total sum of elements:", sum(a))

#Question 3
b=list(map(float,input("Enter numbers seperated by space: ").split()))
print(max(b))

#Question 4
c=list(map(float,input("Enter numbers seperated by space: ").split()))
print(min(c))

#Question 5
d=list(map(str,input("Enter elements seperated by space: ").split()))
e=input("Enter element to check: ")
if e in d:
    print("Yes")
else:
    print("No")

#Question 6
f=list(map(str,input("Enter characters seperated by space: ").split()))
if f:
    print(f[0])
else:
    print("Null")

#Question 7
g=list(map(str,input("Enter characters seperated by space: ").split()))
if g:
    print(g[-1])
else:
    print("Null")

#Question 8
h = list(map(str, input("Enter elements separated by space: ").split()))
print("New list contains:", " ".join(h[:3]))

#Question 9
i = list(map(str, input("Enter elements separated by space: ").split()))
print("Reversed list:", " ".join(i[::-1]))

#Question 10
j = list(map(str, input("Enter elements separated by space: ").split()))
print("New list contains:"," ".join(sorted(j)))

#Question 11
k = list(map(str, input("Enter elements separated by space: ").split()))
k=list(set(k))
print("Unique list contains: "," ".join(k))

#Question 12
l = list(map(str, input("Enter elements separated by space: ").split()))
m=int(input("What index to insert: "))
n=input("What to insert: ")
l.insert(m,n)
print(' '.join(l))

#Question 13
o = list(map(str, input("Enter elements separated by space: ").split()))
p=input("What element to check: ")
index=o.index(p)
print(f"First occurance of {p} is at index  {index}")

#Question 14
q= list(map(str, input("Enter elements separated by space: ").split()))
if q:
    print(bool(1))
else:
    print(bool(0))

#Question 15
r = list(map(int, input("Enter integer numbers separated by space: ").split()))
s=sum(1 for item in r if item%2==0)
print(f"There are {s} even numbers in {r}")

#Question 16
t = list(map(int, input("Enter integer numbers separated by space: ").split()))
u=sum(1 for item in t if item%2!=0)
print(f"There are {u} odd numbers in {t}")

#Question 17
v = list(map(str, input("Enter list's elements seperated by space: ").split()))
x = list(map(str, input("Enter list's elements seperated by space: ").split()))
print('New list:'," ".join(v+x))

#Question 18
main_list = list(map(str,input("Enter main list: ").split()))
sub_list = list(map(str,input("Enter sublist: ").split()))
exists = any(main_list[i:i+len(sub_list)] == sub_list for i in range(len(main_list) - len(sub_list) + 1))
print("Sublist exists:", exists)

#Question 19
l=list(map(str,input("Enter elements seperated by space: ").split()))
old_element=input("What element should be replaced: ")
new_element=input("New element: ")
if old_element in l:
    index=l.index(old_element)
    l[index]=new_element
    print("Updated list: ",' '.join(l))
else:
    print(f"{old_element} is not in \'{ " ".join(l)} \' ")

#Question 20
nums=list(map(int,input("Enter integer numbers seperated by space to compare: ").split()))
sort_unique=sorted(set(nums), reverse=True)
if len(nums)>=2:
    print(sort_unique[1],"is the 2nd largest number")
else:
    print("There is not 2nd largest number")

#Question 21
nums1=list(map(int,input("Enter integer numbers seperated by space to compare: ").split()))
sort_unique1=sorted(set(nums1), reverse=True)
if len(nums1)>=2:
    print(sort_unique1[-2],"is the 2nd smallest number")
else:
    print("There is not 2nd smallest number")

#Question 22
num=list(map(int,input("Enter integer numbers seperated by space: ").split()))
new_list=list()
for char in num:
    if char%2==0:
        new_list.append(char)
print(f'List contains even numbers is {new_list}')

#Question 23
num1=list(map(int,input("Enter integer numbers seperated by space: ").split()))
new_lis1=list()
for char in num1:
    if char%2!=0:
        new_lis1.append(char)
print(f'List contains odd numbers is {new_lis1}')

#Question 24
l3n=list(map(str,input("Enter elements seperated by space: ").split()))
print(l3n,"has",len(l3n),"characters")

#Question 25
org=list(map(str,input("Enter elements seperated by space: ")))
replica=org
print("".join(replica))

#Question 26
lst = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(lst)
if n % 2 == 1:
    middle_element = lst[n // 2]
    print("Middle element:", middle_element)
else:
    middle_elements = (lst[n // 2 - 1], lst[n // 2])
    print("Middle elements:", middle_elements)
#Question 27
lst = list(map(int, input("Enter numbers separated by space: ").split()))
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
if 0 <= start < len(lst) and 0 < end <= len(lst) and start < end:
    max_element = max(lst[start:end])  
    print("Maximum element in the sublist:", max_element)
else:
    print("Invalid indices. Please enter valid range.")

#Question 28
lst = list(map(int, input("Enter numbers separated by space: ").split()))
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
if 0 <= start < len(lst) and 0 < end <= len(lst) and start < end:
    min_element = min(lst[start:end])  
    print("Maximum element in the sublist:", min_element)
else:
    print("Invalid indices. Please enter valid range.")

#Question 29
lst=list(map(str,input("Enter elements seperated by space: ").split()))
a=int(input("Enter the index that should be removed: "))
if 0<= a< len(lst):
    lst.pop(a)
    print(lst)
else:
    print("Unavailable index")

#Question 30
lst = list(map(int, input("Enter numbers separated by space: ").split()))
is_sorted = lst == sorted(lst)
print("Is the list sorted?", is_sorted)

#Question 31
lst = list(map(str, input("Enter elements separated by space: ").split()))
n = int(input("Enter the number of times to repeat each element: "))
repeated_list = [item for item in lst for _ in range(n)]
print("Repeated list:", repeated_list)

#Question 32
lst=list(map(int,input("Enter integer number seperated by space: ").split()))
lst1=list(map(int,input("Enter integer number seperated by space: ").split()))
print(sorted(lst+lst1))

#Question 33
l1st=list(map(str,input("Enter elements seperated by space: ").split()))
elm=input("Enter element to know indecies: ")
indicies = [i for i, val in enumerate(l1st) if val == elm]
print(indicies)

#Question 34
lst = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter the number of positions to rotate: "))
k = k % len(lst) 
rotated_list = lst[-k:] + lst[:-k]
print("Rotated list:", rotated_list)

#Question 35
start=int(input("Enter integer to start list: "))
end=int(input("Enter integer tp end the list: "))
for num in range(start,end+1):
    if num>0:
     print(num, end=' ')

#Question 36
a=list(map(int,input("Enter negative and positive integers seperated by sapce: ").split()))
l1st=list()
for elm in a:
    if elm>0:
        l1st.append(elm)
print(f"The sum of positive numbers={sum(l1st)}")

#Question 37
a=list(map(int,input("Enter negative and positive integers seperated by sapce: ").split()))
l1st=list()
for elm in a:
    if elm<0:
        l1st.append(elm)
print(f"The sum of negative numbers={sum(l1st)}")

#Question 38
a=list(map(str,input("Enter elements seperated by sapce: ").split()))
if a==a[::-1]:
    print("Yes")
else:
    print("No")

#Question 39
lst = list(map(str, input("Enter elements separated by space: ").split()))
n = int(input("Enter the number of elements per sublist: "))
nested_list = [lst[i:i+n] for i in range(0, len(lst), n)]
print("Nested list:", str(nested_list))

#Question 40
lst = list(map(str, input("Enter elements separated by space: ").split()))
seen = set()
unique_list = []
for item in lst:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)
print("Unique elements in order:", unique_list)
