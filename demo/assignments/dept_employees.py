data = [ ('IT', 'George'), ('IT', 'Kevin'), ('HR', 'Cathy'), ('IT', 'Belinda'),
         ('PR', 'Dan'), ('HR', 'Dave')]
depts = {}

for  dept, employee in data:
     employees = depts.get(dept, [])
     employees.append(employee)
     depts[dept] = employees

for dept, employees in depts.items():
    print(dept, ",".join(employees))

