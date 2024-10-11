def count_even_elements(arr):
    return sum(1 for x in arr if x % 2 == 0)

# Пример использования
arr = [1, 2, 3, 4, 5, 6]
even_count = count_even_elements(arr)
print("Количество четных элементов:", even_count)
