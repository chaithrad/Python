try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator
   # print("Result:", result)
except ValueError:
        print("Error: Please enter valid numbers.")
except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
else:
    print("Division successful.", result)
finally:
    print("Operation complete.")