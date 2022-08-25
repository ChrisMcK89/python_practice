class Salary:
    def __init__(self, monthly_income):
        self.monthly_income = monthly_income
        
    
    def total_salary(self):
        return (self.monthly_income * 12)


class Employee:
    def __init__(self, monthly_income, bonus):
        self.monthly_income = monthly_income
        self.bonus = bonus
        self.salary = Salary(monthly_income)

    def get_total(self):
        return (self.salary.total_salary() + self.bonus)

# employee_1 = Employee(2500, 500)
# print(employee_1.get_total())

