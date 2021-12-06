#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.floor import Floor
from src.player import Player
from src.wall import Wall
from src.common.texture import load

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time


__author__ = ["Henrique Kops", "Gabriel Castro"]
__credits__ = "Marcio Pinho"

angle = 0.0
aspect_ratio= 0.0
nFrames, TempoTotal, AccumDeltaT = 0, 0, 0
oldTime = time.time()
ESCAPE = b'\x1b'

floor, player, wall = None, None, None


def init():
    """
    Initialize opengl parameters
    """
    global floor, player, wall

    glClearColor(0.5, 0.5, 0.5, 1.0)
    glClearDepth(1.0) 
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    #    
    glEnable(GL_DEPTH_TEST)
    glEnable (GL_CULL_FACE )
    glEnable(GL_TEXTURE_2D)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    tex = load('./static/textures/rock-tile-2.jpg')

    floor = Floor(25, 50)
    player = Player(12.0, 0.0)
    wall = Wall(tex)
    wall.build(25, 10, 25)


def reshape(w: int, h: int):
    """
    Handle screen reshaping
    """
    global aspect_ratio
	# Evita divisÃ£o por zero, no caso de uam janela com largura 0.
    if h == 0:
        h = 1
    # Ajusta a relaÃ§Ã£o entre largura e altura para evitar distorÃ§Ã£o na imagem.
    # Veja funÃ§Ã£o "PosicUser".
    aspect_ratio = w / h
	# Reset the coordinate system before modifying
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Seta a viewport para ocupar toda a janela
    glViewport(0, 0, w, h)
    
    player.set_position(aspect_ratio)


def set_light():
    """
    Set light system
    """
    # Define cores para um objeto dourado
    LuzAmbiente = [0.4, 0.4, 0.4] 
    LuzDifusa   = [0.7, 0.7, 0.7]
    LuzEspecular = [0.9, 0.9, 0.9]
    PosicaoLuz0  = [2.0, 3.0, 0.0 ]
    Especularidade = [1.0, 1.0, 1.0]

    # ****************  Fonte de Luz 0

    glEnable ( GL_COLOR_MATERIAL )

    #Habilita o uso de iluminaÃ§Ã£o
    glEnable(GL_LIGHTING)

    #Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, LuzAmbiente)
    # Define os parametros da luz nÃºmero Zero
    glLightfv(GL_LIGHT0, GL_AMBIENT, LuzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LuzDifusa  )
    glLightfv(GL_LIGHT0, GL_SPECULAR, LuzEspecular  )
    glLightfv(GL_LIGHT0, GL_POSITION, PosicaoLuz0 )
    glEnable(GL_LIGHT0)

    # Ativa o "Color Tracking"
    glEnable(GL_COLOR_MATERIAL)

    # Define a reflectancia do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, Especularidade)

    # Define a concentraÃ§Ã£oo do brilho.
    # Quanto maior o valor do Segundo parametro, mais
    # concentrado serÃ¡ o brilho. (Valores vÃ¡lidos: de 0 a 128)
    glMateriali(GL_FRONT,GL_SHININESS,51)


def DesenhaCubo():
    """
    Draw cube
    """
    glutSolidCube(1)


def display():
    """
    Display everything
    """
    global angle
    # Limpa a tela com  a cor de fundo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    set_light()
    player.set_position(aspect_ratio)

    glMatrixMode(GL_MODELVIEW)
    
    floor.draw()
    wall.draw()

    # glColor3f(0.5,0.0,0.0) # Vermelho
    # glPushMatrix()
    # glTranslatef(-2,0,0)
    # glRotatef(angle,0,1,0)
    # DesenhaCubo()
    # glPopMatrix()
    
    # glColor3f(0.5,0.5,0.0) # Amarelo
    # glPushMatrix()
    # glTranslatef(2,0,0)
    # glRotatef(-angle,0,1,0)
    # DesenhaCubo()
    # glPopMatrix()

    angle = angle + 1

    glutSwapBuffers()


def animate():
    """
    Idle statistics
    """
    global nFrames, TempoTotal, AccumDeltaT, oldTime

    nowTime = time.time()
    dt = nowTime - oldTime
    oldTime = nowTime

    AccumDeltaT += dt
    TempoTotal += dt
    nFrames += 1
    
    if AccumDeltaT > 1.0/30:  # fixa a atualizaÃ§Ã£o da tela em 30
        AccumDeltaT = 0
        glutPostRedisplay()


def keyboard(*args):
    """
    Hanlde keyboard 
    """
    if args[0] == ESCAPE:   # Termina o programa qdo
        os._exit(0)         # a tecla ESC for pressionada

    if args[0] == b' ':
        init()

    glutPostRedisplay()


def arrow_keys(a_keys: int, x: int, y: int):
    """
    Handle arrow keys
    """
    if a_keys == GLUT_KEY_UP:         # Se pressionar UP
        player.forward()
    if a_keys == GLUT_KEY_DOWN:       # Se pressionar DOWN
        player.backward()
    if a_keys == GLUT_KEY_LEFT:       # Se pressionar LEFT
        player.left()
    if a_keys == GLUT_KEY_RIGHT:      # Se pressionar RIGHT
        player.right()

    glutPostRedisplay()


if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(650, 500)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("OpenGL 3D")
    glutDisplayFunc(display)
    glutIdleFunc (animate)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(arrow_keys)
    init ()

    try:
        glutMainLoop()
    except SystemExit:
        pass