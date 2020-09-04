# -*- coding: utf-8 -*-
'''
Created on Sun Jan 12 13:47:53 2020

@author: Stian B. Soeisdal

Content: First algorithm on the 2 by 2 matrices
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Test that the positive trace-preserving maps are CPT maps
def CPTtest(a):
    for i in range(len(a)):
        eq = 0
        if (abs(a[i,3,3])+abs(a[i,3,0])) -1.0 == 0.0:
            if a[i,1,0] == 0:
                if a[i,2,0] == 0:
                    eq = 4
                else:
                    print('T_{} do not hold 1. and 2.'.format(i+1))
            else:
                print('T_{} do not hold 1. and 2.'.format(i+1))
        else:
            eq1 = 0
            eq1_1 = (a[i,1,1]+a[i,2,2])**2
            eq1_2 = ((1+a[i,3,3])**2 - a[i,3,0]**2
                     - (a[i,1,0]**2+a[i,2,0]**2)*(1+a[i,3,3]+a[i,3,0])/(1-a[i,3,3]+a[i,3,0]))
            eq1_2m= ((1+a[i,3,3])**2 - a[i,3,0]**2
                     - (a[i,1,0]**2+a[i,2,0]**2)*(1+a[i,3,3]-a[i,3,0])/(1-a[i,3,3]-a[i,3,0]))
            eq1_3 = (1+a[i,3,3])**2-a[i,3,0]**2
            if eq1_1 <= eq1_2:
                if eq1_2 <= eq1_3:
                    eq += 1
                    eq1+= 1
            if eq1_1 <= eq1_2m:
                if eq1_2m <= eq1_3:
                    eq += 1
                    eq1+= 1
            if eq1 != 2:
                print('T_{} do not hold 1.'.format(i+1))
            eq2 = 0
            eq2_1 = (a[i,1,1]-a[i,2,2])**2
            eq2_2 = ((1-a[i,3,3])**2 - a[i,3,0]**2
                     - (a[i,1,0]**2+a[i,2,0]**2)*(1-a[i,3,3]+a[i,3,0])/(1+a[i,3,3]+a[i,3,0]))
            eq2_2m= ((1-a[i,3,3])**2 - a[i,3,0]**2
                     - (a[i,1,0]**2+a[i,2,0]**2)*(1-a[i,3,3]-a[i,3,0])/(1+a[i,3,3]-a[i,3,0]))
            eq2_3 = (1-a[i,3,3])**2-a[i,3,0]**2
            if eq2_1 <= eq2_2:
                if eq2_2 <= eq2_3:
                    eq += 1
                    eq2+= 1
            if eq2_1 <= eq2_2m:
                if eq2_2m <= eq2_3:
                    eq += 1
                    eq2+= 1
            if eq2 != 2:
                print('T_{} do not hold 2.'.format(i+1))
        eq3_1 = (1-a[i,1,1]**2-a[i,2,2]**2-a[i,3,3]**2-a[i,1,0]**2-a[i,2,0]**2-a[i,3,0]**2)**2
        subeq1= (a[i,1,1]**2)*(a[i,1,0]**2+a[i,2,2]**2)
        subeq2= (a[i,2,2]**2)*(a[i,2,0]**2+a[i,3,3]**2)
        subeq3= (a[i,3,3]**2)*(a[i,3,0]**2+a[i,1,1]**2)
        eq3_2 = 4*(subeq1+subeq2+subeq3-2*a[i,1,1]*a[i,2,2]*a[i,3,3])
        if eq3_1 >= eq3_2:
            if eq == 4:
                print('T_{} is CPT'.format(i+1))
        else:
            print('T_{} do not hold 3.'.format(i+1))

def SystemOnM2(a, x, y, z, it, pltit=' ', savpng=0):
    # Plot layout
    plot_layout = np.array([111,121,131,221,220,321])
    figsizx = np.array([2.0,4.0,6.0,4.0,4.0,4.0])
    figsizy = np.array([2.1,2.1,2.1,4.2,4.2,6.3])
    
    # Show the density matrices
    Su = np.linspace(0, 2 * np.pi, 100)
    Sv = np.linspace(0, np.pi, 50)
    Sx = np.outer(np.cos(Su), np.sin(Sv))
    Sy = np.outer(np.sin(Su), np.sin(Sv))
    Sz = np.outer(np.ones(np.size(Su)), np.cos(Sv))
    
    # Pre-Iteration:
    fig = plt.figure(figsize=(figsizx[it],figsizy[it]))
    fig.suptitle(pltit, fontsize=16)
    if it != 4:
        ax = fig.add_subplot(plot_layout[it], projection='3d')
        plt.title('Initial set'), ax.view_init(20, 10)
        ax.set_xlim3d([-1, 1]), ax.set_ylim3d([-1, 1]), ax.set_zlim3d([-1, 1])
        #ax.set_xlim3d([-0.7,0.1]), ax.set_ylim3d([-0.25,0.25]), ax.set_zlim3d([0,0.8])
        ax.plot_surface(Sx, Sy, Sz, color=(1.,0.,0.,.1))
        ax.plot_surface(x, y, z, color=(0.1,0.4,1.,0.95))
    
    # System setup
    sys, An = len(a), np.zeros_like(a)
    for i in range(sys):
        An[i] = np.matrix([[1.0, 0, 0, 0],
                           [0.0, 1, 0, 0],
                           [0.0, 0, 1, 0],
                           [0.0, 0, 0, 1]])
    for n in range(it):
        # Setup plot to iteration
        ax = fig.add_subplot(plot_layout[it]+n+1, projection='3d')
        plt.title('Iteration {}'.format(n+1)), ax.view_init(20, 10)
        ax.set_xlim3d([-1, 1]), ax.set_ylim3d([-1, 1]), ax.set_zlim3d([-1, 1])
        #ax.set_xlim3d([-0.7,0.1]), ax.set_ylim3d([-0.25,0.25]), ax.set_zlim3d([0,0.8])
        ax.plot_surface(Sx, Sy, Sz, color=(1.,0.,0.,.1))
        
        # Allocate new maps
        An = np.repeat(An, sys, axis=0)
        
        # Update maps
        for k in range(sys**(n+1)):
            k_re = np.remainder(k,sys)
            Ak = An[k]
            An[k] = np.matmul(a[k_re], Ak)
            
            # Plot next map
            Px = An[k,1,1]*x + An[k,1,2]*y + An[k,1,3]*z + An[k,1,0]
            Py = An[k,2,1]*x + An[k,2,2]*y + An[k,2,3]*z + An[k,2,0]
            Pz = An[k,3,1]*x + An[k,3,2]*y + An[k,3,3]*z + An[k,3,0]
            ax.plot_surface(Px, Py, Pz, color=(0.1,0.4,1.,0.95))
    
    plt.subplots_adjust(top=0.83, bottom=0.05, left=0.10,
                        right=0.95, hspace=0.25, wspace=0.15)
    if savpng != 0:
        plt.savefig(savpng, dpi = 200)
    plt.show()
    

if __name__ =='__main__':
    # Number of iterations that are plotted
    itr = 3
    # -----------------Systems-----------------
    '''
    plttit = 'System generating \n the Cantor set'
    r = 0.334
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [0.0, 0, r, 0],
                             [1-r, 0, 0, r]]),
                  np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [0.0, 0, r, 0],
                             [r-1, 0, 0, r]])])
    savefile = 'Fig_M2_1.png'
    '''
    
    plttit = 'System generating \n the Sierpinski tetrahedron'
    r = 1/2
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [0.0, 0, r, 0],
                             [1-r, 0, 0, r]]),
                  np.matrix([[1.0,                  0, 0, 0],
                             [(1-r)*np.sqrt(8./9.), r, 0, 0],
                             [0.0,                  0, r, 0],
                             [(r-1)/3.,             0, 0, r]]),
                  np.matrix([[1.0,                  0, 0, 0],
                             [(r-1)*np.sqrt(2./9.), r, 0, 0],
                             [(1-r)*np.sqrt(2./3.), 0, r, 0],
                             [(r-1)/3.,             0, 0, r]]),
                  np.matrix([[1.0,                  0, 0, 0],
                             [(r-1)*np.sqrt(2./9.), r, 0, 0],
                             [(r-1)*np.sqrt(2./3.), 0, r, 0],
                             [(r-1)/3.,             0, 0, r]])])
    savefile = 'Fig_M2_2.png'
    
    '''
    plttit = 'System generating \n the Sierpinski triangle'
    r = 1/2
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [0.0, 0, r, 0],
                             [1-r, 0, 0, r]]),
                  np.matrix([[1.0,                  0, 0, 0],
                             [(1-r)*np.sqrt(8./9.), r, 0, 0],
                             [0.0,                  0, r, 0],
                             [(r-1)/3.,             0, 0, r]]),
                  np.matrix([[1.0,                  0, 0, 0],
                             [(r-1)*np.sqrt(2./9.), r, 0, 0],
                             [(1-r)*np.sqrt(2./3.), 0, r, 0],
                             [(r-1)/3.,             0, 0, r]])])
    savefile = 'Fig_M2_3.png'
    '''
    '''
    plttit = 'System generating \n the Sierpinski octahedron'
    r = 1/2
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [0.0, 0, r, 0],
                             [1-r, 0, 0, r]]),
                  np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [0.0, 0, r, 0],
                             [r-1, 0, 0, r]]),
                  np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [1-r, 0, r, 0],
                             [0.0, 0, 0, r]]),
                  np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [r-1, 0, r, 0],
                             [0.0, 0, 0, r]]),
                  np.matrix([[1.0, 0, 0, 0],
                             [1-r, r, 0, 0],
                             [0.0, 0, r, 0],
                             [0.0, 0, 0, r]]),
                  np.matrix([[1.0, 0, 0, 0],
                             [r-1, r, 0, 0],
                             [0.0, 0, r, 0],
                             [0.0, 0, 0, r]])])
    savefile = 'Fig_M2_4.png'
    '''
    '''
    plttit = 'Fern attractor positivity test'
    t = 0.900116 #0.90086
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, 0, 0, 0],
                             [0.0, 0, 0.18, 0],
                             [0.0, 0, 0, 0]]),
                  np.matrix([[1.0,    0, 0, 0],
                             [0.0, 0.85, 0, 0],
                             [0.16*t, 0, np.sqrt(293)/20, 0],
                             [0.0,    0, 0, np.sqrt(293)/20]]),
                  np.matrix([[1.0,    0, 0, 0],
                             [0.0,    np.sqrt(2)/5, 0, 0],
                             [0.08*t, 0, np.sqrt(2)/5, 0],
                             [0.0,    0, 0, 0.3]]),
                  np.matrix([[1.0,    0, 0, 0],
                             [0.0,   -np.sqrt(2)/5, 0, 0],
                             [0.08*t, 0, np.sqrt(2)/5, 0],
                             [0.0,    0, 0, 0.3]])])
    
    '''
    '''
    plttit = 'System generating \n a Fern attractor'
    t = 0.900116
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, 1e-3, 0, 0],
                             [0.0, 0, 1e-3, 0],
                             [0.0, 0, 0, 0.18]]),
                  np.matrix([[1.0,    0,    0,    0],
                             [0.0,    0.85, 0,   -0.1],
                             [0.0,    0,    0.85, 0],
                             [0.16*t, 0.1,  0,    0.85]]),
                  np.matrix([[1.0,    0,   0,   0],
                             [0.0,    0.3, 0,   0],
                             [0.0,    0,   0.2,-0.2],
                             [0.08*t, 0,   0.2, 0.2]]),
                  np.matrix([[1.0,    0,   0,   0],
                             [0.0,    0.3, 0,   0],
                             [0.0,    0,  -0.2, 0.2],
                             [0.08*t, 0,   0.2, 0.2]])])
    savefile = 'Fig_M2_5-.png'
    '''
    # -----------------Inital set-----------------
    
    # Standard, start with the unit ball
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 50)
    X = np.outer(np.cos(u), np.sin(v))
    Y = np.outer(np.sin(u), np.sin(v))
    Z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    '''
    # Tetrahedron inside the unit ball
    u = np.linspace(0, 2 * np.pi, 4)
    v = np.array([0, 3*np.pi/5])
    X = np.outer(np.cos(u), np.sin(v))
    Y = np.outer(np.sin(u), np.sin(v))
    Z = np.outer(np.ones(np.size(u)), np.cos(v))
    '''
    '''
    # Octahedron inside the unit ball
    u = np.linspace(0, 2 * np.pi, 5)
    v = np.linspace(0, np.pi, 3)
    X = np.outer(np.cos(u), np.sin(v))
    Y = np.outer(np.sin(u), np.sin(v))
    Z = np.outer(np.ones(np.size(u)), np.cos(v))
    '''
    '''
    # For fern
    r_s = 0.15
    u = np.linspace(0, 2 * np.pi, 5)
    v = np.linspace(0, np.pi, 4)
    
    X = r_s*np.outer(np.cos(u), np.sin(v))
    Y = r_s*np.outer(np.sin(u), np.sin(v))
    Z = 2*r_s*np.outer(np.ones(np.size(u)), np.cos(v))+3/10
    '''
    SystemOnM2(A, X, Y, Z, itr, plttit, savefile)
    #CPTtest(A)