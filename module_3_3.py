# Распаковка позиционных параметров:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ['первый', 'второй', 'третий']
values_dict = {'a': 1, 'b': 2, 'c': 3}
values_list_2 = [54.32, 'Строка']

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(1, 'строка', True)
print_params(True, 1, 'строка')
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
