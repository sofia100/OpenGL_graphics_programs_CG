from __future__ import division
from __future__ import print_function

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from math import floor


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


def main():
    if not glfw.init():
        raise Exception("glfw nt initialized")

    window=glfw.create_window(512,512, "Clipping",None,None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window not created")

    w,h = glfw.get_framebuffer_size(window)
    print("width: {}, height:{}".format(w,h))

    glfw.set_window_pos(window, 400,200)

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glfw.set_window_size_callback(window, reshape_callback)

    gluOrtho2D(0, 512, 0, 512)
    setpixel(0,0,[1,0,1])

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        #glClearColor(0.0,0.76,0.56,1.0)
        glClearColor(1,1,1,1.0)

        A = (300, 300) 
        B = (650, 450) #clipped
        #B=(250, 450) #not clipped
        C = (350, 500)

        glBegin(GL_TRIANGLES)
        glColor3f(0,0,1)
        glVertex2fv(A)
        glColor3f(0,1,0)
        glVertex2fv(B)
        glColor3f(1,0,0)
        glVertex2fv(C)
        glEnd()

        D = (250, 250)
        E =(1, 300) #not clipped
        F= (40, 450) #not clipped
        G = (-40, 100) #clipped

        glLineWidth(4)
        
        glBegin(GL_LINES)
        glColor3f(0,0,1)
        glVertex2fv(D)
        glColor3f(0,1,1)
        glVertex2fv(E)
        glEnd()

        
        glBegin(GL_LINES)
        glColor3f(0,0,1)
        glVertex2fv(D)
        glColor3f(1,0,1)
        glVertex2fv(G)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0,0,1)
        glVertex2fv(D)
        glColor3f(1,0,0)
        glVertex2fv(F)
        glEnd()
        
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ =="__main__":
    main()

# cohen-sutherland algo is not written coz opengl
# handles it in background . even polygon clipping
# is also handled
        

        


