def count_min_elements(arr):
    if not arr:
        return 0  # Если массив пустой, возвращаем 0
    min_value = min(arr)
    return arr.count(min_value)

# Пример использования
arr = [1, 3, 1, 5, 1, 7]
min_count = count_min_elements(arr)
print("Количество минимальных элементов:", min_count)
