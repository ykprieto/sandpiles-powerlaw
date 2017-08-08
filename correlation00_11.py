#============================================================================
# Name        : correlation00_11
# Author      : Yulieth Prieto
# Version     :
# Copyright   :
# Description : This program computes a relation between a_00 and a_11
# Input	      : python correlation00_11.py
#============================================================================

#LIBRARIES
import matplotlib.pyplot as plt
import sys
import numpy
import math
from struct import unpack
from math import pow
from math import log
import numpy as np
import scipy.stats as stats
from scipy.stats.stats import pearsonr   

#INITIAL PARAMETERS
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
vector_size=[50,100,200,300,500,1000]
vector_pts=[100,500,1000,1500,2000,2500,5000]
def vector_mean(coefi):
	vector_average=numpy.zeros((len(vector_size), len(vector_pts)))
	i=0
	j=0
	for size_i in vector_size:
		for pts_j in vector_pts: 
			name_file=ruta +"exp_"+str(size_i)+"_"+str(pts_j)+".txt"
			coefficient=Leer_archivo(name_file,coefi)
			vector_average[i][j]=sum(coefficient)/float(len(coefficient))
			j=j+1
		i=i+1
		j=0
	#print vector_average
	return vector_average
#----------------------------------------------------------------------------------------------------
def function_0011(s,vector_average,vector_average2):		#function depends of k & fix n
	yPointR=[]	
	for i in range (0,len(vector_pts)):		
		yPointR=yPointR + [round(vector_average[vector_size.index(s)][i]-(vector_average2[vector_size.index(s)][i]), 9)]
	return yPointR
#----------------------------------------------------------------------------------------------------
def function_Log0011(s,vector_average,vector_average2):		#function depends of k & fix n
	yPointR=[]	
	for i in range (0,len(vector_pts)):		#(s*math.pow(vector_pts[i],1./alpha))
		yPointR=yPointR + [round(math.log(vector_average[vector_size.index(s)][i]/(vector_average2[vector_size.index(s)][i]), 9))]
	return yPointR
#----------------------------------------------------------------------------------------------------
def grafica_all_sizes(xPoint,y_50,y_100,y_200,y_300,y_500,y_1000,case):
	if case==0:		#case=0 is normal
		plt.title(r'$f_s(p)=c_{00}-c_{11}$')
	else:			#other case is correlation function	
		plt.title("Correlation")
	plt.grid(True)		
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
	if case==0:		#case=0 is normal
		plt.savefig("/home/ykprieto/Dropbox/Algoritmos/Graficas_fun_mean/f0011.pdf",bbox_inches='tight', pad_inches=0)
	else:			#other case is log function
		plt.savefig("/home/ykprieto/Dropbox/Algoritmos/Graficas_fun_mean/f0011corr.pdf",bbox_inches='tight', pad_inches=0)
	plt.show()
	plt.close()
#correlation between c00 y c11-----------------------------------------------------------------------
def correlation(s,case0,case1):
	vector_corr=[]
	for j in range(0,len(vector_pts)):
		name_file=ruta +"exp_"+str(s)+"_"+str(vector_pts[j])+".txt"
		c_00=Leer_archivo(name_file,case0)
		c_11=Leer_archivo(name_file,case1)
		corr=pearsonr(c_00, c_11)
		vector_corr=vector_corr+[round(corr[0],3)]
	return vector_corr
corr_50=correlation(50,1,5)
corr_100=correlation(100,1,5)
corr_200=correlation(200,1,5)
corr_300=correlation(300,1,5)
corr_500=correlation(500,1,5)
corr_1000=correlation(1000,1,5)
grafica_all_sizes(vector_pts,corr_50,corr_100,corr_200,corr_300,corr_500,corr_1000,1) 	
#----------------------------------------------------------------------------------------------------
vector_00=vector_mean(1)
vector_11=vector_mean(5)
y_50=function_0011(50,vector_00,vector_11)
y_100=function_0011(100,vector_00,vector_11)
y_200=function_0011(200,vector_00,vector_11)
y_300=function_0011(300,vector_00,vector_11)
y_500=function_0011(500,vector_00,vector_11)
y_1000=function_0011(1000,vector_00,vector_11)
grafica_all_sizes(vector_pts,y_50,y_100,y_200,y_300,y_500,y_1000,0) 	
#Aplicar Log
#y_50=function_Log0011(50,vector_00,vector_11)
#y_100=function_Log0011(100,vector_00,vector_11)
#y_200=function_Log0011(200,vector_00,vector_11)
#y_300=function_Log0011(300,vector_00,vector_11)
#y_500=function_Log0011(500,vector_00,vector_11)
#y_1000=function_Log0011(1000,vector_00,vector_11)
#grafica_all_sizes(vector_pts,y_50,y_100,y_200,y_300,y_500,y_1000,1) 
	


