from __future__ import division
from __future__ import print_function

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def key_callback(window, key, scancode, action, mode):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        print("closed window for pressing Escape key")
        glfw.set_window_should_close(window, True)
def reshape_callback(window, width, height):
    glViewport(0,0,width, height)

def translate2D(point, T):
    x_new = point[0] + T[0]
    y_new = point[1] + T[1]
    return (x_new, y_new)

def setpixel(x,y,color):
    glColor3fv(color)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def quad_(a,b,c,d):
    glBegin(GL_QUADS)
    glColor3f(1,1,1) #white
    glVertex2fv(a)
    glVertex2fv(b)
    glVertex2fv(c)
    glVertex2fv(d)
    glEnd()

def main():
    if not glfw.init():
        raise Exception("glfw nt initialized")

    window=glfw.create_window(512,512, "B117021 - OpenGL",None,None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window not created")

    w,h = glfw.get_framebuffer_size(window)
    print("width: {}, height:{}".format(w,h))

    glfw.set_window_pos(window, 400,200)

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glfw.set_window_size_callback(window, reshape_callback)

    gluOrtho2D(0,512,512,0)

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.0,0.0,0.0,1.0)

        a=(20, 500)
        b=(40, 500)
        c= (40,355)
        d=(20, 355)
        quad_(a,b,c,d )
        
        T = (95,0)
        a_ = translate2D(a, T)
        b_ = translate2D(b, T)
        c_ = translate2D(c,T)
        d_ = translate2D(d,T)
        quad_(a_,b_,c_,d_ )

        p=(40,415)
        q=(135,415)
        r=(135, 435)
        s=(40,435)
        quad_(p,q,r,s)

        e=(160, 220)
        f=(220,250)
        g=(220,165)
        h=(160,150)
        quad_(e,f,g,h)

        i=(128,150)
        j=(150,155)
        k=(150,175)
        l=(125,165)
        quad_(i,j,k,l)

        m=(115,205)
        n=(115,140)
        o=(55,125)
        o_=(55,175)
        quad_(m,n,o,o_)

        u=(230,250)
        v=(330,190)
        w=(330,130)
        x=(230,165)
        quad_(u,v,w,x)

        p1=(330,125)
        p2=(295,95)
        p3=(235,155)
        glBegin(GL_TRIANGLES)
        glColor3f(1,1,1) #white
        glVertex2fv(p1)
        glVertex2fv(p2)
        glVertex2fv(p3)
        glEnd()

        p5=(120,60)
        p6=(290,90)
        p7=(225,155)
        p8=(60,113)
        quad_(p5,p6,p7,p8)

        glfw.swap_buffers(window)
        glfw.poll_events()
        

    glfw.terminate()

if __name__ =="__main__":
    main()
