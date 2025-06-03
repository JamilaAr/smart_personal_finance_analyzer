from transactions.utils import format_date

def view_transactions(transactions):
    print("\nID | Date         | Customer | Amount    | Type     | Description")
    print("---------------------------------------------------------------")
    for t in transactions:
        print(f"{t['transaction_id']:>2} | {format_date(t['date']):<12} | {t['customer_id']:^8} | {t['amount']:>8.2f} | {t['type']:<8} | {t['description'][:30]}")
