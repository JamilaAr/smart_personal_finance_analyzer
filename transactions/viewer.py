def view_transactions(transactions):
    print("\n View Options:")
    print("1. View all transactions")
    print("2. Filter by type")
    print("3. View a limited number")

    choice = input("Choose how to view transactions (1/2/3): ")

    if choice == '1':
        for t in transactions:
            print(t)

    elif choice == '2':
        t_type = input("Enter type to filter: ").lower()
        filtered = [t for t in transactions if t['type'].lower() == t_type]
        if filtered:
            for t in filtered:
                print(t)
        else:
            print("No transactions found with that type.")

    elif choice == '3':
        limit = int(input("How many transactions would you like to view? "))
        for t in transactions[:limit]:
            print(t)

    else:
        print("Invalid option.")
