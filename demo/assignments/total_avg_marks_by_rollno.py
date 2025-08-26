data = [ (1, 90), (2, 56), (1, 85), (1,88), (2, 69), (3, 50), (4, 45), (4, 90)]

students = {}

for rollno, marks in data:
    entry = students.get(rollno, (0, 0))
    students[rollno] =  (entry[0] + marks, entry[1] + 1)

for rollno, details in students.items():
    total , count = details  # unpack tuple
    print(f"{rollno:3}  {total:3} {total / count:6.2f}")




