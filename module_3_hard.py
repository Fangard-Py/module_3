def calculate_structure_sum(*args):
    summ = 0
    for element in args:
        if isinstance(element, (list, tuple, set)):
            summ += calculate_structure_sum(*element)
        elif isinstance(element, (int, float)):
            summ += element
        elif isinstance(element, dict):
            for keys, values in element.items():
                summ += calculate_structure_sum(keys)
                summ += calculate_structure_sum(values)
        elif isinstance(element, str):
            summ += len(element)
    return summ


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
