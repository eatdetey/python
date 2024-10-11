import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_prime_factors(num):
    prime_factors_sum = 0
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors_sum += i
    return prime_factors_sum

def count_odd_digits_greater_than_3(num):
    count = 0
    for digit in str(num):
        if int(digit) % 2 != 0 and int(digit) > 3:
            count += 1
    return count

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def product_of_divisors_with_smaller_digit_sum(num):
    original_digit_sum = sum_of_digits(num)
    product = 1
    found = False

    for i in range(1, num + 1):
        if num % i == 0:
            if sum_of_digits(i) < original_digit_sum:
                product *= i
                found = True

    return product if found else 0

number = int(input("Введите число: "))

print("Сумма простых делителей числа:", sum_of_prime_factors(number))
print("Количество нечётных цифр числа, больших 3:", count_odd_digits_greater_than_3(number))
print("Произведение делителей числа с меньшей суммой цифр:", product_of_divisors_with_smaller_digit_sum(number))
