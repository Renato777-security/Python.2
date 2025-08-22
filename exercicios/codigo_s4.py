opcao_usuario=int(input('Digite 1 para receber e-mail de propaganda ou 2 para não receber'))

if opcao_usuario == 1:
   print('Você escolheu receber e-mails de propaganda')
elif opcao_usuario == 2:
   print('Você escolheu não receber e-mails de propaganda')
else:
   print('opcão invalida. Por favor, escolha uma opção')
