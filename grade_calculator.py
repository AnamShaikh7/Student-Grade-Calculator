
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter your name: ")

subjects = ["Python", "Mathematics", "English", "Science", "Computer"]

total_marks = 0

for subject in subjects:
    marks = float(input(f"Enter marks for {subject} (out of 100): "))

    total_marks += marks

percentage = total_marks / len(subjects)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("==============================")
