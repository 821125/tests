from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Function works wrong!')


if capitalize('') != '':
    raise Exception('Funcion works right!')

print('All tests are done!')

