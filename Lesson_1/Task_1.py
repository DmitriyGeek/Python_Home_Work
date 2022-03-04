while True:
    duration=int(input("Введите время в секундах: "))
    d = (duration // 86400) % 30
    h = duration // 3600 % 24
    m = duration // 60 % 60
    s = duration % 60
    if duration <= 60:
        print(f'{s} сек')
    elif duration < 60 * 60:
        print(f'{m} мин {s} сек')
    elif duration < 60 * 60 * 24:
        print(f'{h} час {m} мин {s} сек')
    else:
        print(f'{d} день, {h} час, {m} мин, {s} сек')