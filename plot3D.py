# -*- coding: utf-8 -*-
#==============================================================================================================
# Name        : tropical_curves.py
# Author      : Yulieth Prieto
# Version     :
# Copyright   : 
# Description : This program displays a polytope of a polynomial tropical
# Input       : python plot3D.py N 
#		(size of domain= N, vectores con las entradas i, j y los coeficientes Cij)
#==============================================================================================================
from Tkinter import *
from struct import unpack
import Image, ImageDraw
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
N=int(sys.argv[1])		#size of domain
#v_i=[0,-1,0,0,1]		#vector with coeficients of x
#v_j=[0,0,-1,1,0]		#vector with coeficients of y
#v_Cij=[5,N,N,0,0]		#constants
#v_i=[1,0,-1,0,0]		
#v_j=[0,1,0,-1,0]		
#v_Cij=[0,0,1,1,0.33]		
#v_i=[1,0,-1,0,0,2]		#Ejm.
#v_j=[0,1,0,-1,0,0]		
#v_Cij=[0.133,0,1,1,0.33,0]		
v_i=[-2, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3]	#Ejm.
v_j=[0, -1, 0, 1, 2, -3, -2, -1, 0, 1, 2, 3, 4, 5, -2, -1, 0, 1, 2, 3, -1, 0, 1, 0]
v_Cij=[200, 200, 112, 100, 100, 300, 208, 130, 61, 24, 12, 5, 2, 0, 200, 100, 25, 0, 0, 0, 100, 4, 0, 0]
def monomio(i, j, x, y, c):
   return round((i*x + j*y + c),3)

def curve_trop(x,y):
	vmonomios=[]
	for l in range(len(v_i)):
		vmonomios=vmonomios+[monomio(v_i[l],v_j[l],x,y,v_Cij[l])]
	min_vmonomios=min(vmonomios)
	#min_vmonomios=max(vmonomios)
	#print vmonomios.count(min_vmonomios)
	return vmonomios.count(min_vmonomios)

def z(x,y):
	vmonomios=[]
	for l in range(len(v_i)):
		vmonomios=vmonomios+[monomio(v_i[l],v_j[l],x,y,v_Cij[l])]
	min_vmonomios=min(vmonomios)
	return round(min_vmonomios,4)

def graficar(x,y,z,bx,by,bz):
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	#ax.scatter(x,y,z,'filled')
	plt.axis('off')
	ax.scatter(x,y,z,color='k',alpha = 0.10)
	#ax.plot_wireframe(x, y, z,color="k")
	ax.scatter(bx,by,bz,color='k')
	#ax.plot_wireframe(bx, by, bz,color="red")
	plt.savefig("Piramide_tropical_curve.pdf",bbox_inches='tight', pad_inches=0)
	plt.show()

#PERFECT SCALE FOR PETIT PICTURES
#x_Points=np.arange(0, N,0.01)
#y_Points=np.arange(0, N,0.0005)
#PERFECT SCALE FOR BIG PICTURES
x_Points=np.arange(0, N,0.8)
y_Points=np.arange(0, N,0.5)

X=[]
Y=[]
Z=[]

for x in x_Points:
	for y in x_Points:
		if 0<curve_trop(x,y)<2:
			X=X+[x]
			Y=Y+[y]
			Z=Z+[z(x,y)]
bondx=[]
bondy=[]
bondz=[]
for x in y_Points:
	for y in y_Points:
		if curve_trop(x,y)>=2:
			bondx=bondx+ [x]
			bondy=bondy+ [y]
			bondz=bondz+ [z(x,y)]

graficar(X,Y,Z,bondx,bondy,bondz)
