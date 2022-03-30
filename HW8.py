import random

x = int(input('Рост Пети: '))

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
