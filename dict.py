student = {'name': 'john', 'age': 30, 'course': ['Math', 'Science']}
student['school'] = 'cambridge'
print(student)
print(student['name'])
print(student['course'])
print(student.get('phone', 'Not found'))
print(student.get('age'))

student.update({'name': 'mritunjay', 'age': 20})
print(student)
print("====================")
del student['name']
print(student)
print("====================")
# pop remove from dict and return.
course = student.pop('course')
print(course)
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
print("====================")
for key in student:
    print(key)
print("====================")
for key,value in student.items():
    print(key, value)
