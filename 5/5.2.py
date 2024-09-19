def check_password(func):
    def wrapper():
        password = input("Введите пароль: ")
        if password == "123":
            return func()
        else:
            print("В доступе отказано")
            return None
    return wrapper
@check_password
def fibonacci():
    n = int(input("Введите число n для вычисления числа Фибоначчи: "))
    def calc_fibonacci(n):
        if n <= 1:
            return n
        else:
            return calc_fibonacci(n-1) + calc_fibonacci(n-2)
    result = calc_fibonacci(n)
    return f"Число Фибоначчи для n={n} равно {result}"
print(fibonacci())