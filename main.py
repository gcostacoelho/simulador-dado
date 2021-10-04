import random as r

while True:
    resp = input('Deseja rodar o dado?\nR: ').lower()
    while resp != 'sim' and resp != 'nao':
        print('Insira uma resposta válida (Sim ou Nao)')
        resp = input('Deseja rodar o dado?\nR: ').lower()
    if resp == 'sim':
        dado = r.randint(1, 6)
        print(f'O dado deu {dado}')
    else:
        print("Saindo do programa, obrigado")
        break