# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский
# язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"


dict_nums = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'сеиь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
def num_translate(num_word):
    return dict_nums.get(num_word)

def num_translate_adv(num_word):
    to_key = dict_nums.get(num_word.lower())
    if to_key:
        return to_key.capitalize() if num_word[0].isupper() else to_key
    return None


print(num_translate('zero'))
print(num_translate_adv('Zero'))
print(num_translate_adv('three'))
print(num_translate_adv('eleven'))