def print(*args, **kwargs):
    new_args = [str(arg).upper() for arg in args]
    built_in_print(*new_args, **kwargs)
built_in_print = __builtins__.print
# Пример использования
print('Нельзя ли потише?')