from datetime import datetime
import threading

#
# decorator é basicamente um wrapper de outra função
# que devolver a função com as funcionalidades adicionais
#
def timely(func):

    def call_func(name):
        # passa o nome para a função
        func(name)
        # mas precisa colocar também nos argumentos de Timer()
        threading.Timer(5, call_func, kwargs={"name": name}).start()

    return call_func


@timely
def my_func(name: str = ""):
    print(f"Hello, {name} @ {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    # queremos passar o nome da pessoa aqui
    my_func("João")
