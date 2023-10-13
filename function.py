# 1
def printt (name):

    print("Don’t compare yourself with anyone in this world…\n"
             "if you do so, you are insulting yourself\n\t\t\t\t\t\t\t\t\t", name)

printt ("Bill Gates")
# 2
def display_even_numbers(start, end):
    if start % 2 != 0:
        start += 1  # Якщо початкове число непарне, збільшуємо його на 1, щоб почати з парного числа
    for num in range(start, end + 1, 2):
        print(num)

start_num = int(input("Введіть перше число: "))
end_num = int(input("Введіть друге число: "))

display_even_numbers(start_num, end_num)
# 3
def draw_square(side_length, symbol, filled):
    if filled:
        for _ in range(side_length):
            print(symbol * side_length)
    else:
        for i in range(side_length):
            if i == 0 or i == side_length - 1:
                print(symbol * side_length)
            else:
                print(symbol + " " * (side_length - 2) + symbol)
side_length = 5
symbol = "*"
filled = False
draw_square(side_length, symbol, filled)
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