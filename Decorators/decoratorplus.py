from datetime import datetime
#
# importamos a ultima versao do decorator que criamos anteriormente
#
from decorator_04 import timely


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
@log_parametros
@timely(periodo=1)
def my_func(name):
    print(f"Hello, {name} @ {datetime.now().strftime('%H:%M:%S')}")


if __name__ == "__main__":
    # problema 1 - queremos passar o nome da pessoa aqui
    # my_func("João")
    my_func(name="João")
