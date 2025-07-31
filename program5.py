print("Panneer international [p] ltd")
print("no 5,villupuram dist,Tamilnadu")
print("-----------------------")
print("Employee payroll system")
print("-----------------------")
eid=int(input("Enter the employee id:"))
name=input("Enter the employee name:")
salary=int(input("Enter the salary:"))
print("Income:")
bonus=salary*20/100
print("Bonus(20%):",bonus)
ot=salary*10/100
print("Overtime(10%):",ot)
ta=salary*5/100
print("Travel allowance(5 percentage):",ta)
gross=salary+bonus+ot+ta
print("Gross pay in rupees:",gross)
