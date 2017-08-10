#============================================================================
# Name        : powerlaw.py
# Author      : Yulieth Prieto
# Version     :
# Copyright   :
# Description : This program computes a histogram of power law from avalanches calculated before. Also, it estimats the critical exponent.
# Input	      : python powerlaw.py  size pts NN (where is a subset from pts)
#=========================================================================================================================================
# REMARKS  : Change the path of saved pictures in "ruta". Check the comments between codes line.
#=========================================================================================================================================
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
from math import sqrt, log
import scipy.stats as stats
from collections import Counter

size=sys.argv[1]
pts=sys.argv[2]
NN=int(sys.argv[3])
ruta="/home/ykprieto/Dropbox/Algoritmos/power_law/bueno/power"
name_file=ruta+size+"_"+pts+"w.txt"
#name_file="/home/ykprieto/Dropbox/Algoritmos/power_law/bueno/workfile50.txt"
bi=int(round(math.sqrt(int(pts))))
#bi=200
def Leer_archivo(name):
	vector=""
	f=open(name,"r")
	for line in f: 
		vector=vector+line
	if vector[-1:]==",":
		vector=vector[:-1]
	#print vector
	return map(float,vector.split(","))

def histograma_0(vector):
	plt.xlabel("Log"+r'$(A_{i})$')
	plt.ylabel("Log(Frequency)")
	plt.grid(True)
	plt.yscale('log',basex=2)
	plt.xscale('log',basey=2)
	plt.hist(vector,bins=bi)
	#freq, bins = np.histogram(vector, bi)
	#print freq
	#print bins
	plt.show()
def histogram(xx,yy,yyy,sw):			#log-log scale
	plt.xlabel("Log"+r'$(A_{i})$')
	plt.ylabel("Log(Frequency)")
	plt.grid(True)
	#COMPARAR CON LINEAL:
	plt.plot(xx, yyy, 'r', marker='.',ls='',label='Fitted line')
	plt.plot(xx,yy,'b',marker='.',ls='',label='Experimental values')
	plt.legend(loc='best',ncol=2)
	plt.savefig("./PL"+size +"x"+pts+"_sw"+ str(sw)+".pdf")
	plt.show()
	plt.clf()
	if sw==0:		
		print number_bins0(xx,yy,yyy)	#Para ver a ojo cual es el candidato a NN
def fit_power(yy,xx):				#CALCULA LA APROXIMACION TEORICA DE POWERLAW
	A = np.vstack([xx, np.ones(len(xx))]).T
	m, c = np.linalg.lstsq(A,yy)[0]
	return m,c
def number_bins0(xx,yy,yyy):				#Crea un vector de posiciones donde el valor experimental < valor teorico
	intervalo=[]
	for i in range (0,len(xx)):
		if yy[i]<yyy[i]:		 	#if real is less than theoretical
			intervalo=intervalo+[i]
	return intervalo	
def particion(vector):	
	freq, bins = np.histogram(vector, bi)
	xx=[]
	yy=[]
	zz=[]
	archi=open("./FreqOriginal"+size+"_"+pts+".txt",'w') #Change the path.
	for i in range(0,bi):
		if freq[i]>0:
			xx=xx+[bins[i]]
			yy=yy+[freq[i]]
			zz=zz+[(bins[i]+bins[i+1])/float(2)]
		linea=str(bins[i])+"-"+str(bins[i+1])+";"+str((bins[i]+bins[i+1])/float(2))+";"+str(freq[i])+"\n"
		archi.write(linea)
	archi.write("Total frequencies: "+str(sum(freq)))
	archi.close()
	xx=xx+[bins[len(bins)-1]]
	zz=np.log2(zz)
	yy=np.log2(yy)
	#print yy,zz	
	return xx,yy,zz

def tabla_freq(vector):
	plt.grid(True)
	vector=sorted(vector)
	xx,yy,zz=particion(vector)
	#print len(xx),len(yy),len(zz)
	archi=open("./Freq"+size+"_"+pts+".txt",'w')  #Change the path.
	linea=""
	for i in range(0,len(yy)):
		if (i<len(xx)):
			linea=str(xx[i])+" - "+str(xx[i+1])+ ";"+ str(2**zz[i])+ ";"+str(2**yy[i])+";"+ str(zz[i])+ ";"+str(yy[i])
			#print linea
			archi.write(linea+"\n");
	archi.write("Total Datos en intervalos: "+str(int(sum(np.power(2,yy))))+ "\n"+"Total Datos inicial: "+ str(len(vector))+"\n");
	print "Total Datos en intervalos: "+str(int(sum(np.power(2,yy))))+ "\n"+"Total Datos inicial: "+ str(len(vector))+"\n"
	archi.close()

escalar=float(1)/(int(size)*int(size))
datos1=escalar*np.array(Leer_archivo(name_file))
#print datos1
tabla_freq(datos1)
histograma_0(datos1)
datos2=[]
for x in datos1:
	if x<=1:
		datos2=datos2+[x]
#datos1=datos1[NN:]
#print datos1
W,Y,X=particion(datos2)
M,C=fit_power(Y,X)
print M,C
YY=M*X + C
histogram(X,Y,YY,0)
X1=X[:NN]
Y1=Y[:NN]
M1,C1=fit_power(Y1,X1)
print M1,C1
YY=M1*X1 + C1	
histogram(X1,Y1,YY,1)

X2=X[NN:]
Y2=Y[NN:]
M2,C2=fit_power(Y2,X2)
print M2,C2
YY=M2*X2 + C2	
histogram(X2,Y2,YY,2)	

archi=open("./criticalexponents.txt",'a')
archi.write(size + "," + pts +"," + str(round(int(pts)/float(int(size)*int(size)),10))+ ",("+ str(round(M,3)) + ";" + str(round(C,3))+ ")"+",("+ str(round(M1,3)) + ";" + str(round(C1,3))+ ")"+",("+ str(round(M2,3)) + ";" + str(round(C2,3))+ ")"+"\n");
archi.close()
