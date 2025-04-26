import matplotlib.pyplot as plt, random, math

class Passaro:

    def __init__(self, x: float = None, y: float = None, mov: list[float, float] = None) -> None:
        self.x = random.random() * 2 - 1 if x is None else x
        self.y = random.random() * 2 - 1 if y is None else y
        self.mov = [random.random() * 2 - 1, random.random() * 2 - 1] if mov is None else mov # Vetor de velocidade

    def aplicar_forca(self, forca: tuple[float, float], C: float = .1) -> None:
        self.mov[0] += forca[0] * C
        self.mov[1] += forca[1] * C

    def aplicar_movimento(self, C: float = .1) -> None:
        """:param float C: Constante aplicada ao movimento"""
        self.x += self.mov[0] * C
        self.y += self.mov[1] * C    

    def distancia(self, alvo: 'Passaro') -> float:
        return (self.x - alvo.x)**2 + (self.y - alvo.y)**2

def get_centro(populacao: list[Passaro]) -> tuple[float, float]:
    return sum(p.x for p in populacao) / len(populacao), sum(p.y for p in populacao) / len(populacao)

def get_direcao_media(populacao: list[Passaro]) -> tuple[float, float]:
    return sum(p.mov[0] for p in populacao) / len(populacao), sum(p.mov[1] for p in populacao) / len(populacao)

def get_matriz_distancia(populacao: list[Passaro]) -> list[list[tuple[int, float]]]:
    res = []
    for i in range(len(populacao)):
        linha = []
        for j in range(len(populacao)):
            linha.append((j, populacao[i].distancia(populacao[j])))
        res.append(linha)
    return res

def k_proximos(matriz_distancia: list[list[tuple[int, float]]], passaro: int, k: int = 5) -> list[float]:
    return sorted(matriz_distancia[passaro], key=lambda x: x[1])[1:k+1]

def passo(populacao: list[Passaro]) -> None:
    dir_media = get_direcao_media(populacao)
    centro = get_centro(populacao)
    matriz_distancia = get_matriz_distancia(populacao)

    for i, p in enumerate(populacao):
        proximos = [populacao[prox[0]] for prox in k_proximos(matriz_distancia, i)]
        centro_proximos = get_centro(proximos)
        #p.aplicar_forca(dir_media, C=0.02)
        p.aplicar_forca((centro[0] - p.x, centro[1] - p.y), C=0.2)
        p.aplicar_forca((-centro_proximos[0] + p.x, -centro_proximos[1] + p.y))
        p.aplicar_movimento()

pop = [Passaro() for _ in range(50)]

for i in range(1000):
    passo(pop)
    for p in pop:
        plt.scatter(p.x, p.y, c='r')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.draw()
    plt.pause(0.02)
    plt.clf()