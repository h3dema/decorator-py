
def mais_valor(number: int, constante: int = 1) -> int:
    return number + constante


print("+Valor:", mais_valor(5))
# atribui função a uma variavel
add = mais_valor
# chama a função usando a variável
print("Soma 1:", add(5))
print("Soma 2:", add(5, 2))
