# Ex 3 main_hw7.py: Uses generate_report from report.py

from report import generate_report

students = {
    'Lisa': 85,
    'Bart': 72,
    'Homer': 91
}

report = generate_report(students)
print("Final Report:\n" + report)
