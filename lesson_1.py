def One_func(obj: str) -> str:
    obj = obj[::-1] #Переворачиваем строку
    return obj #Возвращаем перевернутую сьроку

stroka = 'На вход идет эта строка'
print(One_func(stroka))