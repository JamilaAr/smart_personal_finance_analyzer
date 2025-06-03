from datetime import datetime, timedelta
import random

TYPES = ['income', 'expense']
DESCRIPTIONS = ['Groceries', 'Rent', 'Salary', 'Shopping', 'Dining', 'Electricity']

def generate_random_transactions(num=5, start_id=1):
    transactions = []
    for i in range(start_id, start_id + num):
        transaction = {
            'transaction_id': i,
            'customer_id': random.randint(1000, 9999),
            'amount': round(random.uniform(10, 1000), 2),
            'date': datetime.now() - timedelta(days=random.randint(0, 365)),
            'type': random.choice(TYPES),
            'description': random.choice(DESCRIPTIONS)
        }
        transactions.append(transaction)
    return transactions
