def delete_transaction(transactions):
    tid = input("Enter the transaction ID you want to delete: ")
    found = False

    for i, t in enumerate(transactions):
        if str(t['id']) == tid:
            del transactions[i]
            found = True
            print(f" Transaction ID {tid} deleted.")
            break

    if not found:
        print("Transaction not found.")
