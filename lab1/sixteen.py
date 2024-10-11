def shift_right_by_two(arr):
    if len(arr) < 2:
        return arr  # Если массив меньше двух элементов, возвращаем его без изменений
    return arr[-2:] + arr[:-2]

# Пример использования
arr = [1, 2, 3, 4, 5]
shifted_arr = shift_right_by_two(arr)
print("Массив после сдвига на две позиции вправо:", shifted_arr)
