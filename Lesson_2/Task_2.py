# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до
# и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел
# со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное:
# дополнить числа до двух разрядов нулём!

def list_func(arg):

    target_list = []
    for el in arg:
        if el.isdigit():
            target_list.extend([f'"{int(el):02d}"'])
        elif el[0] == '+' or el[0] == '-' and el[1].isdigit():
            new_el = el[0]
            target_list.extend(['"' + new_el + f'{int(el[1:]):02d}"'])
        else:
            target_list.append(el)

    result = ' '.join(target_list)
    return print(result)
text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']



list_func(text_list)
