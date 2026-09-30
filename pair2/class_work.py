# print(1)
# print(2)
# print(3)
# print(4)
# ітерація- одне виконання тіла циклу
# for i in range(1,6,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# n = int(input("Введіть число:"))
# for i in range(1,n+1):
#     print(i)

# n = int(input("Введіть число:"))
# i = 1
# while i <= n:
#     print(i)
#     i += 1   #i = i + 1, збільшення на 1-інкремент,зменшення-декремент

# n = int(input("Введіть число:"))
# suma = 0
# for i in range(1,n+1):
#     suma += 1
# print(f'Сума = {suma}')

# n = int(input("Введіть число:"))
# count = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         count += 1
# print(f'Парних чисел {count}')

# while True:
#     n = int(input('Введіть число або слово "0"'))
#     if n == 0:
#         break
#     print(f'Введено число {n}')

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(i)

# n = int(input('Введіть 4-значьне число'))
# digit_last = n % 10
# digit_first = n % 100
# print(digit_last == digit_first)

n = 1234

# while n > 0:
#     digit = n % 10
#     print(f'остання цифра {digit}')
#     # n = n // 10
#     n //= 10

# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     n //= 10
# print(max_digit)

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)

width = 6
height = 4

for row in range(height):
    for col in range(width):
        print('*', end='')
    print()