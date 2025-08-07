# Ex 1  Currency conversion with unpacking and f-strings

data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]

for amount, currency, target_currency, exchange_rate in data:
    converted = amount * exchange_rate
    print(f"{amount} {currency} = {converted:.2f} {target_currency}")


# Ex 2  Sum of odd numbers from 1 to 100

total = 0
for number in range(1, 101, 2): 
    total += number

print("Sum of odd numbers:", total)

# Ex 3 Number guessing game (while loop)

secret_number = 7
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret_number:
        print("Correct!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong. Try again. Attempts left: {attempts}")
        else:
            print("You've run out of attempts. The number was 7.")

# Ex 4  Enumerate list items with index and length

fruits = ['apple', 'banana', 'cherry', 'date']

for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}: {fruit} ({len(fruit)} letters)")

# Ex 5  Mutate nested list data and find max difference

data = [
    ['2021-01-01', 20, 10],
    ['2021-01-02', 20, 18],
    ['2021-01-03', 10, 10],
    ['2021-01-04', 102, 100],
    ['2021-01-05', 45, 25]
]

max_diff = None
max_date = ""

for row in data:
    stop = row[1]
    start = row[2]
    diff = stop - start
    row.insert(1, diff)

    if max_diff is None or diff > max_diff:
        max_diff = diff
        max_date = row[0]

print("Date with the largest difference:", max_date)
