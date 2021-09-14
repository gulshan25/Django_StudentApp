import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproject.settings')
import django
django.setup()

from studentapp.models import student
from faker import Faker

fg=Faker()
def add_student():
    fname=fg.name()
    femail=fg.email()
    fdob=fg.date()
    fgender='Male'

    std=student.objects.get_or_create(name=fname, email=femail, dob=fdob, gender=fgender)[0]
    return std

def populate_data(n=10):
    for entry in range(n):
        std=add_student()

if __name__ == '__main__':
    print('#'*50)
    print('populating data Please wait...')
    populate_data()
    print('Data populated Complete')
    print('#'*50)             