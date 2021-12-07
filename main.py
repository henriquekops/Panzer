#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.floor import Floor
from src.player import Player
from src.wall import Cell, Wall
from src.projectile import Projectile
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

floor: Floor
player: Player
wall: Wall


def init():
    """
    Initialize opengl parameters
    """
    global floor, player, wall

    glClearColor(0.5, 0.5, 0.5, 1.0)
    glClearDepth(1.0) 
    glDepthFunc(GL_LESS)
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
    if h == 0:
        h = 1
    aspect_ratio = w / h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, w, h)

    player.set_position(aspect_ratio)


def set_light():
    """
    Set light system
    """
    LuzAmbiente = [0.4, 0.4, 0.4] 
    LuzDifusa   = [0.7, 0.7, 0.7]
    LuzEspecular = [0.9, 0.9, 0.9]
    PosicaoLuz0  = [2.0, 3.0, 0.0 ]
    Especularidade = [1.0, 1.0, 1.0]
    glEnable ( GL_COLOR_MATERIAL )
    glEnable(GL_LIGHTING)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, LuzAmbiente)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LuzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LuzDifusa  )
    glLightfv(GL_LIGHT0, GL_SPECULAR, LuzEspecular  )
    glLightfv(GL_LIGHT0, GL_POSITION, PosicaoLuz0 )
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glMaterialfv(GL_FRONT,GL_SPECULAR, Especularidade)
    glMateriali(GL_FRONT,GL_SHININESS,51)


def display():
    """
    Display everything
    """
    global player

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    set_light()
    glMatrixMode(GL_MODELVIEW)
    
    player.set_position(aspect_ratio)
    floor.draw()
    wall.draw()
    player.draw()

    p: Projectile
    for p in player.projectiles:
        if p.delete:
            player.projectiles.remove(p)
        else:
            p.draw()
            cell: Cell
            for cell in wall.cells:
                # p.collision(cell)
                if p.collision(cell):
                    cell.destroy()
    
    if player.cooldown > 0:
        player.cooldown -= 1
    
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
    
    if AccumDeltaT > 1.0/30:  
        AccumDeltaT = 0
        glutPostRedisplay()


def keyboard(*args):
    """
    Hanlde keyboard 
    """
    global player

    if args[0] == ESCAPE:
        os._exit(0)
    if args[0] == b' ':
        if player.cooldown == 0:
            player.shoot()
            player.cooldown = 50
    if args[0] == b'w':
        if player.alpha_aim > -25:
            player.alpha_aim -= 1
    if args[0] == b's':
        if player.alpha_aim < 5:
            player.alpha_aim += 1

    glutPostRedisplay()


def arrow_keys(a_keys: int, x: int, y: int):
    """
    Handle arrow keys
    """
    if a_keys == GLUT_KEY_UP:
        player.forward()
    if a_keys == GLUT_KEY_DOWN:
        player.backward()
    if a_keys == GLUT_KEY_LEFT:
        player.left()
    if a_keys == GLUT_KEY_RIGHT:
        player.right()

    glutPostRedisplay()


if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(650, 500)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Panzer")
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