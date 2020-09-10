from __future__ import division
from __future__ import print_function

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from math import floor
import random

def key_callback(window, key, scancode, action, mode):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        print("closed window for pressing Escape key")
        glfw.set_window_should_close(window, True)
        
def reshape_callback(window, width, height):
    glViewport(0,0,width, height)

def setpixel(x,y,color,s):
    glPointSize(s)
    glColor3fv(color)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def random_point():
    return x,y,(r,g,b)
    
def main():
    if not glfw.init():
        raise Exception("glfw nt initialized")

    window=glfw.create_window(640,480, "B117049 - Random Points, Colours and Sizes",None,None)

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
    x=[]
    y=[]
    r=[]
    g=[]
    b=[]
    size=[]
    
    for i in range (0,10,1):
        x.append(random.randint(-200,200))
        y.append(random.randint(-200,200))   
        r.append(random.randint(0,256)/256)
        g.append(random.randint(0,256)/256)
        b.append(random.randint(0,256)/256)
        size.append(random.randint(3,20))
        print("x= ", x[i], " y= ",y[i],"colour=(", r[i],",",g[i],",",b[i],") ", "size=",size[i])

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1,1,1,1.0)
 
        for i in range(0,10,1):    
            setpixel(x[i], y[i], (r[i],g[i],b[i]), size[i])

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ =="__main__":
    main()
