#write a progarm that take a salary as input using a conditional statement calculate the final tax rate based on these rules
#if salary < 30000- 5%
#if salary is 30000- 70000-15%
#if salary > 70000-25%
salary = float(input("enter a salary:"))
if (salary < 30000):
    tax_rate = 0.5
elif (salary >= 3000 and salary <= 70000):
    tax_rate = 0.15
else:
    tax_rate = 0.25 

print("final tax rate=" , tax_rate*100 , "%")
    
