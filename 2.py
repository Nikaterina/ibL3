import random

text = "Откуда мы пришли? Кто мы? Куда мы идём?"

length_key = 10
cntKeys = 10


def forming_key(length_key_):
    lst = [hex(random.randrange(1051, 10000)) for i in range(length_key_)]
    return lst


""" 
чтение и запись в файл
"""


def read_text_list(name_file_, flag: bool):
    with open(name_file_, "r", encoding='utf-8') as f:
        if flag:
            return f.read()
        else:
            group_keys_lst_str = f.readlines()
            group_keys_ = [i.split() for i in group_keys_lst_str]
            return group_keys_


def write_text_list(name_file_: str, text_file_: str | list, flag: bool):
    if flag:
        with open(name_file_, "w", encoding='utf-8') as f:
            f.write(text_file_)
    else:
        lst_str = ""
        for i in text_file_:
            lst_str += ' '.join(i)
            lst_str += "\n"
        with open(name_file_, "w+", encoding='utf-8') as f:
            f.write(lst_str)


"""
Алгоритм создания группы ключей
для каждого элемента ключа выбирается случайная цифра digit_rand от 2 до 5
элемент ключа раскладывается на digit_rand чисел составляющих в сумме этот элемент
второй элемент n2 из полученного набора содержит в себе указание на digit_rand следующим образом:
    последняя цифра элемента n2 записанного в десятичной системе равна digit_rand
"""


def forming_group(cnt_keys: int, key_: list):
    lst = []
    for i in range(cnt_keys):
        lst_one_key = []
        for j in key_:
            k = int(j, 16)
            digit_rand = random.randrange(2, 6)
            n2 = random.randrange(digit_rand, k - digit_rand * 50 + 1, 10)
            if digit_rand == 2:
                n1 = k - n2
                lst_one_key.append(hex(n1))
                lst_one_key.append(hex(n2))
            else:
                lst_k = []
                k_ = k - n2
                sum_n = 0
                for n in range(digit_rand - 2, 0, -1):
                    ni = random.randrange(1, k_ - (n * 50))
                    k_ -= ni
                    lst_k.append(hex(ni))
                    sum_n += ni
                lst_k.insert(0, hex(k - sum_n - n2))
                lst_k.insert(1, hex(n2))
                lst_one_key += lst_k
        lst.append(lst_one_key)
    return lst


def decode_key(lst_key_: list):
    lst = []
    i = 0
    while i < len(lst_key_):
        digit_rand = int(str(int(lst_key_[i + 1], 16))[-1])
        ki = 0
        for j in range(digit_rand):
            ki += int(lst_key_[i + j], 16)
        ki = hex(ki)
        lst.append(ki)
        i += digit_rand
    return lst


# проверка равенства
# key = forming_key(length_key)
# keys = forming_group(cntKeys, key)
# for i in range(len(keys)):
#     decod_key = decode_key(keys[i])
#     print(f'equals: {key == decod_key}')
#     print(f"len: {len(key) == len(decod_key)}")
#     lst = []
#     for j in range(len(key)):
#         lst.append(decod_key[j] == key[j])
#     print(f"lst: {lst}")


# проверка на неизменяемом наборе
# key = forming_key(length_key)
# test_key = ['0x15ec', '0x2485', '0x1bca', '0x1970', '0x1bef']
# keys = [['0xe4', '0x819', '0xcef', '0x1ab', '0x2070', '0x223', '0x47', '0x656', '0x1574', '0x45', '0x170f', '0x21c',
#          '0x184b', '0x3a4'],
#         ['0xaa', '0x1081', '0x33f', '0x15a', '0x28', '0x3f', '0x1275', '0x76', '0x10d2', '0x89', '0x170', '0x86a',
#          '0x10e8', '0x108', '0xbb9', '0xca1', '0x116', '0x4b5', '0xe33', '0x7c7', '0xb', '0x135'],
#         ['0xa8', '0x12b9', '0x28b', '0xd45', '0x1740', '0x1ace', '0xfc', '0x1d1', '0x11de', '0x32c', '0x295',
#          '0x16bb', '0x534'],
#         ['0x4b6', '0x57c', '0x8eb', '0x2cf', '0x517', '0x1634', '0x4e2', '0x458', '0x22f', '0x1063', '0x4d8', '0x1be',
#          '0x2a2', '0x4e9', '0x375', '0xd1a', '0x17f', '0x279', '0x3c', '0x14a4', '0x5d5', '0x13a'],
#         ['0x907', '0x202', '0x440', '0x6a3', '0xa2f', '0x613', '0x8ce', '0x835', '0x340', '0x267', '0x11b7', '0x5dd',
#          '0x1c5', '0xa', '0x154', '0x181c', '0x14f', '0xa4b', '0xa22', '0x273', '0x3c0']]
# for i in range(len(keys)):
#     decod_key = decode_key(keys[i])
#     print(f'equals: {test_key == decod_key}')
#     print(f"len: {len(test_key) == len(decod_key)}")
#     lst = []
#     for j in range(len(test_key)):
#         lst.append(decod_key[j] == test_key[j])
#     print(f"lst: {lst}")


