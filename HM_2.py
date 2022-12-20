# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# x = input('Введите число ')

# def summa(x):                           
#     if float(x) < 0:                            
#         x = float(x) * (-1)
#     number = 0

#     for i in str(x):
#         if i != '.':
#             number += int(i)
#     return number

# print(f'Сумма чисел равна {summa(x)}')

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# x = int(input('Введите число '))

# f = 1
# for i in range(x):
#     i = i + 1
#     f = i * f
    
#     print(f)

# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) 
    for x in range (1, n + 1)]   
        
print(sequence(n))
print("Сумма равна =", round(sum(sequence(n))))    