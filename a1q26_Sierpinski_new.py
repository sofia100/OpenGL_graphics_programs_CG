from __future__ import division
from __future__ import print_function

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math 

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

def divide_triangle(a1,a2, b1,b2, c1,c2,  m):
     if m>0 :
       v01=(a1+b1)/2
       v02=(a2+b2)/2
       v11=(a1+c1)/2
       v12=(a2+c2)/2
       v21=(c1+b1)/2
       v22=(c2+b2)/2
       
       divide_triangle(a1,a2, v01,v02, v11,v12, m-1)
       divide_triangle(c1,c2, v11,v12, v21,v22, m-1)
       divide_triangle(b1,b2, v21,v22, v01,v02, m-1)
     
     else :
       one_triangle(a1,a2, b1,b2, c1,c2)

def one_triangle(a1,a2, b1,b2, c1,c2):
    glVertex2fv((a1,a2));
    glVertex2fv((b1,b2));
    glVertex2fv((c1,c2));

def main():
    if not glfw.init():
        raise Exception("glfw nt initialized")

    window=glfw.create_window(600,600, "B117049- Sierpinski Triangles",None,None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window not created")

    w,h = glfw.get_framebuffer_size(window)
    print("width: {}, height:{}".format(w,h))

    glfw.set_window_pos(window, 350,85)

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glfw.set_window_size_callback(window, reshape_callback)

    gluOrtho2D(-400,400,-60,400)

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        #glClearColor(0.0,0.76,0.56,1.0)
        glClearColor(1,1,1,1.0)

        glBegin(GL_TRIANGLES);
        glColor3f(1,0,0) 
        divide_triangle(0,300,-300,0,300,0, 4)
        glEnd()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ =="__main__":
    main()
