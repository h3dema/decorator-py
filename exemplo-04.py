
# função que gera
def hello_function(name):

    # função interna (que será gerada)
    def say_hi_to():
        return f"Hi, {name}"

    return say_hi_to


if __name__ == "__main__":
    hello = hello_function("João")
    print(hello())

    hello2 = hello_function("Maria")
    print(hello2())
