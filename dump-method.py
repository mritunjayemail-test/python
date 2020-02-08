import json

class Person(object):
    def __init__(self):
        self.name = 'John'
        self.age = 25
        self.id = 1

person = Person()

s = json.dumps(person.__dict__) 
print(s)