print('Bem-vindo a Loja de Isaque')

valorProduto = float(input('Entre com valor do produto: '))
valorQuantidade = float(input('Entre com valor da quantidade: '))
valorFrete = 0.0

if 0 <= valorQuantidade < 11:
    valorFrete = 30.0
elif 11 <= valorQuantidade < 101:
    valorFrete = 60.0
elif 101 <= valorQuantidade < 1001:
    valorFrete = 120.0
if valorQuantidade >= 1001:
    valorFrete = 240.0
else:
    print('Quantidade Incorreta!!')

print('O valor sem frete foi: %.2f' % (valorProduto * valorQuantidade))
print('O valor com frete foi: %.2f (Frete de R$ %.2f)' % (valorProduto * valorQuantidade + valorFrete, valorFrete))

