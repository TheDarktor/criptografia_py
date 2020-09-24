# A criptografia utilizada é a ROT 13, onde cada letra é substituída por uma letra que esteja 13 casas a frente
import os
print('-'*70)
funcao = str(input('Você deseja criptografar ou descriptografar?: ')) # Usúario decide se o programa vai criptografar ou descriptografar
print('-'*70)

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
rot = 13 # Rotação de Letras

if funcao == 'criptografar':
    texto = str(input('Insira um texto: ')) # Usuário insere um texto para ser criptografado
    t = ''

    for l in texto: # as letras do texto são separadas e analisadas individualmente
        if l in alfabeto:
            l_index = alfabeto.index(l) # l_index é o index da letra que está sendo analisada
            t += alfabeto[(l_index + rot) % len(alfabeto)]  # t é a nova posição que a letra terá de acordo com seu index + 13 (rot)
        else:
            t += l # se a letra não estiver no alfabeto, ela é ignorada
    print('')
    print('A mensagem criptografada foi salva no desktop com sucesso.')
    with open(os.path.join(os.path.expanduser('~'), 'Desktop', 'criptografado.txt'), 'w+') as arquivo: # Cria um arquivo chamado de "criptografado no Desktop"
        for valor in t:
            arquivo.write(valor)
    print('-'*70)

elif funcao == 'descriptografar':
    texto = str(input('Insira um texto: ')) # Usuário insere um texto para ser descriptografado
    t = ''

    for l in texto: # as letras do texto são separadas e analisadas individualmente
        if l in alfabeto:
            l_index = alfabeto.index(l) # l_index é o index da letra que está sendo analisada
            t += alfabeto[(l_index - rot) % len(alfabeto)] # t é a nova posição que a letra terá de acordo com seu index - 13 (rot)
        else:
            t += l # se a letra não estiver no alfabeto, ela é ignorada
    print('')
    print('A mensagem descriptografada é:') # Exibe o texto descriptografado
    print(t)
    print('-'*70)

else:
    print('"{}" é um comando inválido, tente novamente'.format(funcao)) # Caso o comando inserido pelo usuário seja inválido