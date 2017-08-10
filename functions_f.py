#============================================================================
# Name        : function mean
# Author      : Yulieth Prieto
# Version     :
# Copyright   :
# Description : This program computes a function mean(coef)(n,k), f(n,k)=mean(coef)(n,k)/n
# Input	      : python function_f alpha coef #size
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
#======REMARKS======================================================================================================
#Change the path in "ruta" where is the total of experiments: exp_size_pts.txt
#===================================================================================================================
#INITIAL PARAMETERS
alpha=float(sys.argv[1])
coef=int(sys.argv[2])
#n=int(sys.argv[3])
#pts=sys.argv[2]
ruta="/home/ykprieto/Dropbox/EXPERIMENTOS_TOTAL/"

def Leer_archivo(name,pos):
	f=open(name,"r")
	lines=f.readlines()
	column=[]
	for x in lines:
		column.append(x.split(',')[pos])			#pos= columna pos (p.e 1=coeficiente A_00)
	f.close()
	coefficient=map(int, column)
	return coefficient
#----------------------------------------------------------------------------------------------------
#calcula mean or average and save in a matrix (size x pts)
vector_size=[50,100,200,300,500,1000]
#pos_vector_size=vector_size.index(n)
vector_pts=[100,500,1000,1500,2000,2500,5000]
def vector_mean(coefi):
	vector_average=numpy.zeros((len(vector_size), len(vector_pts)))
	#vector_desviation=numpy.zeros((len(vector_size), len(vector_pts)))
	i=0
	j=0
	for size_i in vector_size:
		for pts_j in vector_pts: 
			name_file=ruta +"exp_"+str(size_i)+"_"+str(pts_j)+".txt"
			coefficient=Leer_archivo(name_file,coefi)
			vector_average[i][j]=sum(coefficient)/float(len(coefficient))
			#vector_desviation[i][j]=np.std(coefficient)
			j=j+1
		i=i+1
		j=0
	#print vector_average
	return vector_average
	#return vector_desviation

#----------------------------------------------------------------------------------------------------
#Calcuate mean function for an alpha and an alpha-root.
def function_f_k(m,alpha,vector_average):		
	yPoint=[]
	for i in range (0,len(vector_pts)):
		yPoint=yPoint + [round(vector_average[vector_size.index(m)][i]/(m*math.pow(vector_pts[i],alpha)), 9)]
	return yPoint
#----------------------------------------------------------------------------------------------------
def function_fR_k(m,alpha,vector_average):		
	yPointR=[]	
	for i in range (0,len(vector_pts)):
		yPointR=yPointR + [round(vector_average[vector_size.index(m)][i]/(m*math.pow(vector_pts[i],float(1)/float(alpha))), 9)]
	#print yPointR
	return yPointR
#----------------------------------------------------------------------------------------------------
#Grafica
def graficar(xPoint,yPoint,case):
	if case==0:		#case=0 is a power enteger
		plt.title(r'$\alpha=$'+ str(alpha)+' and n='+str(n)+'.')
	else:			#other case is an alpha-root	
		plt.title(r'$\frac{1}{\alpha}=$'+ str(alpha)+" and n ="+str(n)+".")
	plt.xlabel("k-random points")
	plt.ylabel("f")
	plt.plot(xPoint, yPoint, marker="o",linestyle="dashed", color="k")
	dominio=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000]
	plt.xticks(dominio)
	if case==0:		#case=0 is a power enteger
		plt.savefig(ruta+"f_alpha"+str(alpha)+ "_size"+str(n) +"_coef"+str(coef)+".pdf")
	else:			#other case is an alpha-root	
		plt.savefig(ruta+"f_alpharoot"+str(alpha)+"_size"+ str(n) +"_coef"+str(coef)+".pdf")
	plt.close()
	#plt.show()
def grafica_all_sizes(xPoint,y_50,y_100,y_200,y_300,y_500,y_1000,case):
	if case==0:		#case=0 is a power enteger
		plt.title(r'$\alpha=$'+ str(alpha)+".")
	else:			#other case is an alpha-root	
		plt.title(r'$\alpha=1.85$'+".",fontsize=12)
	plt.xlabel("p-random points")
	plt.ylabel(r'$f_s$')
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
		plt.savefig(ruta+"fmean_alpha"+str(int(alpha))+"_coef"+str(int(coef))+".pdf")
		#plt.savefig("/home/ykprieto/Dropbox/Algoritmos/Graficas_fun_mean/fDE_alpha"+str(alpha)+"_coef"+str(coef)+".pdf")
	else:			#other case is an alpha-root	
		plt.savefig(ruta+"fmean_alpharoot"+str(int(alpha))+"_coef"+str(int(coef))+".pdf")
		#plt.savefig("/home/ykprieto/Dropbox/Algoritmos/Graficas_fun_mean/fDE_alpharoot"+str(alpha)+"_coef"+str(coef)+".pdf")
	plt.show()
	plt.close()
	
#yPoint=function_f_k(n,alpha)
#graficar(vector_pts,yPoint,0)
Vector_average=vector_mean(coef)
print Vector_average
y_50=function_f_k(50,alpha,Vector_average)
y_100=function_f_k(100,alpha,Vector_average)
y_200=function_f_k(200,alpha,Vector_average)
y_300=function_f_k(300,alpha,Vector_average)
y_500=function_f_k(500,alpha,Vector_average)
y_1000=function_f_k(1000,alpha,Vector_average)
#grafica_all_sizes(vector_pts,y_50,y_100,y_200,y_300,y_500,y_1000,0) 	

if alpha>0:
	#yPointR=function_fR_k(n,alpha)
	#graficar(vector_pts,yPointR,1)
	y_50=function_fR_k(50,alpha,Vector_average)
	y_100=function_fR_k(100,alpha,Vector_average)
	y_200=function_fR_k(200,alpha,Vector_average)
	y_300=function_fR_k(300,alpha,Vector_average)
	y_500=function_fR_k(500,alpha,Vector_average)
	y_1000=function_fR_k(1000,alpha,Vector_average)
	grafica_all_sizes(vector_pts,y_50,y_100,y_200,y_300,y_500,y_1000,1) 	
#<a_00-a_11>	
	Vector_average1=vector_mean(1)-vector_mean(5)
	#print Vector_average1
	y_50=function_fR_k(50,alpha,Vector_average1)
	y_100=function_fR_k(100,alpha,Vector_average1)
	y_200=function_fR_k(200,alpha,Vector_average1)
	y_300=function_fR_k(300,alpha,Vector_average1)
	y_500=function_fR_k(500,alpha,Vector_average1)
	y_1000=function_fR_k(1000,alpha,Vector_average1)
	coef=0011
	#grafica_all_sizes(vector_pts,y_50,y_100,y_200,y_300,y_500,y_1000,0) 	




		
