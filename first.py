students = []
n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])
#print(students)
grades = sorted(set(student[1] for student in students))

print(grades)
second_lowest = grades[1]


result = sorted(
    student[0] for student in students if student[1] == second_lowest
)


for name in result:
    print(name)