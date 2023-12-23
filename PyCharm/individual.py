def cyrillic_to_latin(t, chars=" !?"):
    def decorator(func):
        def wrapper(s):
            s_lower = s.lower()

            converted_str = ''.join([t[char] if char in t else char for char in s_lower])

            for char in chars:
                converted_str = converted_str.replace(char, '-')

            converted_str = '-'.join(filter(None, converted_str.split('-')))

            return converted_str

        return wrapper

    return decorator

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

@cyrillic_to_latin(t, chars="?!:;,. ")
def convert_to_latin(s):
    return s

user_input = input("Введите строку на кириллице: ")

result = convert_to_latin(user_input)
print("Результат преобразования:", result)