"""
Шифровка и дешифровка текста
"""


def encoding_text(text_: str, key_: list, flag_text: bool, flag_coding: bool) -> str:
    """
    шифрует и дешифрует файлы
    :param text_: имя файла или строка, выбирается параметром flag_text
    :param key_: ключ для шифровки/дешифровки
    :param flag_text: параметр, указывающий на то, что шифруется/дешифруется: файл с текстом или строка
    :param flag_coding: параметр, указывающий на действие: шифровка или дешифровка
    :return: возвращяет зашифрованный/расшифрованный текст в виде строки
    """
    key_ = decode_key(key_)
    text_ = read_text_list(text_, True) if flag_text else text_
    lst = []
    if flag_coding:
        for i in range(len(text_)):
            j = int(i // len(key_))
            el = hex(ord(text_[i]) ^ int(key_[i - len(key_) * j], 16))
            lst.append(el)
        encod_text_ = " ".join(lst)
    else:
        text_ = text_.split()
        for i in range(len(text_)):
            j = int(i // len(key_))
            el = chr(int(text_[i], 16) ^ int(key_[i - len(key_) * j], 16))
            lst.append(el)
        encod_text_ = "".join(lst)
    return encod_text_


# проверка шифровки и дешифровки на изменяющихся данных для строки
# key = [hex(random.randrange(1051, 10000)) for i in range(length_key)]
# group_keys = forming_group(cntKeys, key)
# encod_text = encoding_text(text, group_keys[0], False, True)
# print(encod_text)
# print(group_keys)
# for i in range(len(group_keys)):
#     decod_text = encoding_text(encod_text, group_keys[i], False, False)
#     print(f"{i + 1}: {decod_text}")

# проверка расшифровки на статичных данных
# text1 = ('0x1e46 0xa69 0x11d9 0x19cc 0x268c 0xc6b 0xdc7 0x1616 0x3ef 0x1c34 0x1e67 0xa6b 0x11db 0x19c7 0x2683 0xc63 '
#          '0xdd8 0x120a 0x3be 0x1856 0x1e66 0xe0b 0x11df 0x19c4 0x2287 0x87b 0x9fd 0x1669 0x390 0x1824 0x1a78 0xa17 '
#          '0x11a8 0x1daf 0x2680 0xc6f 0x9b6 0x1616 0x79b')
# gk = [['0xa8e', '0x3b9', '0xc11', '0x4ff', '0x80f', '0x11d', '0x1b9', '0x142a', '0xf5', '0x2cb', '0x154d', '0x40a',
#        '0x78', '0xd9a', '0x392', '0x49b', '0xcf1', '0xd6', '0x71f', '0x66', '0x469', '0x5ad', '0x3d1', '0xd28',
#        '0x502', '0x482', '0x322', '0x109f', '0x64d', '0x528'],
#       ['0x261', '0xa17', '0xde0', '0x151', '0xa99', '0x241', '0x1ed', '0xaae', '0x85d', '0xeb', '0x391', '0xb76',
#        '0xdce', '0xba', '0x4e7', '0xcfb', '0x10d6', '0xe4', '0x6f7', '0x80', '0xd9f', '0x48', '0x544', '0xce6',
#        '0x1ed', '0x285', '0x28b', '0x91', '0x16', '0x18ca', '0x34a'],
#       ['0x133', '0x799', '0x62f', '0x4cc', '0x691', '0xb41', '0x16b', '0x17f', '0x1131', '0x4b2', '0x306', '0x915',
#        '0x76f', '0x89e', '0x167', '0x7d', '0x1761', '0x70e', '0x390', '0x3c', '0x74', '0x7a1', '0x46', '0x15b',
#        '0xc8c', '0x1d2', '0xebe', '0x168', '0x32', '0x2ac', '0x4f8', '0x4b', '0x1531', '0x3e4', '0x99', '0x21b'],
#       ['0x884', '0x7e7', '0x9ed', '0xbc8', '0xad', '0x1b6', '0xd49', '0x89a', '0x14eb', '0x8a4', '0x8c8', '0xd4c',
#        '0x7f5', '0x4af', '0xde', '0x37', '0x553', '0x186', '0x6d', '0xd1', '0xce7', '0x2f', '0x187', '0x41f', '0x994',
#        '0x138', '0x1b8', '0x298', '0x50c', '0x30e', '0xcb7', '0x763', '0x37d', '0x16f'],
#       ['0x15f6', '0x462', '0x60b', '0x2fb', '0x525', '0x687', '0xf5c', '0x35b', '0xdba', '0x284', '0x9f6', '0x2c0',
#        '0x631', '0x1426', '0x3af', '0x1f2', '0x6f', '0x751', '0x9b', '0x39f', '0xa48', '0x108', '0xb1d', '0x30e',
#        '0x242', '0xb5', '0x2b6', '0x144', '0x39d', '0xd', '0xbc8', '0x104c'],
#       ['0x123', '0x735', '0xf35', '0x225', '0xa6', '0xd07', '0x124', '0xf79', '0x66a', '0x7d', '0x11a3', '0x33b',
#        '0x733', '0x101', '0xdc', '0x16de', '0x174', '0x98a', '0x239', '0x43b', '0x1e7', '0x640', '0x1a8', '0x4ec',
#        '0x113', '0xbd', '0x7cb', '0x47', '0x6a3', '0x2b8', '0x7e', '0x6da', '0x47', '0x5', '0x118', '0x144b',
#        '0x675', '0x25', '0x17'],
#       ['0xedd', '0x8f', '0xaec', '0x4ee', '0x75b', '0x1e2', '0x82', '0x14c2', '0x7', '0x98', '0x235', '0x1b5a',
#        '0x102', '0x1f27', '0x156', '0xb1', '0x88', '0x17c', '0x32d', '0x3b2', '0x73', '0x824', '0x233', '0x31d',
#        '0xe2', '0x7d5', '0x670', '0x2d5', '0x2e', '0xe0', '0x4f0', '0x18d', '0x47', '0x2e0', '0x1934'],
#       ['0x2dd', '0xbef', '0x76e', '0x47', '0x3d7', '0xa9', '0xa5f', '0x23f', '0xc7', '0x1d', '0xda4', '0x37e', '0x2e',
#        '0x493', '0xe5b', '0xf34', '0x888', '0x1449', '0x5e7', '0x255', '0x606', '0x290', '0xad7', '0x2', '0x39',
#        '0x45', '0x2a6', '0xd4b', '0x239', '0x27e', '0x18a', '0x334', '0x68', '0xaf0', '0x143', '0xfe1'],
#       ['0x1556', '0x502', '0x216', '0xaad', '0x168', '0xda2', '0x21', '0x820', '0xa5', '0x1cea', '0x3b2', '0x1f06',
#        '0x84', '0x6bd', '0xaf', '0x29', '0x42', '0x8c', '0x997', '0x1de', '0x11a', '0xcc', '0x18e', '0x109c', '0x93',
#        '0x63a', '0xc9', '0xe', '0x42a', '0x17ea'],
#       ['0xba', '0x1184', '0x10f', '0x70b', '0x72', '0x889', '0x4c6', '0xe', '0x5c', '0x6fc', '0xe45', '0xa2', '0x17b',
#        '0xc5c', '0xe59', '0x15f', '0x49', '0xb08', '0xa61', '0xd06', '0xe6', '0x20c', '0xe9', '0x480', '0x33d',
#        '0x841', '0x269', '0x1a7', '0xc7a', '0x259', '0x1b0', '0x170', '0x12f', '0x505', '0xede', '0xd36']]
#
# encod_text = encoding_text(text1, gk[5], False, False)
# print(encod_text)

# проверка шифровки и дешифровки на изменяющихся данных для файлов
key = [hex(random.randrange(1051, 10000)) for i in range(length_key)]
print(f"Ключ: {key}")
group_keys = forming_group(cntKeys, key)
print(f"Группа ключей: {group_keys}")
name_file = "group_keys.txt"
write_text_list(name_file, group_keys, False)
group_keys_read = read_text_list(name_file, False)
encod_text = encoding_text("text4.txt", group_keys_read[0], True, True)
print(f"Зашифрованный текст: {encod_text}")

all_one = True
if all_one:
    for i in range(len(group_keys)):
        decod_text = encoding_text(encod_text, group_keys_read[i], False, False)
        print(f"{i + 1}: {decod_text}")
else:
    decod_text = encoding_text(encod_text, group_keys_read[9], False, False)
    print(f"Расшифрованный текст: {decod_text}")
