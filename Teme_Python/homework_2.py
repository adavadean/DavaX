# Ex 1 Immutable Data Types
a = 10
print("Original id of a:", id(a))
a += 1
print("New id of a:", id(a))


b = 3.14
print("Original id of b:", id(b))
b *= 2
print("New id of b:", id(b))

#Ex 2 Leap Year Checker
year = input("Enter the year: ")

year = int(year)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")

#Ex 3 Ternary Conditional Operator
num = -5
print("Positive" if num > 0 else "Negative")

#Ex 4  Boolean Logic Practice
x = 5
y = 0
z = -3

print("All > 0:", x > 0 and y > 0 and z > 0)

print("At least one == 0:", x == 0 or y == 0 or z == 0)

print("None are negative:", not (x < 0 or y < 0 or z < 0))

#Ex 5 Type Conversion and Identity
x = 100
y = -30
z = 0

print("float(x):", float(x))
print("bool(y):", bool(y))
print("bool(z):", bool(z))  

a = 100
b = int("100")
print("a == b:", a == b)      
print("a is b:", a is b)        

print("Id of a:", id(a))
print("Id of b:", id(b))
