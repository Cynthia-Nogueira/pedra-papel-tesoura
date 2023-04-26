import re

texto = ''' atalho 

PARA

EStudar

578+

'''
comp = re.compile(r'[a-z0-9]')
respostas = comp.finditer(texto)

for resposta in respostas:
    print(resposta)