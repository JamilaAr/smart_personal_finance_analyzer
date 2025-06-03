import csv
from datetime import datetime

def load_transactions(filename='data/financial_transactions.csv'):
    transactions = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    date = datetime.strptime(row['date'], '%Y-%m-%d')
                    amount = float(row['amount'])
                    if row['type'] == 'debit':
                        amount = -amount
                    transaction = {
                        'transaction_id': int(row['transaction_id']),
                        'date': date,
                        'customer_id': int(row['customer_id']),
                        'amount': amount,
                        'type': row['type'],
                        'description': row['description']
                    }
                    transactions.append(transaction)
                except Exception as e:
                    print(f"Skipping row due to error: {e} -> {row}")
    except FileNotFoundError:
        print("File not found: " + filename)
    return transactions
