#

## cwiczenie - routing + views

1. Utwórz aplikację - calculus
2. Utwórz widok/i obsługujące adresy

```
   /calculus/add/1/2
   /calculus/sub/1/2 
   ...
```


## cwiczenie - include

1. zrób include urls dla aplikacji calculus
2. dodaj widok
    
    /calculus/ - wypisz dostępne operacje


    Dostępne operacje to: add, sub, mul, div

## Dodanie szablonu

Dodaj szablon w aplikacji calculus - dla operacji. 

## Uzycie szablonu

Popraw szablon (z użyciem extends ) dla widoku calculus/home

przekaż do kontekstu zestaw dostępnych operacji. 


Jeśli chcesz wykoma dodawanie, to wejdź na adres

/calculus/add/1/2/

rezultatem będzie wypisane 

Result: 3


## tworzymy aplikacje tasks

wykorzystujac kod przygotowany do aplikacji flaskowej

https://github.com/rkorzen/python_17_12_2022/blob/master/web_projects/flask_projects/todos/db.py
 
wykorzystaj istniejący todos.json

wyświetlamy todosy:

1. widok wyświetlający listę todos
2. widok szczegółów


##  dodajemy update todo

   - formularz na stronie szczegółów
   - obsługa metody POST w widoku details
   - akutalizacja serwisu - dodanie metody update


## Dodanie końcówki /contact/

Obsługa formularza contact
- przeniesc w całosci formularz contact do aplikacji main
- dodac widok (+ url)
- wyprintowac dane wysłane z formularza

## przerobic formularz kontaktowy na bootstrapowy - przy pomocy crispy

## Django extensions

https://django-extensions.readthedocs.io/en/latest/shell_plus.html?highlight=print%20sql#sql-queries

# Migracje

python manage.py showmigrations   # pokazuje stan wykonania migracji
python manage.py makemigrations   # przygotowuje migracje
python manage.py makemigrations --empty tasks  # tworzy pustą migrację w aplikacji tasks
python manage.py sqlmigrate tasks 0002   # pokazuje sql jaki bedzie wykonany dla migracji 0002 z aplikacji tasks

python manage.py migrate # wykona niewykoanne migracje

jakby trzeba było wykona migrację... nie wykonując sqla

https://stackoverflow.com/questions/46772762/django-migrate-fake-and-fake-initial-explained


python manage.py inspectdb  # tworzenie modeli na podstawie istniejącej bazy danych


## django management commands(in shell)

https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

