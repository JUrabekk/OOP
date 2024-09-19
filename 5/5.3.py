def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if input("Введите пароль: ") == password:
                return func(*args, **kwargs)
            else:
                print("Неверный пароль")
        return wrapper
    return decorator
@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    # ...
    pass
make_burger('beef', withOnion=True, withTomato=False)