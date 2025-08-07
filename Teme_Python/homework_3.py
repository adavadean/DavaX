# Ex 1 Working with lists

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
middle_index = len(numbers) // 2
print("Middle element:", numbers[middle_index])
numbers.append(60)
numbers.insert(1, 15)
numbers.pop()
print("Length of list:", len(numbers))
numbers.sort()
print("Sorted list:", numbers)

# Ex 2  Replace a word in a sentence

sentence = "Python is fun because Python is powerful"
target_word = "Python"
new_word = "Programming"

words = sentence.split()
for i in range(len(words)):
    if words[i] == target_word:
        words[i] = new_word

new_sentence = ' '.join(words)
print("Modified sentence:", new_sentence)

# Ex 3 Palindrome checker using slicing

word = input("Enter a word: ")
if word == word[::-1]:
    print("It is.")
else:
    print("It is not.")

# Ex 4  f-string formatting

name = "Alice"
age = 30
balance = 1234.56789
membership_date = "2023-08-12"
status = True

print(f"User: {name}, Age: {age}")
print(f"Balance: ${balance:10.2f}")
print(f"Member since: {membership_date}")
print(f"Active member: {'Yes' if status else 'No'}")
