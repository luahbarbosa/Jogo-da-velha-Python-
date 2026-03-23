jogo_velha=[
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def exibir(jogo_velha): 
    for linha in jogo_velha:
        print('|'.join(linha))
        print( '-' * 6 )

def jogadores(): 
    jogador_um=input("Digite a sua escolha x ou o:")
    jogador_dois=input("Digite a sua escolha x ou o:")
    while jogador_um not in ["x", "o"] or jogador_dois not in ["x", "o"]:
        print("Escolha inválida! escolha x ou o")
        jogador_um=input("Digite a sua escolha x ou o:")
        jogador_dois=input("Digite a sua escolha x ou o:")
    while  jogador_dois == jogador_um:
        print("simbolo ja escolhido ")
        jogador_dois=input("jogador dois escolha outro simbolo:")
    return jogador_um, jogador_dois

def posicao(jogo_velha, linha, coluna, jogador_atual):
    if jogo_velha[linha][coluna] == " ":
        jogo_velha[linha][coluna] = jogador_atual
        return True
    else:
        print("espaço ocupado!")
        return False 
    
def vencedor(jogo_velha, jogador_atual):
    for linha in jogo_velha:
        if linha[0] == linha[1] == linha[2] == jogador_atual:
            return True
    for coluna in range(3):
        if jogo_velha[0][coluna] == jogo_velha[1][coluna] == jogo_velha[2][coluna] == jogador_atual:
            return True
    if jogo_velha[0][0] == jogo_velha[1][1] == jogo_velha[2][2] == jogador_atual:
        return True
    if jogo_velha[0][2] == jogo_velha[1][1] == jogo_velha[2][0] == jogador_atual:
        return True
    return False

def empate(jogo_velha ):   
    for linha in jogo_velha:  
        if " " in linha:
            return False  
    return True  

jogador_um, jogador_dois=jogadores()
jogador_atual=jogador_um


while True:
    exibir(jogo_velha)
    linha=input(f" {jogador_atual} digite um numero entre (0-2)")  
    coluna=input(f" {jogador_atual} digite um numero entre (0-2)")
    if linha.isdigit() and coluna.isdigit():  
        linha= int(linha)
        coluna= int(coluna)
    else:
        print("Errada!digite um numero entre (0-2) ")
        continue

    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2: 
        print("Valor digitado nao encontrado, digite outro valor:")
        continue 
    
    if posicao(jogo_velha, linha, coluna, jogador_atual):
        if vencedor(jogo_velha, jogador_atual):
            print(f"Parabens jogador {jogador_atual} venceu!")
            exibir(jogo_velha)
            break
    if empate(jogo_velha):
        print("jogo empatado!")
        exibir(jogo_velha)
        break
    if jogador_atual == jogador_um:
        jogador_atual = jogador_dois
    else:
        jogador_atual = jogador_um
