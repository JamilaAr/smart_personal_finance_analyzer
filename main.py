from transactions.loader import load_transactions
from transactions.viewer import view_transactions
from transactions.adder import add_transaction
from transactions.updater import update_transaction
from transactions.deleter import delete_transaction
from transactions.saver import save_transactions

from utils.filter_transactions import filter_by_year
from utils.customer_utils import unique_customer_ids
from utils.random_transactions import generate_random_transactions
from transactions.reporter import generate_report


def main():
    transactions = load_transactions()
    
    while True:
        print("\nMenu:")
        print("1. View Transactions")
        print("2. Add Transaction")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Filter Transactions by Year")
        print("6. Get Unique Customer IDs")
        print("7. Generate Random Transactions")
        print("8. Save Transactions to CSV")
        print("9. Generate Financial Report")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_transactions(transactions)
        elif choice == '2':
            add_transaction(transactions)
        elif choice == '3':
            update_transaction(transactions)
        elif choice == '4':
            delete_transaction(transactions)
        elif choice == '5':
            year = int(input("Enter year to filter transactions by: "))
            filtered = filter_by_year(transactions, year)
            view_transactions(filtered)
        elif choice == '6':
            unique_ids = unique_customer_ids(transactions)
            print(f"Unique customer IDs: {unique_ids}")
        elif choice == '7':
            num = int(input("How many random transactions to generate? "))
            new_transactions = generate_random_transactions(num, start_id=len(transactions) + 1)
            transactions.extend(new_transactions)
            print(f"Generated {num} random transactions.")
        elif choice == '8':
            save_transactions(transactions)
            print("Transactions saved to financial_transactions.csv.")
        elif choice == '9':
            generate_report(transactions)
            print("Report saved to report.txt.")
        elif choice == '10':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1-10.")


if __name__ == '__main__':
    main()
