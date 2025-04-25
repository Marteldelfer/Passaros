import matplotlib.pyplot as plt, random, math

class Passaro:

    def __init__(self, x: float = None, y: float = None, mov: list[float, float] = None) -> None:
        self.x = random.random() if x is None else x
        self.y = random.random() if y is None else y
        self.mov = [random.random(), random.random()] if mov is None else mov # Vetor de velocidade

    def aplicar_forca(self, forca: tuple[float, float], C: float = .1) -> None:
        self.mov[0] += forca[0] * C
        self.mov[1] += forca[1] * C

    def aplicar_movimento(self, C: float = .1) -> None:
        """:param float C: Constante aplicada ao movimento"""
        self.x += self.mov[0] * C
        self.y += self.mov[1] * C    

def get_centro(populacao: list[Passaro]) -> tuple[float, float]:
    return sum(p.x for p in populacao) / len(populacao), sum(p.y for p in populacao) / len(populacao)

def passo(populacao: list[tuple[float, float]]) -> list[tuple[float, float]]:
    raise NotImplementedError #TODO
        
p = Passaro(0, 1, [1, 0])
CENTRO = 0, 0

while True:
    print(p.x, p.y)
    p.aplicar_forca((-p.x, -p.y))
    p.aplicar_movimento()

    plt.ylim(-1, 1)
    plt.xlim(-1, 1)
    plt.gca().set_aspect('equal')

    plt.scatter(p.x, p.y, c='r')
    plt.draw()
    plt.pause(0.01)
    plt.clf()