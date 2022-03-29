import random

a = [random.randint(1, 50) for _ in range(20)]

counter = 0

for i in range (1, len(a) - 1):
    if a[i] > a[i-1] + a[i+1]:
        counter +=1
print (f'Кол-во чисел {counter}')