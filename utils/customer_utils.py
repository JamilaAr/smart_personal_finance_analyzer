def unique_customer_ids(transactions):
    """
    Return a set of unique customer IDs from transactions.
    """
    return set(t['customer_id'] for t in transactions)
