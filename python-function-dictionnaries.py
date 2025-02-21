salary = float(input(" Enter salary : "))
month_name = input(" Enter the month name :")

def calculate_expense(salary, percentage):
    return (salary * percentage) / 100

saving_percentage = float(input(" Enter the saving percentage : "))
rent_percentage = float(input(" Enter the rent percentage : "))
electricity_percentage = float(input(" Enter the electricity percentage : "))

expenses = {
    'saving': calculate_expense(salary, saving_percentage),
    'rent': calculate_expense(salary, rent_percentage),
    'electricity': calculate_expense(salary, electricity_percentage)
}

total_expenses = expenses['saving'] + expenses['rent'] + expenses['electricity']
salary_remaining = salary - total_expenses

yearly_rent = expenses['rent'] * 12
yearly_electricity = expenses['electricity'] * 12

additional_saving = 50
left_saving = additional_saving / expenses['saving']

salary_power_2 = salary ** 2

print(f" The saving is {expenses['saving']}")
print(f" The rent is {expenses['rent']}")
print(f" The electricity is {expenses['electricity']}")
print(f" The total expenses are {total_expenses}")
print(f" The salary remaining is {salary_remaining}")
print(f" The yearly rent is {yearly_rent}")
print(f" The yearly electricity is {yearly_electricity}")
print(f" The salary power 2 is {salary_power_2}")
print(f" The left saving is {left_saving}")