keyCenStr = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54"
decryptMessCenStr = "Штирлиц – Вы Герой!!"
encryptMessCenStr = "D8 F2 E8 F0 EB E8 F6 20 2D 20 C2 FB 20 C3 E5 F0 EE E9 21 21"
encryptMessMulStr = "DD FE FF 8F E5 A6 C1 F2 B9 30 CB D5 02 94 1A 38 E5 5B 51 75"
keyMulStr = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 55 F4 D3 07 BB BC 54"
encryptMessMulStr2 = "D8 F2 E8 F0 EB E8 F6 20 2D 20 C2 FB 20 C1 EE EB E2 E0 ED 21"
decryptMessMulStr = "Штирлиц - Вы Болван!"


def str_in_int16(a: str):
    lst = a.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i], 16)
    return lst


def mess_in_int_or_hex(a: str, flag: bool):
    """
    Преобразует строку в лист с инт или лист с хекс
    :param a: строка для преобразования
    :param flag: True  для преобразования в int, False - hex
    :return: лист с интами или хексами
    """
    lst = []
    if flag:
        for i in a:
            hex_ = i.encode('cp1251', 'replace').hex()
            lst.append(int(hex_, 16))
    else:
        for i in a:
            hex_ = i.encode('cp1251', 'replace').hex()
            lst.append(hex(int(hex_, 16)))
    return lst


def int_in_hex_or_mess(lstS: list, flag: bool):
    """
    Преобразует лист с инт в хекс или строку
    :param lstS: лист с интами
    :param flag: True  для преобразования в hex, False - строку
    :return: символьная читаемая строка
    """
    lst = []
    if flag:
        for i in lstS:
            lst.append(hex(i))
        lst = ' '.join(i[2::] for i in lst)
    else:
        for i in lstS:
            lst.append(i.to_bytes(1, 'big').decode('cp1251'))
        lst = ''.join(i for i in lst)
    return lst


def coding(text, key):
    if len(text) != len(key):
        return "длины не равны"
    else:
        codText = []
        for i in range(len(text)):
            codText.append(text[i] ^ key[i])
        return codText


# проверка ключа шифровальщиков Мюллера
# keyCenStr = str_in_int16(keyCenStr)
# encryptMessCenStr = str_in_int16(encryptMessCenStr)
# encryptMessMulStr = str_in_int16(encryptMessMulStr)
# keyMulStr = str_in_int16(keyMulStr)
# encryptMessMulStr2 = str_in_int16(encryptMessMulStr2)
#
# messMul = int_in_hex_or_mess(coding(encryptMessMulStr, keyMulStr), False)
# print(messMul)

# поиск ключа для открытого кода СНовымГодом, друзья!
# messNG = "СНовымГодом, друзья!"
# # encryptMessMulStr = "DD FE FF 8F E5 A6 C1 F2 B9 30 CB D5 02 94 1A 38 E5 5B 51 75"
# encryptMessNG = mess_in_int_or_hex(messNG, True)
# keyNG = int_in_hex_or_mess(coding(encryptMessNG, str_in_int16(encryptMessMulStr)), True)
# print(keyNG)
# print(int_in_hex_or_mess(coding(str_in_int16(encryptMessMulStr), str_in_int16(keyNG)), False))

# проверка определения шифротекста при известном ключе и известном открытом тексте
# keyCenStr = "05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 0B B2 70 54"
# decryptMessCenStr = "Штирлиц – Вы Герой!!"
# encryptMessMulStr = "DD FE FF 8F E5 A6 C1 F2 B9 30 CB D5 02 94 1A 38 E5 5B 51 75"
# messCenr = int_in_hex_or_mess(coding(str_in_int16(keyCenStr), mess_in_int_or_hex(decryptMessCenStr, True)), True)
# print(messCenr)
