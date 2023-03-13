from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt
from progress.bar import Bar

bar = Bar('Processing', max=20)

print(dt.datetime.today().strftime("%d.%m.%Y"))


# pip freeze > requirements.txt

if __name__ == '__main__':
    for i in range(1):
        calculate_salary()
        get_employees()
        bar.next()
    bar.finish()
