
# nossa função básica
def mais_valor(number: int, constante: int = 1) -> int:
    return number + 1


# função que recebe outra função como parametro
def function_call(function, number_to_add=5):
    return function(number_to_add)


if __name__ == "__main__":
    print(function_call(mais_valor))
    print(function_call(mais_valor, 10))
