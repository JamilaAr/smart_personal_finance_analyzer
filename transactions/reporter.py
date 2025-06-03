def generate_report(transactions, filename='report.txt'):
    """Generate a text report of financial summaries."""
    total_income = 0
    total_expense = 0
    type_totals = {}

    for t in transactions:
        t_type = t['type'].lower()
        amount = t['amount']

        if t_type == 'income':
            total_income += amount
        elif t_type == 'expense':
            total_expense += amount

        # Track each type
        if t_type in type_totals:
            type_totals[t_type] += amount
        else:
            type_totals[t_type] = amount

    net_balance = total_income - total_expense

    with open(filename, 'w') as file:
        file.write("Financial Summary\n")
        file.write(f"Total Income : ${total_income:,.2f}\n")
        file.write(f"Total Expense: ${total_expense:,.2f}\n")
        file.write(f"Net Balance  : ${net_balance:,.2f}\n\n")

        file.write("By Type:\n")
        for t_type, total in type_totals.items():
            file.write(f"  {t_type.capitalize():<10}: ${total:,.2f}\n")
