numbers = [1, 2, 3, 4, 5]
print(f"Initial List: {numbers}")

while True:
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Quit")
    
    try:
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            try:
                value = int(input("Enter value: "))
                numbers.append(value)
                print(f"Updated List: {numbers}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
        elif choice == 2:
            try:
                value = int(input("Enter value: "))
                index = int(input("Enter index: "))
                if index < 0 or index > len(numbers):
                    print("Index out of range!")
                else:
                    numbers.insert(index, value)
                    print(f"Updated List: {numbers}")
            except ValueError:
                print("Invalid input! Please enter integers.")
        
        elif choice == 3:
            try:
                index = int(input("Enter index to pop: "))
                if index < 0 or index >= len(numbers):
                    print("Index out of range!")
                else:
                    popped_value = numbers.pop(index)
                    print(f"Popped value: {popped_value}")
                    print(f"Updated List: {numbers}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
        elif choice == 4:
            try:
                value = int(input("Enter value to remove: "))
                if value in numbers:
                    numbers.remove(value)
                    print(f"Updated List: {numbers}")
                else:
                    print(f"Value {value} not found in the list!")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
        elif choice == 5:
            print("Exiting program.")
            break
        
        else:
            print("Invalid option! Please choose a valid option.")
    
    except ValueError:
        print("Invalid input! Please enter a number.")
