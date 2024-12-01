from functions import salary, hello_who

assert hello_who('1') == 'Hello, 1', 'Hello who error'
assert hello_who('2') == 'Hello, 2', 'Hello who error'
assert hello_who('3') == 'Hello, 3', 'Hello who error'
assert salary(2,1) == 4
assert salary(2,2) == 8