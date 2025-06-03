import csv

def save_transactions(transactions, filename='financial_transactions.csv'):
    """Save transactions to a CSV file."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['transaction_id', 'customer_id', 'amount', 'date', 'type', 'description'])
            writer.writeheader()
            for t in transactions:
                writer.writerow({
                    'transaction_id': t['transaction_id'],
                    'customer_id': t['customer_id'],
                    'amount': t['amount'],
                    'date': t['date'].strftime('%Y-%m-%d'),
                    'type': t['type'],
                    'description': t['description']
                })
        print(f"Transactions saved to {filename}")
    except Exception as e:
        print("Error saving transactions:", e)