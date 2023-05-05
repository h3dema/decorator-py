
# função que gera
def hello_function(name: str):

    # função interna (que será gerada)
    def say_hi_to():
        return f"Hi, {name}"

    return say_hi_to


if __name__ == "__main__":
    helloJoao = hello_function("João")
    print(helloJoao())

    helloMaria = hello_function("Maria")
    print(helloMaria())
