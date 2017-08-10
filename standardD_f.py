#============================================================================
# Name        : standardD_f
# Author      : Yulieth Prieto
# Version     :
# Copyright   :
# Description : This program computes a function SD(A_00)(n,k), f(n,k)=mean(a_00)(n,k)/n
# Input	      : python standardD_f coef #size
#==============REMARKS=======================================================
#Change the path in "ruta".
#============================================================================

#LIBRARIES
import matplotlib.pyplot as plt
import sys
import numpy
import math
from struct import unpack
from math import pow
import numpy as np
import scipy.stats as stats

#INITIAL PARAMETERS
alpha=float(sys.argv[1])
coef=int(sys.argv[2])
ruta="/home/ykprieto/Dropbox/EXPERIMENTOS_TOTAL/"
#----------------------------------------------------------------------------------------------------
def Leer_archivo(name,pos):
	f=open(name,"r")
	lines=f.readlines()
	column=[]
	for x in lines:
		column.append(x.split(',')[pos])	#pos= columna pos (p.e 1=coeficiente A_00)
	f.close()
	coefficient=map(int, column)
	#print coefficient
	return coefficient
#----------------------------------------------------------------------------------------------------
#calcula SD and save in a matrix (size x pts)
vector_size=[50,100,200,300,500,1000]
vector_pts=[100,500,1000,1500,2000,2500,5000]
def vector_SD(coefi):
	vector_desviation=numpy.zeros((len(vector_size), len(vector_pts)))
	i=0
	j=0
	for size_i in vector_size:
		for pts_j in vector_pts: 
			name_file=ruta +"exp_"+str(size_i)+"_"+str(pts_j)+".txt"
			coefficient=Leer_archivo(name_file,coefi)
			vector_desviation[i][j]=np.std(coefficient)
			j=j+1
		i=i+1
		j=0
	return vector_desviation

#----------------------------------------------------------------------------------------------------
#calcula funcion SD fijando n
def function_f_k(s,alpha,vector_SD):		#function depends of k & fix n
	yPoint=[]
	for i in range (0,len(vector_pts)):
		yPoint=yPoint + [round(vector_SD[vector_size.index(s)][i], 5)]
	return yPoint
#----------------------------------------------------------------------------------------------------
def function_fR_k(s,alpha,vector_SD):		#function depends of k & fix n
	yPointR=[]	
	for i in range (0,len(vector_pts)):
		yPointR=yPointR + [round(vector_SD[vector_size.index(s)][i]/(s*math.pow(vector_pts[i],float(1)/float(alpha))), 5)]
	return yPointR
#----------------------------------------------------------------------------------------------------
def grafica_all_sizes(xPoint,y_50,y_100,y_200,y_300,y_500,y_1000,case):
	if case==0:		#case=0 is a power enteger
		plt.title(r'$\alpha=$'+ str(int(alpha))+".",fontsize=12)
	else:			#other case is an alpha-root	
		plt.title(r'$\alpha=$'+ str(int(float(1)/float(alpha)))+ r'$+ \epsilon$'+".",fontsize=12)
	plt.xlabel("p-random points")
	plt.ylabel(r'$f^{SD}_s$')
	plt.plot(xPoint, y_50, marker="o",linestyle="dashed", color="lightgrey",label="s=50.")
	plt.plot(xPoint, y_100, marker="o",linestyle="dashed", color="silver",label="s=100.")
	plt.plot(xPoint, y_200, marker="o",linestyle="dashed", color="gainsboro",label="s=200.")
	plt.plot(xPoint, y_300, marker="o",linestyle="dashed", color="darkgrey",label="s=300.")
	plt.plot(xPoint, y_500, marker="o",linestyle="dashed", color="dimgrey",label="s=500.")
	plt.plot(xPoint, y_1000, marker="o",linestyle="dashed", color="k",label="s=1000.")
	plt.legend(loc='best',ncol=2)
	plt.setp(plt.gca().get_legend().get_texts(), fontsize='8')
	dominio=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500]
	plt.xticks(dominio)
	if case==0:		#case=0 is a power enteger
		plt.savefig("./fSD_alpha"+str(int(alpha))+"_coef"+str(coef)+".pdf")
	else:			#other case is an alpha-root	
		plt.savefig("./fSD_alpharoot"+str(int(alpha))+"_coef"+str(coef)+".pdf")
	plt.show()
	plt.close()
#----------------------------------------------------------------------------------------------------	
Vector_SD=vector_SD(coef)
print Vector_SD
y_50=function_f_k(50,alpha,Vector_SD)
y_100=function_f_k(100,alpha,Vector_SD)
y_200=function_f_k(200,alpha,Vector_SD)
y_300=function_f_k(300,alpha,Vector_SD)
y_500=function_f_k(500,alpha,Vector_SD)
y_1000=function_f_k(1000,alpha,Vector_SD)
grafica_all_sizes(vector_pts,y_50,y_100,y_200,y_300,y_500,y_1000,0) 	

if alpha>0:
	y_50=function_fR_k(50,alpha,Vector_SD)
	y_100=function_fR_k(100,alpha,Vector_SD)
	y_200=function_fR_k(200,alpha,Vector_SD)
	y_300=function_fR_k(300,alpha,Vector_SD)
	y_500=function_fR_k(500,alpha,Vector_SD)
	y_1000=function_fR_k(1000,alpha,Vector_SD)
	grafica_all_sizes(vector_pts,y_50,y_100,y_200,y_300,y_500,y_1000,1)	




		
