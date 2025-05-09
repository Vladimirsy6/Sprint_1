def digit_root(num):
    while num >= 10:  # Пока число больше или равно 10
        num = sum(int(digit) for digit in str(num))  # Разбиваем на цифры и суммируем
    return num

# Пример использования
print(digit_root(775634))  # 9
print(digit_root(3463))  # 9
print(digit_root(889543))  # 4