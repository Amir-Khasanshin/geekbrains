# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

a = int(input())
sum=0
total=0
for i in range(a):
        total += (1+1/a)**a
        sum +=total
        print (total)
print (sum)