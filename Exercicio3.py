print('Bem-vindo ao Programa de Serviços de Limpeza do Isaque da Silva Rodrigues')
print('*' * 80)

def metragem_limpeza():
   # função que retorna a metragem
   print(' --------------------- Menu 1 de 3 - Metragem Limpeza --------------------- ')
   while True:
      try:
         # validação de numeros inteiros
         metragem = int(input('Entre com a metragem da casa: '))
         if(metragem < 30 or metragem > 700):
            print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!')
         else:
            print('')
            break
      except ValueError:
         print('Favor fornecer apenas números inteiros')

   # calculos de valores das metragens
   valor1 = 60 + (0.3 * metragem)
   valor2 = 120 + (0.5 * metragem)

   if(metragem >= 30 and metragem < 300):
      valorTotal = valor1

   elif metragem >= 300 and metragem <= 700:
      valorTotal = valor2

   # retorno da função
   return valorTotal

def tipo_limpeza():
   # função para definir o tipo da limpeza e seu multiplicador
   print('*' * 80)
   print(' --------------------- Menu 2 de 3 - Tipo de Limpeza --------------------- ')
   while True:
      print('Entre com o tipo de Limpeza: ')
      print('B - Básica - Indicada para sujeiras semanais ou quinzenais')
      print('C - Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras')
      # entrada de dados do usuário
      limpeza = input('')

      if(limpeza == "B"):
         print('Você selecionou a limpeza BÀSICA')
         multiplicador = 1.00
         break
      elif(limpeza == "C"):
         print('Você selecionou a limpeza COMPLETA')
         multiplicador = 1.30
         break
      else:
         print('!!!!!!! Opção Inválida !!!!!!')
         continue
   # retorno da função, multiplicador de limpeza
   return multiplicador

def adicional_limpeza():
   #função que retorna os adicionais de limpeza
   print('*' * 80)
   print(' --------------------- Menu 3 de 3 - Adicional de Limpeza --------------------- ')
   # valores dos adicionais
   adcTotal = 0
   adc1 = 10
   adc2 = 12
   adc3 = 20

   while True:
      # laço para manter usuário dentro do menu até que a opção
      print('Deseja mais algum adicional?')
      print('0 - Não desejo mais nada (encerrar)')
      print('1 - Passar 10 peças de roupas - R$ 10,00')
      print('2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00')
      print('3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00')
      opcao = input('')
      if(opcao == '1'):
         adcTotal += adc1
         print('Opção 1 - Passagem de 10 peças de roupa ADICIONADA!')
         print('')
         continue
      elif(opcao == '2'):
         adcTotal += adc2
         print('Opção 2 - Limpeza de 1 Forno/Micro-ondas ADICIONADA!')
         print('')
         continue
      elif(opcao == '3'):
         adcTotal += adc3
         print('Opção 3 - Limpeza de 1 Geladeira/Freezer ADICIONADA!')
         print('')
         continue
      elif(opcao == '0'):
         adcTotal += 0
         break
      else:
         # retorna ao início do laço, caso uma opção inválida seja selecionada
         print('!!!! Opção invalida! !!!! , tente novamente')
         print('')
         continue
   # retorno do adicional de limpeza
   return adcTotal



# PARTE PRINCIPAL DO PROGRAMA

# retornos das funções atrelados à variáveis
valor_metragem = metragem_limpeza()
valor_limpeza = tipo_limpeza()
valor_adicional = adicional_limpeza()

# cálculo do valor total   ///   total=(metragem*tipo)+adional(is)
total = (valor_metragem * valor_limpeza) + valor_adicional

print('*' * 80)
print('TOTAL: R$ {:.2f} (metragem: {:.2f} * tipo: {:.2f} + adicional: {:.2f}'.format(total, valor_metragem, valor_limpeza, valor_adicional))
print('*' * 80)
