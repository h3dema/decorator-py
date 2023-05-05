from datetime import datetime
import threading

#
# decorator é basicamente um wrapper de outra função
# que devolver a função com as funcionalidades adicionais
#
def timely(func):

    # podemos tornar mais genérico usando args/kwargs
    def call_func(*args, **kwargs):
        # print("args  :", args)
        # print("kwargs:", kwargs)
        # passa o nome para a função
        func(*args, **kwargs)
        # mas precisa colocar também nos argumentos de Timer()
        threading.Timer(5, call_func, args=args, kwargs=kwargs).start()

    return call_func

# problema 2 - queremos alterar o periodo de Timer()
"""
Traceback (most recent call last):
  File "decorato-03.py", line 26, in <module>
    @timely(periodo=1)
TypeError: timely() got an unexpected keyword argument 'periodo'
"""
# @timely(periodo=1)
@timely
def my_func(name):
    print(f"Hello, {name} @ {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    # problema 1 - queremos passar o nome da pessoa aqui
    my_func("João")
