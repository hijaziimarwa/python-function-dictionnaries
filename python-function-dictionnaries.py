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