# -*- coding: utf-8 -*-
#===============================================================================
# Name        : compare_pictures.py
# Author      : Yulieth Prieto.
# Version     :
# Copyright   : 
# Description : This program calculates a percentage of similitude from two .dat
#               of tropical and usual sandpiles.
# Input       : python visualizegridlinearsandpile_2.py size pts seed
#===============================================================================
import sys
import numpy as np
from Tkinter import *
from struct import unpack
import matplotlib.pyplot as plt
#===============================================================================
size=sys.argv[1]
pts=sys.argv[2]
seed=sys.argv[3]
#===============================================================================
im1 = "/home/ykprieto/Dropbox/Algoritmos/Algoritmos_principales/imagenes_Tropical/grid_"+pts+"pts_"+size+"size_"+seed+"_experiment.dat"
im2 = "/home/ykprieto/Dropbox/Algoritmos/Algoritmos_principales/imagenes_Sandpiles/gridSand_"+pts+"pts_"+size+"size_"+seed+"_experiment.dat"

def vector_tropical():
	curva=[]
	with open(im1,"rb") as input:
		n = unpack("i",input.read(4))[0]
		nunstable = unpack("i",input.read(4))[0]
		nmonomials = unpack("i",input.read(4))[0]
		monomials = [ [unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]] for i in xrange(nmonomials)]
		unstable = [ [unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]] for i in xrange(nunstable)]
	curva=curva+unstable+monomials
	#print curva
	return curva	

def vector_sandpile():
	curva=[]
	with  open(im2,"rb") as input:
		n = unpack("i",input.read(4))[0]
		nunstable = unpack("i",input.read(4))[0]
		grid = [ [unpack("i",input.read(4))[0] for i in xrange(n)] for j in xrange(n) ]
		curva =curva+ [ [unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]] for i in xrange(nunstable)]	
	for i in xrange(n):
		for j in xrange(n):
			if grid[i][j]==2 or grid[i][j]==1 or grid[i][j]==0 or grid[i][j]>3:
				curva=curva+[[i,j]]
	#print curva
	return curva
def similitud_images(c1,c2):				#REMARK:LA MATRIZ QUE ARROJA ES LA TRANSPUESTA A LA ASOC A LA IMAGEN. 1:COINCIDEN 0:NO COINCIDE.
	A=np.ones((int(size),int(size)))
	#print A
	for x in c1:
		i=x[0]
		j=x[1]
		if x not in c2:
			A[i][j]=0
	for x in c2:
		i=x[0]
		j=x[1]
		if x not in c1:
			A[i][j]=0
	print str(int(100*(sum(sum(A))/float(int(size)*int(size)))))+"% de similitud"
	#archi=open("/home/ykprieto/Dropbox/Algoritmos/similitudes_"+size+"size.txt",'a')
	archi=open("/home/ykprieto/Dropbox/Algoritmos/similitudes_"+pts+"pts.txt",'a')
	archi.write(str(sum(sum(A))/float(int(size)*int(size)))+",");
	archi.close()

#curvS=vector_sandpile()
#curvT=vector_tropical()
#similitud_images(curvT,curvS)

#================================================================================
def Leer_archivo(name):
	f=open(name,"r")
	lines=f.readlines()
	print str(lines[0])
	vector=map(float,lines[0].split(','))
	f.close()
	return vector
#Analisis puntos
#v_percentage=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/similitudes_"+size+"size.txt")
#v_points=np.arange(1,int(pts)+1)
#plt.plot(v_points, v_percentage, 'black', marker='.',ls='-')
#plt.xlabel("Number of random points")

#Analisis size
v_percentage=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/similitudes_"+pts+"pts.txt")
v_size=np.arange(5,int(size)+1)
plt.plot(v_size, v_percentage, 'black', marker='.',ls='-')
plt.xlabel("Size of square")

plt.grid("on")
plt.ylabel("m")
plt.show()

	
