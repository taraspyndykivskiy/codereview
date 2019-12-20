"""
Вивести усі цілі числа зі списку
"""

print([element for element in [1, 2.3, 2, 'Bob', [1]] if isinstance(element, int)])