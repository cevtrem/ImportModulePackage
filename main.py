import datetime
from people import get_employees
from salary import calculate_salary
from colorful_print import color

b = calculate_salary()
c = get_employees()

if __name__ == '__main__':
    salary_expenses = b * c
    print(salary_expenses, color.green(datetime.date.today()))