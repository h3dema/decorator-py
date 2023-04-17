from datetime import datetime
import threading

#
# decorator é basicamente um wrapper de outra função
# que devolver a função com as funcionalidades adicionais
# para passarmos os argumentos para o próprio decorator,
# precisamos definir mais uma camada mais externa que recebe estes argumentos, e
# dentro dele definimos um decorator como vimos anteriormente.
# E, por fim, dentro deste definimos a função wrapper que chama a função que foi decorrada.
#
def timely(periodo: int = 5):

    def timely_internal(func):

        # podemos tornar mais genérico usando args/kwargs
        def call_func(*args, **kwargs):
            # passa o nome para a função
            func(*args, **kwargs)
            # mas precisa colocar também nos argumentos de Timer()
            threading.Timer(periodo, call_func, args=args, kwargs=kwargs).start()

        return call_func

    return timely_internal


def log_parametros(func):

    def wrapper(*args, **kwargs):
        print("*" * 40)
        print(f"Função iniciada em {datetime.now().strftime('%H:%M:%S')}")
        if "name" in kwargs:
            print("NOME:", kwargs["name"])
        else:
            print("NOME não foi definido")
            print("Args:", args)
        print("*" * 40)
        func(*args, **kwargs)

    return wrapper

# problema 3 - queremos logar o parametro passado para a função my_func()
# problema 2 - queremos alterar o periodo de Timer()
@log_parametros
@timely(periodo=1)
def my_func(name):
    print(f"Hello, {name} @ {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    # problema 1 - queremos passar o nome da pessoa aqui
    # my_func("João")
    my_func(name="João")
