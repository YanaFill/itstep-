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