from datetime import datetime


# Принимает словарь с паролем и добавляет его в файл
def add_password(site_name, login, password, src='./data/sdrowssap.txt'):
    the_date = datetime.now()
    the_date = the_date.strftime('%H:%M:%S  %d.%m.%Y')
    with open(src, 'a') as f1:
        for el in (the_date, site_name, login, password):
            print(el, end=';  ', file=f1)
        print(file=f1)

