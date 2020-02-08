
def function(greeting, name='You'):
    return '{}, {} '.format(greeting, name)


print(function('Hello', name='Mritunjay'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


course = ['math', 'science']
info = {'name': 'Mritunjay', 'age': 30}
print("****************************")
student_info(course, info)
print("****************************")
student_info(*course, **info)
print("****************************")
student_info('math', 'science', name='Mritunjay', age=30)
