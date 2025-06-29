def update_transaction(transactions):
    tid = input("Enter the transaction ID you want to update: ")

    for t in transactions:
        if str(t['id']) == tid:
            print(f"Current transaction: {t}")
            new_amount = input(f"Enter new amount (leave blank to keep {t['amount']}): ")
            new_type = input(f"Enter new type (leave blank to keep {t['type']}): ")

            if new_amount:
                t['amount'] = new_amount
            if new_type:
                t['type'] = new_type

            print("✅ Transaction updated.")
            return

    print("Transaction not found.")
