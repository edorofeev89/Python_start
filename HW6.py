import random

a = [random.randint(1, 10) for _ in range(10)]
b = [random.randint(1, 10) for _ in range(10)]

count_uniq = [i for i in (a + b)
              if (a + b).count(i) == 1]

print(len(count_uniq))
