from transactions.utils import format_date
from datetime import datetime

def update_transaction(transactions):
    for idx, t in enumerate(transactions, 1):
        print(f"{idx}. {format_date(t['date'])} | {t['customer_id']} | {t['amount']} | {t['type']} | {t['description']}")
    try:
        choice = int(input("Select transaction number to update: ")) - 1
        if 0 <= choice < len(transactions):
            field = input("Which field to update? (date, amount, type, description): ").lower()
            new_value = input("Enter new value: ")

            if field == 'date':
                transactions[choice]['date'] = datetime.strptime(new_value, "%Y-%m-%d")
            elif field == 'amount':
                transactions[choice]['amount'] = float(new_value)
            elif field == 'type':
                if new_value not in ['credit', 'debit', 'transfer']:
                    print("Invalid type.")
                    return
                transactions[choice]['type'] = new_value
            elif field == 'description':
                transactions[choice]['description'] = new_value
            else:
                print("Invalid field.")
                return
            print("Transaction updated!")
    except Exception as e:
        print(f"Error updating transaction: {e}")
