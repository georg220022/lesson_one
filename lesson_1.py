def One_func(obj: str) -> str:
    obj = obj[::-1]  # Переворачиваем строку
    return obj  # Возвращаем перевернутую сьроку


stroka = 'На вход идет эта строка'
print(One_func(stroka))

print("Baltika 9 is a great beer!")
print("Baltika 9 is a great beer!")
# гера взял ветку валеры и сделал изменения!
print('а вот и изменение!')


def valeron(baltika: str):
    return One_func(baltika)


baltika = "Baltika 9 is a great beer!"

print(valeron(baltika))
