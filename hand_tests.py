from functions import salary, hello_who
#print(hello_who('мыш'))
#print(salary(2,10))
if salary(1,10) != 20:
    print('ERROR')
if hello_who('mbllll') != 'Hello, mbllll':
    print('Failed')
else:
    print('GOOD')
if hello_who('MblLLl') != 'Hello, MblLLl':
    print('Failed')
else:
    print('GOOD')
if salary(54648547,2345689098765) == 256377001922493488910:
    print('GOOD')