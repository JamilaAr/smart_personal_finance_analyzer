from datetime import datetime
from transactions.utils import generate_new_id

def add_transaction(transactions):
    try:
        date_input = input("Enter date (YYYY-MM-DD): ")
        date = datetime.strptime(date_input, "%Y-%m-%d")
        customer_id = int(input("Enter customer ID: "))
        amount = float(input("Enter amount: "))
        t_type = input("Enter type (credit/debit/transfer): ").strip().lower()
        if t_type not in ['credit', 'debit', 'transfer']:
            print("Invalid transaction type!")
            return
        description = input("Enter description: ")

        if t_type == 'debit':
            amount = -abs(amount)

        transaction = {
            'transaction_id': generate_new_id(transactions),
            'date': date,
            'customer_id': customer_id,
            'amount': amount,
            'type': t_type,
            'description': description
        }
        transactions.append(transaction)
        print("Transaction added!")

    except ValueError:
        print("Invalid input. Please check your values.")
