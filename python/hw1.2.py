# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


X = input('введите X ')
Y = input('введите Y ')
Z = input('введите Z ')

left =  not  (X or Y or Z)
right = not X and not Y and not Z

if left == right:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")