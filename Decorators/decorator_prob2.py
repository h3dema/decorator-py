from datetime import datetime
import threading
import functools

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

        @functools.wraps(func)
        # podemos tornar mais genérico usando args/kwargs
        def call_func(*args, **kwargs):
            # passa o nome para a função
            # nome pode ser o primeiro valor em args
            # ou pode estar no dicionario em kwargs se o parametro foi nomeado
            func(*args, **kwargs)
            # mas precisa colocar também nos argumentos de Timer()
            threading.Timer(periodo, call_func, args=args, kwargs=kwargs).start()

        return call_func

    return timely_internal


@timely(periodo=1)
def my_func(name):
    """
        esta é a funcao simples que sera decorada

        Params
        ======

        name (str):
            nome a ser passado para a funcao
    """
    print(f"Hello, {name} @ {datetime.now().strftime('%H:%M:%S')}")


if __name__ == "__main__":

    print(my_func)
    print(my_func.__name__)
    help(my_func)
