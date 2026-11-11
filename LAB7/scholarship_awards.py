
import math

def parse_applicant(text):
    if not isinstance(text, str) or ':' not in text:
        return None

    parts = text.split(':')
    if len(parts) != 2:
        return None

    category, marks = parts

    if not category.strip() or not marks.strip():
        return None

    try:
        marks = float(marks)
        if not math.isfinite(marks):
            return None
    except ValueError:
        return None

    return category.strip().title(), marks

def marks_average(marks_csv):
    if not isinstance(marks_csv, str) or not marks_csv.strip():
        return None

    try:
        values = [int(r.strip()) for r in marks_csv.split(',')]

        if not values:
            return None

        return sum(values) // len(values)

    except ValueError:
        return None

def payable_award(text):
    if not isinstance(text, str) or '|' not in text:
        return None

    parts = text.split('|')
    if len(parts) != 2:
        return None

    award, deduction = parts

    if not award.strip() or not deduction.strip():
        return None

    try:
        award = float(award)
        deduction = float(deduction)

        if not math.isfinite(award) or not math.isfinite(deduction):
            return None

        total = award * 1.18 - deduction
        return max(total, 0)

    except ValueError:
        return None


def main():
    print("==== Running parse_applicant ====")
    user_input = input("Enter category:marks (e.g. merit:82): ")
    result = parse_applicant(user_input)
    print("Category and Marks:", result)

    print("\n==== Running marks_average ====")
    user_input = input("Enter marks as CSV (e.g. 72,85,90): ")
    result = marks_average(user_input)
    print("Average Marks:", result)

    print("\n==== Running payable_award ====")
    user_input = input("Enter award|deduction (e.g. 5000|500): ")
    result = payable_award(user_input)
    print("Payable Award:", result)

if __name__ == "__main__":
    main()