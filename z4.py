# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

decimal = int(input('Введите число: '))
binary = []
while True:
    remainder = decimal%2
    binary.append(remainder)
    decimal //=2
    if decimal == 0 or decimal == 1:
        binary.append(decimal)
        break
binary = reversed(binary)
print(''.join(map(str,binary)))