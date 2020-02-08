try:
    f = open('dict.py')
except FileNotFoundError as e:
    print('file doent exist:', e)
except Exception as e:
    print('Exception exist:', e)
else:
    print(f.read())
    f.close()
finally:
    print('always finally block execute')


