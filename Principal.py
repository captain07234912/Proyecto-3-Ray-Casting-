import sys
from pygame.locals import *
from pygame import mixer
from RayCaster import *

"""
Universidad del Valle de Guatemala
Graficas por computadora
Principal
Jorge Suchite 
Carnet 15293
08/11/2020
Proyecto No. 3 Ray Casting
"""
pygame.init()
pygame.display.set_caption(' Blizzard Inc.')
screen = pygame.display.set_mode((1000, 500), pygame.DOUBLEBUF | pygame.HWACCEL)  # , pygame.FULLSCREEN)
screen.set_alpha(None)
clock = pygame.time.Clock()
mainClock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

#mixer.music.load('BobIntro.mp3')
#mixer.music.play(1)


mixer.music.load('BobLoop.mp3')
mixer.music.play(500)


def updateFPS():
    fps = str(int(clock.get_fps()))
    fps = font.render(fps, 1, pygame.Color("white"))
    return fps


r = Raycaster(screen)

def escribir(text, size, color, surface, x, y):
    font = pygame.font.Font(pygame.font.match_font('comicsansms'), size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def inicio():
    click = False

    fondoBikini = pygame.image.load('imagenes/fondo.jpg')
    fondoBikini = pygame.transform.rotozoom(fondoBikini, 0, 1.2)
    fondo = fondoBikini.get_rect()
    fondo.center = 400, 250

    btnPlay = pygame.Rect(600, 200, 250, 75)
    btnSalir = pygame.Rect(625, 300, 200, 50)


    while True:

        screen.blit(fondoBikini, fondo)
        escribir('¡Fondo de Bikini!', 50, (0, 0, 0), screen, 500, 50)

        pygame.draw.rect(screen, (255, 242, 0), btnPlay)
        pygame.draw.rect(screen, (255, 242, 0), btnSalir)

        escribir('Jugar', 35, (0, 0, 0), screen, 675, 215)
        escribir('Salir', 30, (0, 0, 0), screen, 685, 305)

        mx, my = pygame.mouse.get_pos()

        if btnPlay.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 128, 128), btnPlay)
            escribir('Jugar', 35, (255, 255, 255), screen, 675, 215)
            if click:
                niveles()
        if btnSalir.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 128, 128), btnSalir)
            escribir('Salir', 30, (255, 255, 255), screen, 685, 305)
            if click:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #screen.fill((0, 0, 0))
        pygame.display.update()
        mainClock.tick(60)


def niveles():
    click = False


    fondoBikini = pygame.image.load('imagenes/fondo.jpg')
    fondoBikini = pygame.transform.rotozoom(fondoBikini, 0, 1.2)
    fondo = fondoBikini.get_rect()
    fondo.center = 400, 250

    btn1 = pygame.Rect(600, 200, 200, 50)
    btn2 = pygame.Rect(600, 300, 200, 50)
    btn3 = pygame.Rect(600, 400, 200, 50)

    isRunning = True
    while isRunning:

        screen.blit(fondoBikini, fondo)
        escribir('¡Fondo de Bikini!', 50, (0, 0, 0), screen, 500, 50)

        pygame.draw.rect(screen, (255, 242, 0), btn1)
        pygame.draw.rect(screen, (255, 242, 0), btn2)
        pygame.draw.rect(screen, (255, 242, 0), btn3)

        escribir('Nivel 1', 25, (0, 0, 0), screen, 660, 210)
        escribir('Nivel 2', 25, (0, 0, 0), screen, 660, 305)
        escribir('Nivel 3', 25, (0, 0, 0), screen, 660, 400)

        mx, my = pygame.mouse.get_pos()

        if btn1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 128, 128), btn1)
            escribir('Nivel 1', 25, (255, 255, 255), screen, 660, 210)
            if click:
                Jugar(1)
                screen.fill((0, 0, 0))


        elif btn2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 128, 128), btn2)
            escribir('Nivel 2', 25, (255, 255, 255), screen, 660, 305)
            if click:
                Jugar(2)
        elif btn3.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 128, 128), btn3)
            escribir('Nivel 3', 25, (255, 255, 255), screen, 660, 400)
            if click:
                Jugar(3)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    isRunning = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def Jugar(nivel):
    if (nivel ==1):
        r.load_map('fondoDeBikini.txt')
        r.player['x'] = 425
        r.player['y'] = 425
    elif (nivel ==2):
        r.load_map('CrustaceoCascarudo.txt')
        r.player['x'] = 75
        r.player['y'] = 425
    elif (nivel ==3):
        r.player['x'] = 250
        r.player['y'] = 250
        r.load_map('CasaDeArenita.txt')

    isRunning = True
    while isRunning:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isRunning = False

            newX = r.player['x']
            newY = r.player['y']

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    isRunning = False
                elif ev.key == pygame.K_UP:
                    newX += cos(r.player['angle'] * pi / 180) * r.stepSize
                    newY += sin(r.player['angle'] * pi / 180) * r.stepSize
                elif ev.key == pygame.K_DOWN:
                    newX -= cos(r.player['angle'] * pi / 180) * r.stepSize
                    newY -= sin(r.player['angle'] * pi / 180) * r.stepSize
                elif ev.key == pygame.K_LEFT:
                    newX -= cos((r.player['angle'] + 90) * pi / 180) * r.stepSize
                    newY -= sin((r.player['angle'] + 90) * pi / 180) * r.stepSize
                elif ev.key == pygame.K_RIGHT:
                    newX += cos((r.player['angle'] + 90) * pi / 180) * r.stepSize
                    newY += sin((r.player['angle'] + 90) * pi / 180) * r.stepSize
                elif ev.key == pygame.K_a:
                    r.player['angle'] -= 5
                elif ev.key == pygame.K_d:
                    r.player['angle'] += 5

                i = int(newX / r.blocksize)
                j = int(newY / r.blocksize)

                if r.map[j][i] == ' ':
                    r.player['x'] = newX
                    r.player['y'] = newY

        screen.fill(pygame.Color("gray"))  # Fondo

        # Techo
        screen.fill(pygame.Color("saddlebrown"), (int(r.width / 2), 0, int(r.width / 2), int(r.height / 2)))

        # Piso
        screen.fill(pygame.Color("dimgray"), (int(r.width / 2), int(r.height / 2), int(r.width / 2), int(r.height / 2)))

        r.render()

        # FPS
        screen.fill(pygame.Color("black"), (0, 0, 30, 30))
        screen.blit(updateFPS(), (0, 0))
        clock.tick(30)

        pygame.display.update()

inicio()

pygame.quit()
