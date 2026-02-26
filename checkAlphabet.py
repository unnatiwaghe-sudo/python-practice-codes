text = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase = 0

for char in text:
    if char in "aeiouAEIOU":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char == " ":
        spaces += 1
    
    if char.islower():
        lowercase += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)
