from my_module import find_index as fi
import datetime
import os

student = {'name': 'john', 'age': 30, 'course': ['Math', 'Science']}
print("************************************")
print(fi(student, 'age'))
print(fi.__doc__)
print(datetime.date.today())
print(os.cpu_count())