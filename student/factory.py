from student.models import Student
import factory
from faker import Faker
import random
FAKE = Faker()
COURSE_LIST = [
    'Python', 'Java', 'C', 'C++', 'JavaScript', 'C#', 
    'Django', 'Go-lang', 'Machine Learning', 'Data Science'
]
def generate_bd_phone_number():
    
    prefix = random.choice(['3', '4', '5', '6', '7', '8', '9'])  
    number = ''.join([str(random.randint(0, 9)) for _ in range(8)]) 
    return f'+8801{prefix}{number}'


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    student_Id = factory.LazyFunction(lambda: FAKE.random_int(min=1000000, max=9999999))  # Ensures a 7-digit ID
    name = factory.Faker('name')
    email = factory.Faker('email')
    phone_number = factory.LazyFunction(generate_bd_phone_number) 
    course = factory.LazyFunction(lambda: random.choice(COURSE_LIST)) 


