from __future__ import division
from __future__ import print_function

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from math import floor, sin, cos


def key_callback(window, key, scancode, action, mode):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        print("closed window for pressing Escape key")
        glfw.set_window_should_close(window, True)
def reshape_callback(window, width, height):
    glViewport(0,0,width, height)


def setpixel(x,y,color):
    glColor3fv(color)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()


def drawAxes():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glVertex2f(0,-200)
    glVertex2f(0,200)
    glEnd()

def translate2D(point, T):
    x_new = point[0] + T[0]
    y_new = point[1] + T[1]
    return (x_new, y_new)

def main():
    if not glfw.init():
        raise Exception("glfw cannot be initialised.......")

    window=glfw.create_window(700,700, "rotation 2D",None,None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window not created")

    w,h = glfw.get_framebuffer_size(window)
    print("width: {}, height:{}".format(w,h))

    glfw.set_window_pos(window, 400,40)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glfw.set_window_size_callback(window, reshape_callback)

    gluOrtho2D(-200.0, 200.0,-200.0,200.0)
    setpixel(0,0,[1,0,1])

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        #glClearColor(0.0,0.76,0.56,1.0)
        glClearColor(0,0,0,1.0)

        drawAxes()



        a =(20,20)
        b = (20, 80)
        c=(80,20)

        glBegin(GL_TRIANGLES)
        glColor3f(0,0,1)
        glVertex2fv(a)
        glColor3f(0,1,0)
        glVertex2fv(b)
        glColor3f(1,0,0)
        glVertex2fv(c)
        glEnd()

        #translate traingle vertices 100 units along x-dir

        T = (100,0)
        A_new = translate2D(a, T)
        B_new = translate2D(b, T)
        C_new = translate2D(c,T)

        glBegin(GL_TRIANGLES)
        glColor3f(0,0,1)
        glVertex2fv(A_new)
        glColor3f(0,1,0)
        glVertex2fv(B_new)
        glColor3f(1,0,0)
        glVertex2fv(C_new)
        glEnd()

        #translate traingle vertices 100 units along x-dir

        T = (0,100)
        A_new = translate2D(a, T)
        B_new = translate2D(b, T)
        C_new = translate2D(c,T)

        glBegin(GL_TRIANGLES)
        glColor3f(0,0,1)
        glVertex2fv(A_new)
        glColor3f(0,1,0)
        glVertex2fv(B_new)
        glColor3f(1,0,0)
        glVertex2fv(C_new)
        glEnd()

        T = (100,100)
        A_new = translate2D(a, T)
        B_new = translate2D(b, T)
        C_new = translate2D(c,T)

        glBegin(GL_TRIANGLES)
        glColor3f(0,0,1)
        glVertex2fv(A_new)
        glColor3f(0,1,0)
        glVertex2fv(B_new)
        glColor3f(1,0,0)
        glVertex2fv(C_new)
        glEnd()

        glfw.swap_buffers(window)

        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
        
        
        
