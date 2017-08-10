# -*- coding: utf-8 -*-
#============================================================================
# Name        : visualizegrid.py
# Author      : Yulieth Prieto.
# Version     :
# Copyright   : 
# Description : This program saves a graphical representation of the output
#               of sandpile_usual
# Input       : python visualizegrid2.py size pts seed
#==============REMARKS==========================================================
#Change the path in "ruta".
#============================================================================
from Tkinter import *
from struct import unpack
import Image, ImageDraw
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
size=sys.argv[1]
pts=sys.argv[2]
seed=sys.argv[3]
ruta="/home/ykprieto/Dropbox/Algoritmos/Algoritmos_principales/imagenes_Sandpiles/"
n=1
nunstable=1
monomials=[]
unstable=[]
def draw_image():
	plt.axis('on')
	plt.grid('on')
	for i in xrange(n):
		for j in xrange(n):
		    print i,j,grid[i][j]
		    if grid[i][j]==2:
			plt.plot(i,j,'o',markersize=6,color="black",linestyle='-')
		    if grid[i][j]==1:
			plt.plot(i,j,'o',markersize=6,color="black",linestyle='-')
		    if grid[i][j]==0:
			plt.plot(i,j,'o',markersize=6,color="black",linestyle='-')
		    if grid[i][j]>3:
			plt.plot(i,j,'o',markersize=6,color="black",linestyle='-')
	    	    if [i,j] in unstable:
	     		plt.plot(i,j,'o',linestyle='-',markersize=10,color="grey")
	plt.savefig(ruta+"sandpile_"+size +"_"+pts+"pt_"+seed+"experiment.pdf")
	plt.show()

if __name__ == "__main__":
    with  open(ruta+"gridSand_"+ pts +"pts_" + size + "size_" + seed+"_experiment.dat","rb") as input:
        n = unpack("i",input.read(4))[0]
        nunstable = unpack("i",input.read(4))[0]
        grid = [ [unpack("i",input.read(4))[0] for i in xrange(n)] for j in xrange(n) ]
        unstable = [ [unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]] for i in xrange(nunstable)]
	draw_image()
