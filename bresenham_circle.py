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

def reflectpoints(x,y,colour):
    setpixel((x), (-y), colour)
    setpixel((-x), (y), colour)
    setpixel((-x), (-y), colour)
    setpixel((-y), (-x), colour)
    setpixel((y), (-x), colour)
    setpixel((y), (x), colour)
    setpixel((-y), (x), colour)
    
    
def BresenhamCircle(xc,yc,r, colour):
    x=0
    y=r
    d=3-2*r  #d=d0 initially

    while x<=y:
        setpixel(xc+x, yc+y, colour)
        reflectpoints(xc+x, yc+y, colour)
        
        if d <0:
            d=d+ 4*x  +6
        else:
            d=d+ 4*(x-y) +10
            y=y-1

        x=x+1


def main():
    if not glfw.init():
        raise Exception("glfw nt initialized")

    window=glfw.create_window(480,480, "Midpoint Circle Algorithm",None,None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window not created")

    w,h = glfw.get_framebuffer_size(window)
    print("width: {}, height:{}".format(w,h))

    glfw.set_window_pos(window, 400,200)

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glfw.set_window_size_callback(window, reshape_callback)

    gluOrtho2D(-200.0, 200.0,-200.0,200.0)
    setpixel(0,0,[1,0,1])

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        #glClearColor(0.0,0.76,0.56,1.0)
        glClearColor(1,1,1,1.0)
        setpixel((0), (0), [1,0,0])

        BresenhamCircle(0,0,150, [1,0,1])
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ =="__main__":
    main()
