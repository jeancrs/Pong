'''
Projete um programa mundo que consiste em uma bolinha (ou partícula) que se mova em velocidade constante
pela tela. A bola deve poder se mover tanto no eixo x quanto no eixo y. Quando a bola atinge
os limites (beiradas) da tela, ela deve "quicar", isto é, não deve sair fora da tela e deve continuar
se movendo na direção correta (imagine o que acontece com uma bola que quica no chão diagonalmente).
DICA1: Inspire-se no exemplo da vaca. No entanto, lembre-se que aqui o eixo y (assim como o deslocamento
no eixo y) deve ser considerado.
DICA2: A direção da bolinha deve ser definifa no estado inicial passado à função main.
DICA3: Veja como funciona um jogo de Arkanoid para entender a dinâmica da bola na tela: https://www.youtube.com/watch?v=Th-Z6QQ5AOQ
DICA3: Trabalhem cuidadosamente na análise de domínio e nos exemplos. Este exercicio não é tão
simples como pode parecer.
'''




from universe import *

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))



from namedlist import namedlist

Bolinha = namedlist("Bolinha", "x dx y dy raio")
'''
Bolinha eh criada como: Bolinha(Int+ Int Int+ Int)
interp. uma bolinha na posicao (x,y) e deslocamentos
dx e dy.
Ex:
'''
BOLA_INICIAL = Bolinha(100,3,100,3, 20)
'''Template para dados do tipo Bolinha:
def fn_para_bolinha(bola):
    ... bola.x
        bola.dx
        bola.y
        bola.dy
'''




'''...'''
def move_bola(bolinha):
    # calcula novo dy
    if (bolinha.y == ALTURA and bolinha.dy > 0) or (bolinha.y == 0 and bolinha.dy < 0):  # se vaca bateu na parede
        bolinha.dy = - bolinha.dy

    # usar depurador (debugger)

    # calcula novo y
    bolinha.y = bolinha.y + bolinha.dy

    if bolinha.y > ALTURA:
        bolinha.y = ALTURA
    elif bolinha.y < 0:
        bolinha.y = 0

    # calcula novo dy
    if (bolinha.x == LARGURA and bolinha.dx > 0) \
                or (bolinha.x == 0 and jogol.bolinha.dx < 0):  # se vaca bateu na parede
            bolinha.dx = - bolinha.dx
        # usar depurador (debugger)

    # calcula novo y
    bolinha.x = bolinha.x + bolinha.dx

    if bolinha.x > LARGURA:
        bolinha.x = LARGURA
    elif bolinha.x < 0:\
        bolinha.x = 0


    return bolinha


def inverte(bola):
    bola.dx = -bola.dx


'''...'''
def mover(bolinha):
    move_bola(bolinha)
    return bolinha



'''...'''
def desenha(bolinha):
    pg.draw.circle(TELA,
                 (203, 230, 67),
                   (bolinha.x,
                    bolinha.y), bolinha.raio)


def main(BOLA_INICIAL):
    big_bang(BOLA_INICIAL, tela=TELA,
             quando_tick=mover,
             desenhar=desenha,
            )

main(BOLA_INICIAL)