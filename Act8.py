print("Simple Calculator")
print("------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1 - Addition (+)")
print("2 - Subtraction (-)")
print("3 - Multiplication (*)")
print("4 - Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation
if choice == "1":
    answer = num1 + num2
    print("Result:", answer)

elif choice == "2":
    answer = num1 - num2
    print("Result:", answer)

elif choice == "3":
    answer = num1 * num2
    print("Result:", answer)

elif choice == "4":
    if num2 != 0:
        answer = num1 / num2
        print("Result:", answer)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid choice")