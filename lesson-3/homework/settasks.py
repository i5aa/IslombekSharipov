#Question 1
set1 = set(input("Enter elements of first set (space-separated): ").split())
set2 = set(input("Enter elements of second set (space-separated): ").split())
union_set = set1.union(set2)
print("Union of sets:", union_set)

#Question 2
set1 = set(input("Enter elements of first set (space-separated): ").split())
set2 = set(input("Enter elements of second set (space-separated): ").split())
intersection_set = set1 & set2  
print("Intersection of sets:", intersection_set)

#Question 3
set1 = set(input("Enter elements of first set (space-separated): ").split())
set2 = set(input("Enter elements of second set (space-separated): ").split())
difference_set = set1 - set2  
print("Difference of sets:", difference_set)

#Question 4
set1 = set(input("Enter elements of first set (space-separated): ").split())
set2 = set(input("Enter elements of second set (space-separated): ").split())
if set1 <= set2:  
    print("The first set is a subset of the second set.")
else:
    print("The first set is NOT a subset of the second set.")

#Question 5
my_set = set(input("Enter elements of the set (space-separated): ").split())
element = input("Enter the element to check: ")
if element in my_set:
    print(f"'{element}' exists in the set.")
else:
    print(f"'{element}' does NOT exist in the set.")

#Question 6
my_set = set(input("Enter elements of the set (space-separated): ").split())
set_length = len(my_set)
print("Number of unique elements in the set:", set_length)

#Question 7
my_list = input("Enter elements of the list (space-separated): ").split()
my_set = set(my_list)
print("Set with unique elements:", my_set)

#Question 8
my_set = set(input("Enter elements of the set (space-separated): ").split())
element = input("Enter the element to remove: ")
if element in my_set:
    my_set.remove(element)
    print(f"'{element}' has been removed.")
else:
    print(f"'{element}' is not in the set.")
print("Updated set:", my_set)

#Question 9
my_set = set(input("Enter elements of the set (space-separated): ").split())
my_set.clear()
print("The set after clearing:", my_set)

#Question 10
my_set = set(input("Enter elements of the set (space-separated): ").split())
if len(my_set) == 0:
    print("The set is empty.")
else:
    print("The set is not empty.")

#Question 11
set1 = set(input("Enter elements of the first set (space-separated): ").split())
set2 = set(input("Enter elements of the second set (space-separated): ").split())
symmetric_diff = set1 ^ set2  
print("Symmetric difference:", symmetric_diff)

#Question 12
my_set = set(input("Enter elements of the set (space-separated): ").split())
element = input("Enter the element to add: ")
my_set.add(element)
print("Updated set:", my_set)

#Question 13
my_set = set(input("Enter elements of the set (space-separated): ").split())
popped_element = my_set.pop()
print(f"Popped element: {popped_element}")
print("Updated set:", my_set)

#Question 14
my_set = set(map(int, input("Enter numbers for the set (space-separated): ").split()))
max_element = max(my_set)
print("The maximum element in the set is:", max_element)

#Question 15
my_set = set(map(int, input("Enter numbers for the set (space-separated): ").split()))
max_element = min(my_set)
print("The minimum element in the set is:", max_element)

#Question 16
my_set = set(map(int, input("Enter integers for the set (space-separated): ").split()))
even_set = {num for num in my_set if num % 2 == 0}
print("Set with only even numbers:", even_set)

#Question 17
my_set = set(map(int, input("Enter integers for the set (space-separated): ").split()))
odd_set = {num for num in my_set if num % 2 != 0}
print("Set with only odd numbers:", odd_set)

#Question 18
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
my_set = set(range(start, end + 1))
print("Set of numbers in the range:", my_set)

#Question 19
set1_input = input("Enter elements for set 1, separated by commas: ").split(',')
set2_input = input("Enter elements for set 2, separated by commas: ").split(',')
set1 = set(set1_input)
set2 = set(set2_input)
merged_set = set1.union(set2)
print("Merged set without duplicates:", merged_set)

#Question 20
set1_input = input("Enter elements for set 1, separated by commas: ").split(',')
set2_input = input("Enter elements for set 2, separated by commas: ").split(',')
set1 = set(set1_input)
set2 = set(set2_input)
if set1.isdisjoint(set2):
    print("The sets are disjoint (no common elements).")
else:
    print("The sets are not disjoint (they have common elements).")

#Question 21
input_list = input("Enter elements for the list, separated by commas: ").split(',')
unique_list = list(set(input_list))
print("List after removing duplicates:", unique_list)

#Question 22
input_list = input("Enter elements for the list, separated by commas: ").split(',')
unique_elements = set(input_list)
count_unique = len(unique_elements)
print("The count of unique elements is:", count_unique)

#Question 23
import random
n = int(input("Enter the number of elements: "))
rs = int(input("Enter the start of the range: "))
re = int(input("Enter the end of the range: "))
r_s = set(random.sample(range(rs, re + 1), n))
print("Generated random set:", r_s)
