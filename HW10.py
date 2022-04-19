text = input('Введите текст:').split()

dic = {}

for i in range(len(text)):
    if dic.get(text[i]) is None:
        dic[text[i]] = 1
    else:
        dic[text[i]] = dic[text[i]] + 1

for w, c in dic.items():
    print(f"Слово {w} встречается {c} раз в этом тексте")