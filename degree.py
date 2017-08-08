# -*- coding: utf-8 -*-
#============================================================================
# Name        : degree.py
# Author      : Yulieth Prieto
# Version     :
# Copyright   : 
# Description : This program computes the minimal degree from 5000 experiments.
# Input	      : python degree.py pts size seed
#Output	      : the minimal degree alpha
#============================================================================

from struct import unpack
import numpy as np
import scipy.stats as stats
import os
import os.path
import sys
import math
from math import pow
import matplotlib.pyplot as plt
#----------------------------------------------------------------------------------------------------
alpha=float(sys.argv[1])
#ruta="/home/ykprieto/Dropbox/Algoritmos/"					#DIRECCION MI_COMPU
#ruta="/home/lupercio/ResultadosTotal/EXPERIMENTOS_TROPICAL/"			#DIRECCION XIU
ruta=ruta="/home/yprieto/"							#DIRECCION BUUUU	
vector_size=[50,100,200,300,500,1000]
vector_pts=[100,500,1000,1500,2000,2500,5000]
#vector_size=[50,100,200,300,500,1000,10000]
#vector_pts=[100,500,1000,1500,2000,2500,5000,200,400,10000,20000]
#----------------------------------------------------------------------------------------------------
def Crear_Degreetxt():
	name_file2="Degree.txt"
	with open(name_file2,"wb") as output:
		for s in vector_size:
			for p in vector_pts:
				vector_degree=[]
				if os.path.exists(ruta+str(s)+"x"+str(p))==True:
					for r in range(1,5001):
						name_file=ruta+str(s)+"x"+str(p)+"/active"+ str(p) +"pts_" + str(s) + "size_" + str(r)+"_experiment.dat"	#DIRECCION XIU y compu
						if os.path.isfile(name_file) and os.access(name_file, os.R_OK):
							with open(name_file,"rb") as input:
								pseqlen = unpack("i",input.read(4))[0]
								points = [(unpack("i",input.read(4))[0],unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]) for i in xrange(pseqlen )]
							vector_d=[]
							for k in range(0,len(points)):
								element=points[k]
								i=element[0]
								j=element[1]
								vector_d=vector_d+[i+j]					#grado de un polinomio tropical.
							vector_degree=vector_degree+[max(vector_d)]			#coleccion de todos los grados para los 5000 experimentos de un p y s fijos.
					if len(vector_degree)>0:				
						degree=min(vector_degree)				#escogencia del minimo grado apartir de los 5000 calculados. El definitivo para s y p fijos.
						degree_mean=int(round(np.mean(vector_degree)))			#degree promedio
						line= str(s)+","+str(p)+","+str(degree)+","+str(degree_mean)+'\n'
						print line
						output.write(line)						#cada linea guarda el grado para un s y p fijos.
				else:
					print str(s)+"x"+str(p)+": Folder isn't exist."
#Crear_Degreetxt()
#----------------------------------------------------------------------------------------------------
def Leer_archivo(name,s,pos):
	f=open(name,"r")
	lines=f.readlines()
	column=[]
	for x in lines:
		if x.split(',')[0]==str(s):
			column=column+[x.split(',')[pos]]			#pos= columna pos (p.e 0=size, 1=pts, 2=minimal_degree, 3=mean_degree)
	f.close()
	coefficient=map(int, column)
	#print coefficient
	return coefficient			
#----------------------------------------------------------------------------------------------------
def function_degree(s,vector_x,vector_p,alpha):		
	yPointR=[]	
	for i in range (0,len(vector_p)):		
		yPointR=yPointR + [round(vector_x[i]/(math.pow(s,0)*math.pow(vector_p[i],float(1)/float(alpha))), 5)]		#Dependiendo de s^algo
	return yPointR
#----------------------------------------------------------------------------------------------------
def grafica_all_sizes(x_50,x_100,x_200,x_300,x_500,x_1000,y_50,y_100,y_200,y_300,y_500,y_1000,case):
	if case==0:		#case=0 is MINIMAL DEGREE
		plt.title("Minimal degree of tropical polynomials")
	else:			#other case MEAN DEGREE	
		plt.title("Mean degree of tropical polynomials")
	plt.xlabel("p-random points")
	plt.ylabel(r'$f_s$')
	plt.plot(x_50, y_50, marker="o",linestyle="dashed", color="lightgrey",label="s=50.")
	plt.plot(x_100, y_100, marker="o",linestyle="dashed", color="silver",label="s=100.")
	plt.plot(x_200, y_200, marker="o",linestyle="dashed", color="gainsboro",label="s=200.")
	plt.plot(x_300, y_300, marker="o",linestyle="dashed", color="darkgrey",label="s=300.")
	plt.plot(x_500, y_500, marker="o",linestyle="dashed", color="dimgrey",label="s=500.")
	plt.plot(x_1000, y_1000, marker="o",linestyle="dashed", color="k",label="s=1000.")
	plt.legend(loc='best',ncol=2)
	plt.setp(plt.gca().get_legend().get_texts(), fontsize='8')
	dominio=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500]
	plt.xticks(dominio)
	if case==0:		#case=0 is MINIMAL DEGREE
		plt.savefig("/home/ykprieto/Dropbox/Algoritmos/Graficas_fun_mean/minimalDegree.pdf")
	else:			#other case is MEAN DEGREE
		plt.savefig("/home/ykprieto/Dropbox/Algoritmos/Graficas_fun_mean/meanDegree.pdf")
	plt.show()
	plt.close()
#----------------------------------------------------------------------------------------------------
#Dominio Ptos,minimal_degree,mean_degree
X_50=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",50,1) 			#PUNTOS
X2_50=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",50,2)			#MINIMAL_DEGREE
X3_50=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",50,3)			#MEAN_DEGREE

X_100=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",100,1)
X2_100=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",100,2)
X3_100=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",100,3)

X_200=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",200,1)
X2_200=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",200,2)
X3_200=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",200,3)

X_300=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",300,1)
X2_300=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",300,2)
X3_300=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",300,3)

X_500=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",500,1)
X2_500=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",500,2)
X3_500=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",500,3)

X_1000=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",1000,1)
X2_1000=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",1000,2)
X3_1000=Leer_archivo("/home/ykprieto/Dropbox/Algoritmos/Degree.txt",1000,3)

#Rango MINIMAL_DEGREE
Y_50=function_degree(50,X2_50,X_50,alpha)
Y_100=function_degree(100,X2_100,X_100,alpha)
Y_200=function_degree(200,X2_200,X_200,alpha)
Y_300=function_degree(300,X2_300,X_300,alpha)
Y_500=function_degree(500,X2_500,X_500,alpha)
Y_1000=function_degree(1000,X2_1000,X_1000,alpha)
grafica_all_sizes(X_50,X_100,X_200,X_300,X_500,X_1000,Y_50,Y_100,Y_200,Y_300,Y_500,Y_1000,0)
#Rango MEAN_DEGREE
Y_50=function_degree(50,X3_50,X_50,alpha)
Y_100=function_degree(100,X3_100,X_100,alpha)
Y_200=function_degree(200,X3_200,X_200,alpha)
Y_300=function_degree(300,X3_300,X_300,alpha)
Y_500=function_degree(500,X3_500,X_500,alpha)
Y_1000=function_degree(1000,X3_1000,X_1000,alpha)
grafica_all_sizes(X_50,X_100,X_200,X_300,X_500,X_1000,Y_50,Y_100,Y_200,Y_300,Y_500,Y_1000,1)


