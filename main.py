
name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

result = f"{name} scored {marks} and received grade {grade}"

with open("grades.txt", "a") as f:
    f.write(result + "\n")

print(result)
