import operator
a= {"a": 2, "b": 3, "c": 6, "d": 7, "e": 4, "f": 5}
print(a)

sorted_a= sorted(a.items(), key=operator.itemgetter(1))
print('ascending : ',sorted_a)

sorted_a= sorted(a.items(),reverse=True, key=operator.itemgetter(1))
print('dscending : ',sorted_a)
