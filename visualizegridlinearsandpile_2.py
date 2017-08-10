# -*- coding: utf-8 -*-
#============================================================================
# Name        : visualizegrid.py
# Author      : Yulieth Prieto.
# Version     :
# Copyright   : 
# Description : This program saves a graphical representation of the output
#               of linearsandpile
# Input       : python visualizegridlinearsandpile_2.py size pts seed
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
ruta="/home/ykprieto/Dropbox/Algoritmos/Algoritmos_principales/imagenes_Tropical/"
n=1
nunstable=1
delta=1
monomials=[]
unstable=[]
def draw_image():
	plt.axis('on')
	plt.grid('on')
	for [i,j] in monomials:
        	plt.plot(i,j,'o',markersize=6,linestyle='-',color="black")
	for [i,j] in unstable:
        	#plt.plot(i,j,'o',markersize=6,linestyle='-',color="yellow")
     		plt.plot(i,j,'o',markersize=10,linestyle='-',color="grey")
	plt.savefig(ruta+"grid_"+pts +"pts_"+size+"size_"+seed+"_experiment.pdf")
    	plt.show()


if __name__ == "__main__":
    with  open(ruta+"grid_"+ pts +"pts_" + size + "size_" + seed+"_experiment.dat","rb") as input:
        n = unpack("i",input.read(4))[0]
        nunstable = unpack("i",input.read(4))[0]
        nmonomials = unpack("i",input.read(4))[0]
        monomials = [ [unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]] for i in xrange(nmonomials)]
        unstable = [ [unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]] for i in xrange(nunstable)]
	print unstable
	print monomials	
	draw_image()
