# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }

def thesaurus(*args):
    dict = {}
    for name in args:
        if dict.get(name[0]):
            dict[name[0]].append(name)
        else:
            dict[name[0]] = [name]
    return dict

print(thesaurus("Иван", "Мария", "Петр", "Илья"))


def thesaurus_adv(*args):
    out_dict = {}
    for elem in args:
        name, second_name = elem.split()
        if not out_dict.get(second_name[0]):
            out_dict[second_name[0]] = { name[0] : [elem] }
        elif not out_dict[second_name[0]].get(name[0]):
            (out_dict[second_name[0]])[name[0]] = [elem]
        else:
            (out_dict[second_name[0]])[name[0]].append(elem)

    return out_dict

print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))