print('Bem-Vindo a Sorveteria do Isaque da Silva Rodrigues')
print('---------------------------------------------Cardápio------------------------------------------------')
print('|  Código  |     Descrição        |  Tamanho P (500ml)  |  Tamanho M (1000ml)  |  Tamanho G (1000ml)|')
print('|    TR    | Sabores Tradicionais |       R$ 6,00       |       R$ 10,00       |       R$ 18,00     |')
print('|    ES    | Sabores Especiais    |       R$ 7,00       |       R$ 12,00       |       R$ 21,00     |')
print('|    PR    | Sabores Premium      |       R$ 8,00       |       R$ 14,00       |       R$ 24,00     |')
print('-----------------------------------------------------------------------------------------------------')


def tradicionais(valor=None):
    if tamanho == "P":
        valor = trP
        return valor
    elif tamanho == "M":
        valor = trM
        return valor
    elif tamanho == "G":
        valor = trG
        return valor


def especiais(valor=None):
    if tamanho == "P":
        valor = esP
        return valor
    elif tamanho == "M":
        valor = esM
        return valor
    elif tamanho == "G":
        valor = esG
        return valor


def premium(valor=None):
    if tamanho == "P":
        valor = prP
        return valor
    elif tamanho == "M":
        valor = prM
        return valor
    elif tamanho == "G":
        valor = prG
        return valor


# sabores tradicionais
trP = 6
trM = 10
trG = 18
# sabores especiais
esP = 7
esM = 12
esG = 21
# sabores premium
prP = 8
prM = 14
prG = 24

valor = 0
total = 0

while True:
    # entradas
    sabor = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')
    tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G): ')

    # validadores
    validaSabor = sabor == "TR" or sabor == "ES" or sabor == "PR"
    validaTamanho = tamanho == "P" or tamanho == "M" or tamanho == "G"
    if not validaSabor:
        print('!!!!!!!!!!!!!!!!!! CÓDIGO INVALIDO !!!!!!!!!!!!!!!!!!" ')
        print('Você digitou "{}", escolha entre as opções disponíveis (TR/ES/PR): '.format(sabor))
        sabor = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')
    if not validaTamanho:
        print('!!!!!!!!!!!!!!!!!! TAMANHO INVÁLIDO !!!!!!!!!!!!!!!!!! ')
        print('Você digitou "{}", escolha entre as opções disponíveis (P/M/G): '.format(tamanho))
        tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G): ')

    # Condicionais para utilizar funções relacionadas aos respectivo sabores
    if sabor == "TR":
        sabor = "TRADICIONAL"
        valor = tradicionais(valor)
        total += valor
        print('Você pediu um sorvete sabor {} {} de R$ {},00'.format(sabor, tamanho, valor))
        print('----------------------------------------------------------------------------')
    if sabor == "ES":
        sabor = "ESPECIAL"
        valor = especiais(valor)
        total += valor
        print('Você pediu um sorvete sabor {} {} de R$ {},00'.format(sabor, tamanho, valor))
        print('----------------------------------------------------------------------------')
    if sabor == "PR":
        sabor = "PREMIUM"
        valor = premium(valor)
        total += valor
        print('Você pediu um sorvete sabor {} {} de R$ {},00'.format(sabor, tamanho, valor))
        print('----------------------------------------------------------------------------')

    # Acrescentar itens
    continuar = input('Deseja pedir mais alguma coisa? (S/N): ')
    if continuar == 'S':
        continue
    else:
        print('O valor total a ser pago é: R$ {:.2f}'.format(total))
        break

print('Pedido realizado com sucesso!')