# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = Y = Z = [True, False]
res = True
for x in X:
    for y in Y:
        for z in Z:
            if not(not(x or y or z) == (not(x) and not(y) and not(z))):
                res = False
if res: res = 'Истина' 
else: res = 'Ложь'
print(res)


