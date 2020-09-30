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

def drawAxes():
    glColor3f(0,0,1)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(0,-50000)
    glVertex2f(0,40000000)
    glEnd()

def setpixel(x,y,color):
    glColor3fv(color)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def quartic(x):
    return (x**4)-(5*(x**3))+(x*x)-(3*x)-1

def main():
    if not glfw.init():
        raise Exception("glfw nt initialized")

    window=glfw.create_window(700,700, "B117049- Quartic Function",None,None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window not created")

    w,h = glfw.get_framebuffer_size(window)
    print("width: {}, height:{}".format(w,h))

    glfw.set_window_pos(window, 400,45)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_window_size_callback(window, reshape_callback)
    gluOrtho2D(-80.0,80,-400000.0,40000000.0)

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        #glClearColor(0.0,0.76,0.56,1.0)
        glClearColor(1,1,1,1.0)
        drawAxes()

        for i in range(-79, 79,1):
            y=quartic(i)
            setpixel(i,y,(1,0,0))
   
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ =="__main__":
    main()
