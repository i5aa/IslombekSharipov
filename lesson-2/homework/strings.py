#Question 1
from datetime import datetime
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = datetime.now().year
age = current_year - year_of_birth
print(f"Hello {name}, you are {age} years old.")

#Question 2
txt = "LMaasleitbtui"
car1 = txt[::2]
car2= txt[1::2]
print(f"These cars are {car1} and {car2}")

#Question 3
word=str(input("Word: "))
print(f" {word} is {len(word)} characters-long")
print(word.upper())
print(word.lower())

#Question 4
p=str(input("Word: "))
if p==p[::-1]:
    print(f"{p} is palindrom word")
else:
    print(f"{p} is not palindrome word")

#QUestion 5
text = input("Enter a string: ").lower()
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char in consonants)
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")

#Question 6
txt=str(input("Word: ")).lower()
ck=str(input("To check: ")).lower()
if ck in txt:
    print("Yes, contains")
else:
    print("No, doesn't contain")

#Question 7
m=str(input("Sentence: "))
v=str(input("What word to replace: "))
re=str(input("With word: "))
print(m.replace(v,re))

#Question 8 
t=str(input("Word: "))
print(f'First character is {t[0]} and last character is {t[-1]}')

#Question 9
ask=str(input("Word: "))
print(ask[::-1])

#Question 10
q=str(input("Sentence: "))
print(f"This sentence contains {len(q.split())} words")

#Question 11
d=str(input("Any string: "))
if any(char.isdigit() for char in d):
    print("The sentence contains digits.")
else:
    print("The sentence does not contain any digits.")

#Question 12
words = input("Enter a list of words separated by spaces: ").split()
separator = input("Enter a separator character (e.g., - or ,): ")
joined_string = separator.join(words)
print("Joined string:", joined_string)

#Question 13
sent=input("Sentence: ")
print(sent.replace(" ",""))

#Question 14
h,j=map(str,input("2 strings: ").split())
if h==j:
    print('Yes')
else:
    print("No")

#Question 15
sen=input("Sentence:").split()
print((''.join(word[0].upper() for word in sen)))

#Question 16
wrd=input("Word: ")
char=input("What character: ")
if char in wrd:
    print(wrd.replace(char,""))
else:
    print(f"There is not {char} in {wrd}")

#Question 17
sentence = input("Enter a string: ")
symbol = input("Enter a symbol to replace vowels: ")
vowels = "aeiouAEIOU"
replaced_sentence = ''.join(symbol if char in vowels else char for char in sentence)
print("Modified string:", replaced_sentence)

#Question 18
sentence=str(input("Sentence: ")).split()
print(f"Starts with {sentence[0]} \nEnds with {sentence[-1]}")