# склонение слова процент
for i in range(1, 101):
    if 11 <= i <= 14:
        print(f'{i} процентов')
    elif i % 10 == 1:
        print(f'{i} процент')
    elif 2 <= i % 10 <= 4:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
