from collections import defaultdict


def category_summary(expenses):
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount
    return summary

def generate_monthly_report(expenses, month):
    total = 0
    report_lines = []

    for exp in expenses:
        if exp.date.startswith(month):
            total += exp.amount
            report_lines.append(str(exp))

    return total, report_lines
