nome = str(input('qual seu nome?'))
if nome == 'gustavo':
    print('que belo nome!')
elif nome == 'pedro' or 'maria' or  'paulo':
    print('seu nnome eh bem famoso no brasil!')
elif nome in 'ana claudia jessica julia':
    print('um belo nome feminino!')
else:
    print('seu nome eh bem comum!')
print('tenha um bom dia {}!'.format(nome))