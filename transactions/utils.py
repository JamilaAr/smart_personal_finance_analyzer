from datetime import datetime

def format_date(date_obj):
    return date_obj.strftime('%Y-%m-%d')


def generate_new_id(transactions):
    if not transactions:
        return 1
    existing_ids = [t['transaction_id'] for t in transactions]
    return max(existing_ids) + 1


def log_error(message, file_path="data/errors.txt"):
    with open(file_path, "a") as f:
        f.write(message + "\n")


