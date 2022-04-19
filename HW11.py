import random
import string

dict_1 = {k: v for k, v in
          zip([random.choice(string.ascii_lowercase) for _ in range(10)],
              [random.randint(1, 100) for _ in range(10)])}

dict_2 = {k: v for k, v in
          zip([random.choice(string.ascii_lowercase) for _ in range(10)],
              [random.randint(1, 100) for _ in range(10)])}

dict_3 = {}

for i in dict_1.keys():
    if dict_3.get(i) is None:
        dict_3[i] = dict_1[i]
    else:
        if dict_3[i] < dict_1[i]:
            dict_3[i] = dict_1[i]

for i in dict_2.keys():
    if dict_3.get(i) is None:
        dict_3[i] = dict_2[i]
    else:
        if dict_3[i] < dict_2[i]:
            dict_3[i] = dict_2[i]

print(dict_1)
print(dict_2)
print(dict_3)