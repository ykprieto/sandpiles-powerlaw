#============================================================================
# Name        : info_onecoefficient
# Author      : Yulieth Prieto
# Version     :
# Copyright   :
# Description : This program computes a info of one coef
# Input	      : python info_onecoefficient size pts coef
#============================================================================
import sys
from struct import unpack
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pylab 
import math 
from math import sin, cos, pi
from scipy import integrate
size=int(sys.argv[1])
pts=sys.argv[2]
coef=int(sys.argv[3])
ruta="/home/ykprieto/Dropbox/EXPERIMENTOS_TOTAL/Sin_modificiar-exp/"

#archivo con la info del coeficiente----------------------------------------------------------------------------------------------------------
def Leer_archivo(name,pos):
	f=open(name,"r")
	lines=f.readlines()
	column=[]
	for x in lines:
		column.append(x.split(',')[pos])			#pos= columna pos (p.e 1=coeficiente A_00)
	f.close()
	coefficient=map(int, column)
	#print coefficient
	return coefficient
#archi=open("/home/ykprieto/Dropbox/coef"+str(coef)+"_size"+str(size)+"_pts"+pts+".txt",'a')
#archi.write(str(size)+";"+pts+";"+str(vector_coef));
#archi.close()

#------Normalizar DATA----------------------------------------------------------------------------------------------
def standardized(vector):
	c_vector=[]	
	promedio=np.mean(vector)
	DE=np.std(vector)
	for x in vector:
		c_vector=c_vector + [round(float(x-promedio)/float( DE),8)]
	return c_vector
#-------------------------------------------------------------------------------------------------------------------
def draw_function(vector,freq_vector):
	plt.xlabel(r'$\mathrm{C_{00}}$')
	plt.ylabel("Frequency")	
	plt.plot(vector,freq_vector,color='k')
	plt.savefig(str(size) +"x"+ pts+"freq.pdf",bbox_inches='tight', pad_inches=0)
	plt.show()
	plt.close()
#-------------------------------------------------------------------------------------------------------------------
def count_freq(vector):
	c_vector=sorted(list(set(vector)))
	freq_vector=[]
	for x in c_vector:
		freq_vector=freq_vector+ [vector.count(x)]
	return freq_vector
#-------------------------------------------------------------------------------------------------------------------
def P_i(x,valor):
	vec_i=[]
	for i in x:
		if i>=valor:
			vec_i=vec_i +[i]
	return min(vec_i)
#-------------------------------------------------------------------------------------------------------------------
def integrar_f(n,x,freq,k,case):
	maximo=max(x)
	minimo=min(x)
	L=max(math.fabs(maximo),math.fabs(minimo))
	delta=float(maximo-minimo)/float(n)
	#print maximo, minimo, L, delta
	p_i0=minimo-delta
	integral=0	
	for i in range(0,n+1):
		p_ic=p_i0+delta
		p_i=P_i(x,p_ic)
		if case==0:
			F= lambda t: freq[x.index(p_i)]*math.cos(t*k*p_i*(float(math.pi)/float(L)))
			integral1=integrate.quad(F,p_i0,p_ic)
		else:
			F= lambda t: freq[x.index(p_i)]*math.sin(t*k*p_i*(float(math.pi)/float(L)))
			integral1=integrate.quad(F,p_i0,p_ic)
		if i==n-1:
			p_i0=maximo-delta
		else:
			p_i0=p_ic
		integral=integral+integral1[0]
	coef_fourier=(float(1)/float(L) )*integral
	return coef_fourier
#-------------------------------------------------------------------------------------------------------------------		
def partition(n,x,freq,k,case):	 #x = normalized and without repet elements, n=partition size, freq= vector de frequencia o funcion, case, 1=B_k 0=A_k
	maximo=max(x)
	minimo=min(x)
	L=max(math.fabs(maximo),math.fabs(minimo))
	delta=float(maximo-minimo)/float(n)
	#print maximo, minimo, L, delta
	p_i0=minimo-delta
	integral=0	
	for i in range(0,n+1):
		p_ic=p_i0+delta
		p_i=P_i(x,p_ic)
		if case==0:
			F=freq[x.index(p_i)]*math.cos(k*p_i*(float(math.pi)/float(L)))*delta
		else:
			F=freq[x.index(p_i)]*math.sin(k*p_i*(float(math.pi)/float(L)))*delta
		if i==n-1:
			p_i0=maximo-delta
		else:
			p_i0=p_ic
		integral=integral+F
	coef_fourier=(float(1)/float(L) )*integral
	return coef_fourier
#-calcular,estandarizar y dibujar vectores coeficientes----------------------------------------------------------------
vector_coef=Leer_archivo(ruta +"exp_"+str(size)+"_"+str(pts)+".txt",coef) 			#[:30]
#draw_function(list(set(vector_coef)),count_freq(vector_coef))
t=standardized(vector_coef)
ct=sorted(list(set(t)))
draw_function(ct,count_freq(sorted(t)))
#escribiendo la serie--------------------------------------------------------------------------------------------------
vector_coef_fourierA=[]
vector_coef_fourierB=[]
DegF=100
for k in range(0,DegF):
	vector_coef_fourierA=vector_coef_fourierA+[partition(50,ct,count_freq(sorted(t)),k,0)]
	vector_coef_fourierB=vector_coef_fourierB+[partition(50,ct,count_freq(sorted(t)),k,1)]
#	vector_coef_fourierA=vector_coef_fourierA+[integrar_f(50,ct,count_freq(sorted(t)),k,0)]
#	vector_coef_fourierB=vector_coef_fourierB+[integrar_f(50,ct,count_freq(sorted(t)),k,1)]
L=max(math.fabs(max(t)),math.fabs(min(t)))
#print vector_coef_fourierA
#print vector_coef_fourierB
x_Points=np.arange(-L, L,0.01)
y_Points=[]
for x in x_Points:
	f_y=float(vector_coef_fourierA[0])/float(2)
	for k in range(1,len(vector_coef_fourierA)):
		f_y=f_y+vector_coef_fourierA[k]*cos(float(k*math.pi*x)/float(L))+vector_coef_fourierB[k]*sin(float(k*math.pi*x)/float(L))
	y_Points=y_Points+[f_y]
print len(x_Points),len(y_Points)
plt.axis('on')
plt.plot(x_Points, y_Points, color='k')
freqt=count_freq(sorted(t))
plt.plot(ct,freqt, color='red')
plt.show()
		




