# 4
def find_min(a, b, c, d, e):
    return min(a, b, c, d, e)

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
num4 = float(input("Введіть четверте число: "))
num5 = float(input("Введіть п'яте число: "))

min_number = find_min(num1, num2, num3, num4, num5)
print("Мінімальне число:", min_number)

# 5
def calculate_product_in_range(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product

range_start = int(input("Введіть початок діапазону: "))
range_end = int(input("Введіть кінець діапазону: "))

result = calculate_product_in_range(range_start, range_end)
print("Добуток чисел у зазначеному діапазоні:", result)

# 6
def count_digits(number):
    return len(str(number))

input_number = int(input("Введіть число: "))

digit_count = count_digits(input_number)
print("Кількість цифр у числі:", digit_count)

# 7
def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

input_number = int(input("Введіть число: "))

if is_palindrome(input_number):
    print("Число є паліндромом.")
else:
    print("Число не є паліндромом.")
print()