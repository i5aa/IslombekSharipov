#Question 1
tpl = tuple(map(str, input("Enter elements separated by space: ").split()))
element = input("Enter the element to count: ")
count = tpl.count(element)
print(f"The element '{element}' appears {count} times in the tuple.")

#Question 2
tpl = tuple(map(int, input("Enter numbers separated by space: ").split()))
max_element = max(tpl)
print("The largest element in the tuple is:", max_element)

#Question 3
tpl = tuple(map(int, input("Enter numbers separated by space: ").split()))
max_element = min(tpl)
print("The largest element in the tuple is:", max_element)

#Question 4
tpl = tuple(input("Enter elements separated by space: ").split())
element = input("Enter the element to check: ")
if element in tpl:
    print(f"The element '{element}' is present in the tuple.")
else:
    print(f"The element '{element}' is NOT present in the tuple.")

#Question 5
tpl = tuple(input("Enter elements separated by space: ").split())
if tpl:
    print("The first element is:", tpl[0])
else:
    print("The tuple is empty. No first element.")

#Question 6
tpl = tuple(input("Enter elements separated by space: ").split())
if tpl:
    print("The first element is:", tpl[-1])
else:
    print("The tuple is empty. No first element.")

#Question 7
tpl = tuple(input("Enter elements separated by space: ").split())
length = len(tpl)
print("The number of elements in the tuple is:", length)

#Question 8
tpl = tuple(input("Enter elements separated by space: ").split())
sliced_tpl = tpl[0:3]  
print("The sliced tuple (first 3 elements) is:", sliced_tpl)

#Question 9
tpl1 = tuple(input("Enter elements for first tuple separated by space: ").split())
tpl2 = tuple(input("Enter elements for second tuple separated by space: ").split())
combined_tuple = tpl1 + tpl2
print("The concatenated tuple is:", combined_tuple)

#Question 10
tpl = tuple(input("Enter elements separated by space: ").split())
if tpl:
    print("The tuple is NOT empty. It contains elements:", tpl)
else:
    print("The tuple is empty.")

#Question 11
tpl = tuple(input("Enter elements separated by space: ").split())
element = input("Enter the element to find indices for: ")
indices = [index for index, value in enumerate(tpl) if value == element]
if indices:
    print(f"The element '{element}' is found at indices:", indices)
else:
    print(f"The element '{element}' is not found in the tuple.")

#Question 12
tpl = tuple(map(int, input("Enter numbers separated by space: ").split()))
unique_numbers = list(set(tpl))  
if len(unique_numbers) < 2:
    print("There is no second largest element.")
else:
    unique_numbers.sort(reverse=True)  
    print("The second largest element is:", unique_numbers[1])

#Question 13
tpl = tuple(map(int, input("Enter numbers separated by space: ").split()))
unique_numbers = list(set(tpl))
if len(unique_numbers) < 2:
    print("There is no second largest element.")
else:
    unique_numbers.sort() 
    print("The second smallest element is:", unique_numbers[1])

#Question 14
element = input("Enter the element to create a tuple: ")
single_element_tuple = (element)
print("The single element tuple is:", single_element_tuple)

#Question 15
lst = list(input("Enter elements separated by space: ").split())
tpl = tuple(lst)
print("The tuple is:", tpl)

#Question 16
tpl = tuple(input("Enter elements separated by space: ").split())
if tpl == tuple(sorted(tpl)):
    print("The tuple is sorted in ascending order.")
else:
    print("The tuple is NOT sorted in ascending order.")

#Question 17
a = tuple(map(int, input("Enter tuple including integers: ").split()))
start = int(input("Enter the starting index of subtuple: "))
end = int(input("Enter the ending index of subtuple: "))
if 0 <= start < end and (end + 1) - start > 0:
    subtuple = a[start:end+1] 
    largest = max(subtuple) 
    print("Largest element in the subtuple:", largest)
else:
    print("Invalid indices")

#Question 18
a = tuple(map(int, input("Enter tuple including integers: ").split()))
start = int(input("Enter the starting index of subtuple: "))
end = int(input("Enter the ending index of subtuple: "))
if 0 <= start < end and (end + 1) - start > 0:
    subtuple = a[start:end+1] 
    smallest = min(subtuple) 
    print("Smallest element in the subtuple:", smallest)
else:
    print("Invalid indices")

#Question 19
a = tuple(map(int, input("Enter tuple including integers: ").split()))
element = int(input("Enter the element to remove: "))
a_list = list(a)
if element in a_list:
    a_list.remove(element)
new_tuple = tuple(a_list)
print("New tuple after removing the element:", new_tuple)

#Question 20
a = tuple(map(int, input("Enter tuple including integers: ").split()))
n = int(input("Enter the number of elements in each subtuple: "))
nested_tuple = tuple(tuple(a[i:i+n]) for i in range(0, len(a), n))
print("Nested Tuple:", nested_tuple)

#Question 21
a = tuple(input("Enter tuple including elements (space-separated): ").split())
n = int(input("Enter the number of times to repeat each element: "))
repeated_tuple = tuple(item for item in a for _ in range(n))
print("New tuple with repeated elements:", repeated_tuple)

#Question 22
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
range_tuple = tuple(range(start, end + 1))
print("Tuple with numbers in the specified range:", range_tuple)

#Question 23
a = tuple(input("Enter tuple elements (space-separated): ").split())
reversed_tuple = a[::-1]
print("Reversed tuple:", reversed_tuple)

#Question 24
a = tuple(input("Enter tuple elements (space-separated): ").split())
if a == a[::-1]:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")

#Question 25
a = tuple(input("Enter tuple elements (space-separated): ").split())
seen = set()
unique_tuple = tuple(item for item in a if item not in seen and not seen.add(item))
print("Tuple with unique elements:", unique_tuple)
