# Name: Diana C. Esguerra
# Section: IV - BSIT - B
# Activity: P4 - Exception Handling
# Date: November 23, 2026

# Divide two numbers
def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero!")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed.")

# Open and read a file
def open_file():
    try:
        filename = input("Enter filename: ")

        with open(filename, "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found!")

    finally:
        print("File operation completed.")

# Display the menu
def show_menu():
    print("\n===== EXCEPTION HANDLING =====")
    print("[1] Divide Numbers")
    print("[2] Open File")
    print("[3] Exit")

# Main program
def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                divide_numbers()

            elif choice == 2:
                open_file()

            elif choice == 3:
                print("Thank you!")
                break

            else:
                print("Invalid choice! Please select 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()

