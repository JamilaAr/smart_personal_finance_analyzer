def filter_by_year(transactions, year):
    """
    Filter transactions dict/list by given year.
    """
    filtered = [t for t in transactions if t['date'].year == year]
    return filtered
