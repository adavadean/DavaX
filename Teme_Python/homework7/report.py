# Ex 3  report.py: Generates a report of students who scored >= 80

def generate_report(data: dict) -> str:
    passed = {name: score for name, score in data.items() if score >= 80}
    sorted_items = sorted(passed.items(), key=lambda x: x[1], reverse=True)
    lines = [f"{name}: {score}" for name, score in sorted_items]
    return "\n".join(lines)
