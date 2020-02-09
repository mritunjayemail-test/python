from  functools import reduce

def mx(x, y): return x if x > y else y

print(mx(7, 6))
################################################
def square(list1):
    list2 = []
    for num in list1:
        list2.append(num ** 2)
    return list2

n = [1, 2, 3, 4]
print(square(n))
# print(list(map(square(n))))
################################################

n_square = list(map(lambda x: x**2, n))
print(n_square)
#################################################
print([x**2 for x in n])
###############################################
def over_two(list1):
    lst2=[x for x in list1 if x > 2]
    return lst2
print(over_two(n))
print(list(filter(lambda x: x>2, n)))
print([x for x in n if x >2])
################################################
def mult_then_add(list1):
    prod = list1[0]
    print(prod)
    for i in range(0,len(list1)):
        prod = prod * list1[i]
    return prod

print(mult_then_add(n))
print(reduce(lambda x,y: x*y, n ))
##################################################
