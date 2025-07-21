def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = [] 

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ").strip()
            if item:  # Avoid adding empty strings
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to the shopping list.")
            else:
                print("⚠️ Item name cannot be empty.")

        elif choice == '2':
            # Remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"✅ '{item}' has been removed from the shopping list.")
            else:
                print(f"⚠️ '{item}' was not found in the shopping list.")

        elif choice == '3':
            # View the shopping list
            if shopping_list:
                print("\n🛒 Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\n🛒 The shopping list is empty.")

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            # Handle invalid menu choice
            print("⚠️ Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
