from datetime import datetime
import threading

#
# decorator é basicamente um wrapper de outra função
# que devolver a função com as funcionalidades adicionais
#
def timely(func):

    def call_func():
        func()
        threading.Timer(5, call_func).start()

    return call_func


@timely
def my_func(name: str = ""):
    print(f"Hello, {name} @ {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    my_func()
    """
    problema 1 - passar o nome da pessoa aqui

    Traceback (most recent call last):
    File "decorator-01.py", line 22, in <module>
        my_func("João")
    TypeError: timely.<locals>.call_func() takes 0 positional arguments but 1 was given
    """
