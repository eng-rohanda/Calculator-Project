def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Choose: ")

    if choice == "5":
        break

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == "1":
        print(add(num1, num2))
    elif choice == "2":
        print(subtract(num1, num2))
    elif choice == "3":
        print(multiply(num1, num2))
    elif choice == "4":
        print(divide(num1, num2))