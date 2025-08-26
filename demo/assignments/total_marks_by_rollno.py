
data = [ (1, 90), (2, 56), (1,88), (2, 69), (3, 50), (4, 45), (4, 90)]

students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks

print(students)



