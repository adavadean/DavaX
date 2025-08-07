# Ex 1 Custom calculator function with optional operation and error handling

def calculate(*numbers, operation='+'):
    if not numbers:
        return 0
    try:
        result = numbers[0]
        for num in numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/':
                if num == 0:
                    raise ZeroDivisionError("Division by zero.")
                result /= num
            else:
                raise ValueError(f"Invalid operation: {operation}")
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# Test calls
print(calculate(2, 3, 4, operation='*'))
print(calculate(10, 0, operation='/'))
print(calculate(operation='-'))


# Ex 2 Sort students by score using lambda, filter scores >= 80

names = ["Lucas", "Nataly", "Megi", "Maria", "Steven"]
scores = [85, 92, 78, 81, 67]

students = list(zip(names, scores))
filtered = list(filter(lambda s: s[1] >= 80, students))
sorted_students = sorted(filtered, key=lambda s: s[1], reverse=True)

for name, score in sorted_students:
    print(f"{name}: {score}")


# Ex 3 Validate age input and handle exceptions

def check_age(age_input):
    try:
        if age_input == "":
            raise ValueError("Input is empty.")
        age = int(age_input)
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
        print(f"Valid age: {age}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"Unknown error: {e}")
    finally:
        print("Validation complete.")

# Test calls 
check_age("25")
check_age("abc")
check_age("")
check_age("-5")
check_age("140")
