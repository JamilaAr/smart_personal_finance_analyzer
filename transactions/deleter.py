from transactions.utils import format_date

def delete_transaction(transactions):
    for idx, t in enumerate(transactions, 1):
        print(f"{idx}. {format_date(t['date'])} | {t['customer_id']} | {t['amount']} | {t['type']} | {t['description']}")
    try:
        choice = int(input("Select transaction number to delete: ")) - 1
        if 0 <= choice < len(transactions):
            confirm = input("Are you sure you want to delete this transaction? (y/n): ")
            if confirm.lower() == 'y':
                transactions.pop(choice)
                print("Transaction deleted.")
    except Exception as e:
        print(f"Error deleting transaction: {e}")
