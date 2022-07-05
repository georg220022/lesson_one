def My_func() -> str:
    obj = 'Командный проект'
    return obj
def valeron(func):
    return func()


baltika = "Baltika 9 is a great beer!"

print(valeron(My_func))
