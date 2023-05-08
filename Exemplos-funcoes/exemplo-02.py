

# função externa
def plus_one(number):

    # função interna
    def mais_valor(number: int, constante: int = 1) -> int:
        return number + constante

    result = mais_valor(number)
    return result


if __name__ == "__main__":
    print("plus_one", plus_one(4))

    # não conseguimos acessar diretamente a função interna
    """
        Traceback (most recent call last):
          File "exemplo-02.py", line 24, in <module>
            print("mais_valor", mais_valor(1))
        NameError: name 'mais_valor' is not defined
    """
    # print("mais_valor", mais_valor(1))
