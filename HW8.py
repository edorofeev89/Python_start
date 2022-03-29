import random

x = int(input('Рост Пети: '))

if x < 120:
    print('Рост не может быть менее 120 см')
elif x > 200:
    print('Рост не может быть более 200 см')

people = [random.randint(120, 200) for _ in range(20)]
people.sort(reverse=True)

print(people)

for i in range (len(people)):
    if people[i] == x:
        for p in range(i + 1, len(people)):
            if people[i] != people[p]:
                print(f'Номер по порядку {p + 1}')
                break
        break
    elif people[i] < x:
        for p2 in range(i + 1, len(people)):
            if people[i] != people[p2]:
                print(f'Номер по порядку {i + 1}')
                break
        break
