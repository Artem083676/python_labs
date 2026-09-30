#1

# N = int(input("Введіть число:"))
# kratne3 = 0
# kratne5 = 0
# suma1 = 0
# suma2 = 0
# for i in range(N - 1):
#     N = N - 1
#     if N % 3 == 0:
#         kratne3 += 1
#     if N % 5 == 0:
#         kratne5 += 1

# for g in range(kratne3 + 1):
#     suma1 = suma1 +(3 * g)
# for j in range(kratne5 + 1):
#     suma2 = suma2 +(5 * j)

# kratni = kratne3 + kratne5
# suma = suma1 + suma2
# serednie = suma / kratni
# print('Кількість: {kratni}')
# print('Сума: {suma}')
# print('Середнє: {serednie}')

#2

# N = int(input("Введіть число:"))
# count = 0
# suma = 0
# maxim = 0
# minim = 9
# while N > 0:
#     n = N % 10
#     N = N // 10
#     count = count + 1
#     suma = suma + n
#     if n > maxim:
#         maxim = n
#     if n < minim:
#         minim = n

# print(f'Кількість цифр: {count}')
# print(f'Сума цифр: {suma}')
# print(f'Найбільша цифра: {maxim}')
# print(f'Найменша цифра: {minim}')

#3

# N = int(input("Введіть число:"))
# n = 0
# for i in range(N):
#     while n != N:
#         if n < 10:
#             n = n + 1
#             a = n % 10
#             if a == 0 or n % a != 0:
#                 pass
#             else:
#                 print(n)
#         else:
#             n = n + 1
#             a = n % 10
#             b = n % 100
#             if a == 0 or n % a != 0 or n % b != 0:
#                 pass
#             else:
#                 print(n)
        



