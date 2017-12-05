'''
Reaproveitando mais uma vez o exemplo da bolinha:
crie um programa com a bolinha que desliza pela tela
e que contenha também uma plataforma, como se fosse
a raquete do jogo Pong. Essa plataforma nada mais é
do que um retângulo (pode ser na horizontal ou na
vertical). Quando a bola encostar na raquete, ela
deve quicar, assim como faz quando encosta na parede.
A raquete deve ser movimentada simplesmente
ao mover o ponteiro do mouse pela tela.
'''




from universe import *

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))


from namedlist import namedlist

Bolinha = namedlist("Bolinha", "x dx y dy raio pontos1")
'''
Bolinha eh criada como: Bolinha(Int+ Int Int+ Int)
interp. uma bolinha na posicao (x,y) e deslocamentos
dx e dy.
Ex:
'''
BOLA_INICIAL = Bolinha(100,3,100,3, 20,0)
BOLA2 = Bolinha(200,-3,200,3, 20,0)
'''Template para dados do tipo Bolinha:
def fn_para_bolinha(bola):
    ... bola.x
        bola.dx
        bola.y
        bola.dy
'''

Plataforma = namedlist("Plataforma", "x, tx, y, ty")
Plataforma2 = namedlist("Plataforma2", "x, tx, y, ty")
'''...'''

Jogo = namedlist("Jogo", "bolinha, plataforma,plataforma2,pontos1,pontos2")
'''...'''
JOGO_INICIAL = Jogo(BOLA_INICIAL, Plataforma(10,15,ALTURA//2,50),Plataforma2(570,15,ALTURA//2, 50,),0,0)



'''...'''
def move_bola(bolinha):
    # calcula novo dy
    if (bolinha.y == ALTURA and bolinha.dy > 0) \
            or (bolinha.y == 0 and bolinha.dy < 0):  # se vaca bateu na parede
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
            or (bolinha.x == 0 and bolinha.dx < 0):  # se vaca bateu na parede
        bolinha.dx = - bolinha.dx
    # usar depurador (debugger)

    # calcula novo y
    bolinha.x = bolinha.x + bolinha.dx

    if bolinha.x > LARGURA:
        bolinha.x = LARGURA
    elif bolinha.x < 0:
        bolinha.x = 0

    return bolinha


def colide(plataforma,plataforma2, bolinha):
    if (plataforma.x == bolinha.raio and plataforma.x <= bolinha.x + bolinha.x) or (plataforma.x + bolinha.raio >= bolinha.x and plataforma.x + 15 <= bolinha.x + bolinha.raio) :
        bolinha.dx = - bolinha.dx
    if (plataforma2.x == bolinha.raio and plataforma2.x <= bolinha.x + bolinha.x) or (plataforma2.x + bolinha.raio >= bolinha.x and plataforma2.x + 15 <= bolinha.x + bolinha.raio) :
        bolinha.dx = - bolinha.dx
    if (bolinha.x == 500):
        print("pontos")

def inverte(bola):
    bola.dx = -bola.dx


'''...'''
def move_jogo(jogo):
    if colide(jogo.plataforma,jogo.plataforma2, jogo.bolinha):
        inverte(jogo.bolinha)
        move_bola(jogo.bolinha)
    if colide(jogo.plataforma2,jogo.plataforma2, jogo.bolinha):
        inverte(jogo.bolinha)
    move_bola(jogo.bolinha)
    return jogo


'''...'''
def trata_mouse(jogo,x,y,me):
    if me == pg.MOUSEMOTION:
        plataforma = jogo.plataforma
        plataforma.y = y - \
                        (plataforma.ty)//2
    return jogo
'''...'''
def trata_tecla(jogo, tecla):
    if tecla == pg.K_UP:
        jogo.plataforma2.y += -20
    if tecla == pg.K_DOWN:
        jogo.plataforma2.y += 20
    return jogo

'''...'''
def desenha_jogo(jogo):
    pg.draw.rect(TELA,
                 (203, 230, 67),
                 (jogo.plataforma.x,
                  jogo.plataforma.y,
                  jogo.plataforma.tx,
                  jogo.plataforma.ty))
    pg.draw.rect(TELA,
                 (203, 230, 67),
                 (jogo.plataforma2.x,
                  jogo.plataforma2.y,
                  jogo.plataforma2.tx,
                  jogo.plataforma2.ty))
    pg.draw.circle(TELA,
                 (203, 230, 67),
                   (jogo.bolinha.x,
                    jogo.bolinha.y), jogo.bolinha.raio)
    fonte1 = pg.font.SysFont("Arial", 20)
    pontos1 = str(jogo.pontos1)
    pontos2 = str(jogo.pontos2)
    placar1 = fonte1.render('Jogador 1: {0}'.format(pontos1), 0, (0, 0, 0))
    placar2 = fonte1.render('Jogador 2: {0}'.format(pontos2), 0, (0, 0, 0))
    TELA.blit(placar1, (10, 10))
    TELA.blit(placar2, (480, 10))


def main(jogo):
    big_bang(jogo, tela=TELA,
             quando_tick=move_jogo,
             quando_mouse=trata_mouse,
             quando_tecla=trata_tecla,
             desenhar=desenha_jogo,
             modo_debug=True
            )

main(JOGO_INICIAL)