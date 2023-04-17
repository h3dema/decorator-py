from datetime import datetime
import threading


def my_func(name: str):
    print(f"Hello, {name} @ {datetime.now().strftime('%H:%M:%S')}")
    threading.Timer(5, my_func, kwargs={"name": name}).start()

if __name__ == "__main__":
    my_func("João")
