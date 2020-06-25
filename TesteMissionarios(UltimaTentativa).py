class Estado():
    def __init__(self, canibalEsquerda, missionarioEsquerda, barco, canibalDireita, missionarioDireita):
        self.canibalEsquerda = canibalEsquerda
        self.missionarioEsquerda = missionarioEsquerda
        self.canibalDireita = canibalDireita
        self.missionarioDireita = missionarioDireita
        self.barco = barco
        self.jogos = None

    def fim(self):#Fim de jogo
        if self.canibalEsquerda == 0 and self.missionarioEsquerda == 0:
            return True
        return False

    def estadoValido(self):#Verifica se o estado é valido;
        if self.missionarioEsquerda >= 0 and self.missionarioDireita >= 0 and self.canibalEsquerda >= 0 and self.canibalDireita >= 0 and (self.missionarioEsquerda == 0 or self.missionarioEsquerda >= self.canibalEsquerda) and (self.missionarioDireita == 0 or self.missionarioDireita >= self.canibalDireita):
            print("Estado Valido:" + "(" + str(self.missionarioDireita) + ", " + str(self.canibalDireita) + " | "+ str(self.missionarioEsquerda) + ", " + str(self.canibalEsquerda) + ")")
            return True
        return False

    def __eq__(self, novo):#Criar um novo nó e verifica se ele não é igual;
        return self.canibalEsquerda == novo.canibalEsquerda and self.missionarioEsquerda == novo.missionarioEsquerda and self.barco == novo.barco and self.canibalDireita == novo.canibalDireita and self.missionarioDireita == novo.missionarioDireita
    
    def __hash__(self):#Criar um endereço para localização dentro da arvore;
        return hash((self.canibalEsquerda, self.missionarioEsquerda, self.barco, self.canibalDireita, self.missionarioDireita))

def novaJogada(jogadaAtual):#Criar uma nova jogada e ir adicionando na árvore;
    jogos = []
    if jogadaAtual.barco == 'esquerda':
        novoEstado = Estado(jogadaAtual.canibalEsquerda, jogadaAtual.missionarioEsquerda - 2, 'direita ', jogadaAtual.canibalDireita, jogadaAtual.missionarioDireita + 2)
        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("2 missionários para a direita.")
            jogos.append(novoEstado)
        novoEstado = Estado(jogadaAtual.canibalEsquerda - 2, jogadaAtual.missionarioEsquerda, 'direita ', jogadaAtual.canibalDireita + 2, jogadaAtual.missionarioDireita)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("2 canibais para a direita.")
            jogos.append(novoEstado)
        novoEstado = Estado(jogadaAtual.canibalEsquerda - 1, jogadaAtual.missionarioEsquerda - 1, 'direita ', jogadaAtual.canibalDireita + 1, jogadaAtual.missionarioDireita + 1)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("1 missionário e 1 canibal para a direita.")
            jogos.append(novoEstado)
        novoEstado = Estado(jogadaAtual.canibalEsquerda, jogadaAtual.missionarioEsquerda - 1, 'direita ', jogadaAtual.canibalDireita, jogadaAtual.missionarioDireita + 1)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("1 missionário para a direita.")
            jogos.append(novoEstado)
        novoEstado = Estado(jogadaAtual.canibalEsquerda - 1, jogadaAtual.missionarioEsquerda, 'direita ', jogadaAtual.canibalDireita + 1, jogadaAtual.missionarioDireita)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("1 canibal para a direita.")
            jogos.append(novoEstado)
    else:
        novoEstado = Estado(jogadaAtual.canibalEsquerda, jogadaAtual.missionarioEsquerda + 2, 'esquerda', jogadaAtual.canibalDireita, jogadaAtual.missionarioDireita - 2)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("1 canibal para a esquerda.")
            jogos.append(novoEstado)
        novoEstado = Estado(jogadaAtual.canibalEsquerda + 2, jogadaAtual.missionarioEsquerda, 'esquerda', jogadaAtual.canibalDireita - 2, jogadaAtual.missionarioDireita)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("2 canibais para a esquerda.")
            jogos.append(novoEstado)
        novoEstado = Estado(jogadaAtual.canibalEsquerda + 1, jogadaAtual.missionarioEsquerda + 1, 'esquerda', jogadaAtual.canibalDireita - 1, jogadaAtual.missionarioDireita - 1)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("1 missionario e 1 canibal para a esquerda.")
            jogos.append(novoEstado)
        novoEstado = Estado(jogadaAtual.canibalEsquerda, jogadaAtual.missionarioEsquerda + 1, 'esquerda', jogadaAtual.canibalDireita, jogadaAtual.missionarioDireita - 1)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("1 missionario para a esquerda.")
            jogos.append(novoEstado)
        novoEstado = Estado(jogadaAtual.canibalEsquerda + 1, jogadaAtual.missionarioEsquerda, 'esquerda', jogadaAtual.canibalDireita - 1, jogadaAtual.missionarioDireita)

        if novoEstado.estadoValido():
            novoEstado.jogos = jogadaAtual
            print("1 canibal para a esquerda.")
            jogos.append(novoEstado)

    return jogos

def buscaLargura(estado = Estado(3,3,'esquerda',0,0)):
    estadoInicio = estado
    if estadoInicio.fim():
        return estadoInicio
    borda = list() # Cria uma lista vazia
    analisado = set() #retorna um conjunto vazio para poder adicionar estados compativeis a jogada
    borda.append(estadoInicio)
    while borda:
        estado = borda.pop(0)
        if estado.fim():
            return estado
        analisado.add(estado)
        jogos = novaJogada(estado)
        for filho in jogos:
            if (filho not in analisado) or (filho not in borda):
                borda.append(filho)
    return None

def melhorSolucao(solucao):
    caminho = []
    caminho.append(solucao)
    jogos = solucao.jogos
    print("Busca em Largura")

    while jogos:
        caminho.append(jogos)
        jogos = jogos.jogos
    for t in range(len(caminho)):
        estado = caminho[len(caminho) - t - 1]
        print("(C" + str(estado.canibalEsquerda) +",M"+ str(estado.missionarioEsquerda) + " Esquerda|Direita C" + str(estado.canibalDireita) + ",M" + str(estado.missionarioDireita) + ")" + " Lado Barco: "+ str(estado.barco))

def main():
    solucao = buscaLargura()
    melhorSolucao(solucao)

main()