#Question 1
my_dict = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
key = 'profession'
try:
    value = my_dict[key]
except KeyError:
    value = 'Key not found'
print(value)  

#Question 2
my_dict = {"name": "Alice", "age": 25}
if "name" in my_dict:
    print("Key exists")
else:
    print("Key does not exist")

#Question 3
my_dict = {"name": "Alice", "age": 25, "gender": "Female"}
key_count = len(my_dict)
print(key_count) 

#Question 4
my_dict = {"name": "Alice", "age": 25, "gender": "Female"}
keys_list = list(my_dict.keys())
print(keys_list)  

#Question 5
my_dict = {"name": "Alice", "age": 25, "gender": "Female"}
values_list = list(my_dict.values())
print(values_list) 

#Question 6
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

#Question 7
my_dict = {"name": "Alice", "age": 25, "gender": "Female"}
if "age" in my_dict:
    del my_dict["age"]
print(my_dict)  

#Question 8
empty_dict = {}
print(empty_dict)  

#Question 9
if len(my_dict) == 0:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")

#Question 10
my_dict = {"name": "Alice", "age": 25, "gender": "Female"}
key = "age"
value = my_dict.get(key)
if value is not None:
    print(f"Key-Value pair: {key}: {value}")
else:
    print("Key not found.")

#Question 11
my_dict = {"name": "Alice", "age": 25, "gender": "Female"}
my_dict["age"] = 26
print(my_dict)  

#Question 12
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}
value_to_count = 1
count = sum(1 for v in my_dict.values() if v == value_to_count)
print(count)  

#Question 13
my_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in my_dict.items()}
print(inverted_dict)  

#Question 14
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}
target_value = 1
keys_with_value = [k for k, v in my_dict.items() if v == target_value]
print(keys_with_value)  

#Question 15
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)

#Question 16
my_dict = {
    "name": "Alice",
    "details": {"age": 25, "city": "New York"},
    "hobby": "Reading"
}
has_nested = any(isinstance(v, dict) for v in my_dict.values())
print(has_nested)

#Question 17
my_dict = {
    "name": "Alice",
    "details": {
        "age": 25,
        "city": "New York"
    }
}
age = my_dict["details"]["age"]
print(age)

#Question 18
from collections import defaultdict
my_dict = defaultdict(int)
print(my_dict["missing_key"])  # Output: 0

#Question 19
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
unique_count = len(set(my_dict.values()))
print(unique_count)  

#Question 20
my_dict = {"b": 2, "a": 3, "d": 1, "c": 4}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)

#Question 21
my_dict = {"a": 3, "b": 2, "c": 4, "d": 1}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)

#Question 22
filtered_dict = dict(filter(lambda item: item[1] > 8, my_dict.items()))
print(filtered_dict)

#Question 23
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common = any(key in dict2 for key in dict1)
print(common) 

#Question 24
tuple_of_pairs = (("a", 1), ("b", 2), ("c", 3))
my_dict = dict(tuple_of_pairs)
print(my_dict)

#Question 25
my_dict = {"a": 1, "b": 2, "c": 3}
first_key, first_value = next(iter(my_dict.items()))
print(first_key, first_value)
