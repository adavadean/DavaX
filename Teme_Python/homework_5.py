# Ex 1 Check if two words are anagrams

word1 = "listen"
word2 = "silent"

freq1 = {}
freq2 = {}

for char in word1:
    freq1[char] = freq1.get(char, 0) + 1

for char in word2:
    freq2[char] = freq2.get(char, 0) + 1

print("Are they anagrams?", freq1 == freq2)

del freq1['t']
print("Modified freq1:", freq1)
print("Original freq2:", freq2)

# Ex 2 Invert dictionary with duplicate values

grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C"
}

inverted = {}

for name, grade in grades.items():
    if grade not in inverted:
        inverted[grade] = []
    inverted[grade].append(name)

print("Inverted dictionary:", inverted)

# Ex 3 Set analysis for conference attendees

testing = {"Ana", "Bob", "Charlie", "Diana"}
development = {"Charlie", "Eve", "Frank", "Ana"}
devops = {"George", "Ana", "Bob", "Eve"}

all_three = testing & development & devops
print("Attended all sessions:", all_three)

only_testing = testing - (development | devops)
only_development = development - (testing | devops)
only_devops = devops - (testing | development)
only_one = only_testing | only_development | only_devops
print("Attended only one session:", only_one)

subset_check = testing.issubset(devops)
print("All testing attendees also in devops?", subset_check)

all_attendees = sorted(testing | development | devops)
print("All unique attendees (sorted):", all_attendees)

# Copy and clear
dev_copy = development.copy()
development.clear()
print("Cleared development set:", development)
print("Copied development set:", dev_copy)

# Ex 4 Comprehensions

squares = [x ** 2 for x in range(1, 11)]
print("Squares 1–10:", squares)

div7 = {x for x in range(1, 51) if x % 7 == 0}
print("Divisible by 7 (1–50):", div7)

score = {"Alice": 85, "Bob": 59, "Charlie": 92}
passed = {name: grade for name, grade in score.items() if grade >= 60}
print("Students who passed:", passed)

# Nested dict comprehension: attendance log
students = ["Michael", "David", "Liza"]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

attendance = {
    name: {day: (day in ["Mon", "Wed"]) for day in weekdays}
    for name in students
}

print("Weekly attendance:")
for student, days in attendance.items():
    print(student, "->", days)
