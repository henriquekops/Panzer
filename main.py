#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.floor import Floor

# external dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

__author__ = ["Henrique Kops", "Gabriel Castro"]
__credits__ = "Marcio Pinho"

Angulo = 0.0
nFrames, TempoTotal, AccumDeltaT = 0, 0, 0
oldTime = time.time()
ESCAPE = b'\x1b'

floor = Floor()

def init():
    """
    Initialize opengl parameters
    """
    # Define a cor do fundo da tela (BRANCO) 
    glClearColor(0.5, 0.5, 0.5, 1.0)
    
    glEnable(GL_DEPTH_TEST)
    glEnable (GL_CULL_FACE )
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


def reshape(w: int, h: int):
    """
    Treat screen reshaping
    """
    global AspectRatio
	# Evita divisÃ£o por zero, no caso de uam janela com largura 0.
    if h == 0:
        h = 1
    # Ajusta a relaÃ§Ã£o entre largura e altura para evitar distorÃ§Ã£o na imagem.
    # Veja funÃ§Ã£o "PosicUser".
    AspectRatio = w / h
	# Reset the coordinate system before modifying
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Seta a viewport para ocupar toda a janela
    glViewport(0, 0, w, h)
    
    PosicUser()


def DefineLuz():
    """
    Set light system
    """
    # Define cores para um objeto dourado
    LuzAmbiente = [0.4, 0.4, 0.4] 
    LuzDifusa   = [0.7, 0.7, 0.7]
    LuzEspecular = [0.9, 0.9, 0.9]
    PosicaoLuz0  = [2.0, 3.0, 0.0 ]  # PosiÃ§Ã£o da Luz
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

 
def PosicUser():
    """
    Position user
    """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #print ("AspectRatio", AspectRatio)
    gluPerspective(40,AspectRatio,0.01,50) # Projecao perspectiva
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 4, 10, 0,0,0, 0,1.0,0.0) 


def display():
    """
    Display everything
    """
    global Angulo
    # Limpa a tela com  a cor de fundo
    glClear(GL_COLOR_BUFFER_BIT)

    DefineLuz()
    PosicUser()

    glMatrixMode(GL_MODELVIEW)
    
    floor.draw()

    glColor3f(0.5,0.0,0.0) # Vermelho
    glPushMatrix()
    glTranslatef(-2,0,0)
    glRotatef(Angulo,0,1,0)
    DesenhaCubo()
    glPopMatrix()
    
    glColor3f(0.5,0.5,0.0) # Amarelo
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(-Angulo,0,1,0)
    DesenhaCubo()
    glPopMatrix()

    Angulo = Angulo + 1

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
        pass
    if a_keys == GLUT_KEY_DOWN:       # Se pressionar DOWN
        pass
    if a_keys == GLUT_KEY_LEFT:       # Se pressionar LEFT
        pass
    if a_keys == GLUT_KEY_RIGHT:      # Se pressionar RIGHT
        pass

    glutPostRedisplay()


def mouse(button: int, state: int, x: int, y: int):
    """
    Handle mouse
    """
    glutPostRedisplay()

def mouseMove(x: int, y: int):
    """
    Handle mouse move
    """
    glutPostRedisplay()

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(650, 500)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("OpenGL 3D")
    init ()
    glutDisplayFunc(display)
    glutIdleFunc (animate)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(arrow_keys)

    #glutMouseFunc(mouse)
    #glutMotionFunc(mouseMove)

    try:
        glutMainLoop()
    except SystemExit:
        pass