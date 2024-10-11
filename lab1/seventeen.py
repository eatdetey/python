def shift_right_by_one(arr):
    if len(arr) < 1:
        return arr  # Если массив пустой или содержит один элемент, возвращаем его
    return arr[-1:] + arr[:-1]

# Пример использования
arr = [1, 2, 3, 4, 5]
shifted_arr = shift_right_by_one(arr)
print("Массив после сдвига на одну позицию вправо:", shifted_arr)
