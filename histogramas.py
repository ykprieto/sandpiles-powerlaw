#============================================================================
# Name        : Histogram
# Author      : Yulieth Prieto
# Version     :
# Copyright   :
# Description : This program computes a histogram (coefficient's value vs cumulative frequency) of a experiment's set.
# Input	      : python histogramas.py  size pts compare_i compare_j
#============================================================================

#LIBRARIES
import matplotlib.pyplot as plt
import sys
import math
import matplotlib.mlab as mlab
from struct import unpack
import numpy as np
from math import sqrt
import pylab 
import scipy.stats as stats
from scipy.stats import chi2
#import plotly
#plotly.__version__
#import plotly.plotly as py
#from plotly.tools import FigureFactory as FF 
#INITIAL PARAMETERS
size=sys.argv[1]
pts=sys.argv[2]
ruta="/home/ykprieto/Dropbox/EXPERIMENTOS_TOTAL/"
name_file=ruta + "exp_"+size+"_"+pts+".txt"

#FIX POINTS
name_fileP1=ruta +"exp_"+'50'+"_"+pts+".txt"
name_fileP2=ruta +"exp_"+'100'+"_"+pts+".txt"
name_fileP3=ruta +"exp_"+'200'+"_"+pts+".txt"
name_fileP4=ruta +"exp_"+'300'+"_"+pts+".txt"
name_fileP5=ruta +"exp_"+'500'+"_"+pts+".txt"
name_fileP6=ruta +"exp_"+'1000'+"_"+pts+".txt"

#FIX SIZE
name_fileS1=ruta +"exp_"+size+"_"+'100'+".txt"
name_fileS2=ruta +"exp_"+size+"_"+'500'+".txt"
name_fileS3=ruta +"exp_"+size+"_"+'1000'+".txt"
name_fileS4=ruta +"exp_"+size+"_"+'1500'+".txt"
name_fileS5=ruta +"exp_"+size+"_"+'2000'+".txt"
name_fileS6=ruta +"exp_"+size+"_"+'2500'+".txt"
name_fileS7=ruta +"exp_"+size+"_"+'5000'+".txt"

total_experiments=5000
i = sys.argv[3]
j = sys.argv[4]

#Define case where case is the column that you want analize.
if (i,j)==('0','0'):
	case=1
if (i,j)==('1','0'):
	case= 2
if (i,j)==('0','1'):
	case=3
if (i,j)==('2','0'):
	case=4
if (i,j)==('1','1'):
	case=5
if (i,j)==('0','2'):
	case=6
if (i,j)==('0','3'):
	case=7
if (i,j)==('3','3'):
	case=8
if (i,j)==('3','4'):
	case=9
if (i,j)==('4','3'):
	case=10
if (i,j)==('4','4'):
	case=11
if (i,j)==('5','4'):
	case=12
if (i,j)==('7','8'):
	case=13
if (i,j)==('15','3'):
	case=14
if (i,j)==('15','4'):
	case=15
if (i,j)==('16','3'):
	case=16
if (i,j)==('16','4'):
	case=17
if (i,j)==('k','1'):
	case=18
if (i,j)==('k','2'):
	case=19
if (i,j)==('k','3'):
	case=20
if (i,j)==('k','4'):
	case=21

#print case

#MAKE A VECTOR (coefficient) WITH THE COLUMN TO ANALIZE

def Escribir_tabla1(Classe, difX_mean, X_normal, Area_below, Area_class, Fe):
	name_file="Table_1_"+str(size)+"size_"+str(pts)+"pts_"+str(i)+"-"+str(j) + "_coeff.txt"
	archi=open(ruta+name_file,'w')
	archi.close()
	linea=""
	archi=open("/home/ykprieto/Dropbox/Algoritmos/tablas/"+name_file,'a')
	encabezado="CLASSES,X,X-$\bar{X}$,Z,AREA BELOW,AREA IN CLASS,$F_e$"
	archi.write(encabezado+'\n');
	for k in range(0,len(Classe)+1):
		if k==0:
			intervalo= "Below "+ str(Classe[0])
			linea=intervalo+","+ str(Classe[k]) + ","+ str(difX_mean[k]) + ","+ str(X_normal[k]) + ","+ str(Area_below[k]) + ","+ str(Area_class[k]) + ","+ str(Fe[k])
		
		if 0<k<len(Classe):
			intervalo= str(Classe[k-1]) + "-" + str(Classe[k])
			linea=intervalo+","+ str(Classe[k]) + ","+ str(difX_mean[k]) + ","+ str(X_normal[k]) + ","+ str(Area_below[k]) + ","+ str(Area_class[k]) + ","+ str(Fe[k])
		if k==len(Classe):
			intervalo= str(Classe[k-1])+ " or more"
			linea=intervalo+","+ "__" + ","+ "__" + ","+ "$\infty$" + ","+ str(Area_below[k]) + ","+ str(Area_class[k]) + ","+ str(Fe[k])
		archi.write(linea+'\n');
	archi.close()

def Escribir_tabla2(Classe, Fe, Fr, Dif_Freq, Dif_Freq_2, vector_chi):
	name_file="Table_2_"+str(size)+"size_"+str(pts)+"pts_"+str(i)+"-"+str(j) + "_coeff.txt"
	archi=open(ruta+name_file,'w')
	archi.close()
	linea=""
	archi=open("/home/ykprieto/Dropbox/Algoritmos/tablas/"+name_file,'a')
	encabezado="CLASSES,$F_0$,$F_e$,$F_r-F_e$,$(F_r-F_e)^2$,$(F_r-F_e)^2/F_e$"
	archi.write(encabezado+'\n');
	for k in range(0,len(Classe)+1):
		if k==0:
			intervalo= "Below "+ str(Classe[0])
			linea=intervalo+","+ str(Fr[k]) + ","+ str(Fe[k]) + ","+ str(Dif_Freq[k]) + ","+ str(Dif_Freq_2[k]) + ","+ str(vector_chi[k])
		if 0<k< len(Classe):
			intervalo= str(Classe[k-1]) + "-" + str(Classe[k])
			linea=intervalo+","+ str(Fr[k]) + ","+ str(Fe[k]) + ","+ str(Dif_Freq[k]) + ","+ str(Dif_Freq_2[k]) + ","+ str(vector_chi[k])
		if k==len(Classe):
			intervalo= str(Classe[k-1])+ " and above"
			linea=intervalo+","+ str(Fr[k]) + ","+ str(Fe[k]) + ","+ str(Dif_Freq[k]) + ","+ str(Dif_Freq_2[k]) + ","+ str(vector_chi[k])
		archi.write(linea+'\n');
	archi.close()

def Leer_archivo(name):
	f=open(name,"r")
	lines=f.readlines()
	column=[]
	for x in lines:
		column.append(x.split(',')[case])
	f.close()
	coefficient=map(int, column)
	return coefficient

def histogram(vector):
	plt.hist(vector,bins=13,color='lightgrey')
	#plt.title("Histogram of the coefficient C"+ i + j + " to size: "+ size + " and "+ pts + " random points")
	plt.xlabel(r'$\mathrm{C_{10}}$')
	plt.ylabel("Frequency")
	plt.savefig("cumulative_histogram"+size +"x"+ pts+"_"+str(i)+"-"+str(j)+".pdf")
        plt.show()

def histograma_normal(vector):
	#plt.title("Histogram of the coefficient C"+ i + j + " to size: "+ size + " and "+ pts + " random points")
	plt.xlabel(r'$\mathrm{C_{11}}$')
	#plt.ylabel("Frequency")
	promedio=np.mean(vector)
	print promedio
	DE=np.std(vector)
	print DE
	high = max(vector)
	low = min(vector)
	n, bins, patches = plt.hist(vector, 13, normed=1, facecolor='lightgrey', alpha=0.60)
	x = mlab.normpdf( bins, promedio, DE)
	plt.title(r'$\mathrm{Histogram\ of\ C_{11}:}\ \mu=%.3f,\ \sigma=%.3f$' %(promedio, DE))
	plt.plot(bins, x, 'k--', linewidth=2)
	plt.grid(True)
	plt.savefig(size +"x"+ pts+"_"+str(i)+"-"+str(j)+"Normal.pdf")
        plt.show()

#CONTAR FRECUENCIAS DE DATOS.
def count_freq(vector):
	c_vector=list(set(vector))
	#print c_vector
	freq_vector=[]
	for x in c_vector:
		freq_vector=freq_vector+ [vector.count(x)]
	#plt.title(r'$\mathrm{Frequency\ of\ C}\ $'+i+j )
	plt.xlabel(r'$\mathrm{C_{00}}$')
	plt.ylabel("Frequency")	
	plt.plot(c_vector,freq_vector,'K')
	plt.savefig(size +"x"+ pts+"_"+str(i)+"-"+str(j)+"count_freq.pdf")
	plt.show()

def standardized(vector,promedio,DE):
	c_vector=[]	
	cc_vector=[]
	for x in vector:
		c_vector=c_vector+ [round((x-promedio),3)]
		cc_vector=cc_vector + [round((x-promedio)/ DE,2)]
	return c_vector, cc_vector

def fun_classes (vector):
	low = min(vector)
	high = max(vector)
	ancho=round(float(high-low)/13,2)			#13=(log_2(5000)+1)+1
	classes=[] 		
	for k in range (0,14):					#15=13 +2 (-infty...+infty)
		if k==0:
			lim_sup=low
		if k>0 & k<14:			
			lim_sup=round(lim_sup+ancho,2)		
		classes=classes + [lim_sup]	
	print "VECTOR OF CLASSES:"
	print classes	
	return classes

def frequency_estimated (vector):
	classes=fun_classes(vector)
	promedio=np.mean(vector)
	DE=np.std(vector)
	W,Z=standardized(classes,promedio,DE)
	area_below=[]
	for x in Z:
		area_below=area_below+[round(stats.norm.cdf(x),5)]
	area_below=area_below+[1.00000]
	area_class=[]
	#print "AREA_BELOW"	
	#print area_below
	for k in range(0,len(area_below)):
		if k==0:
			area_class=area_class+[area_below[0]]
		else:
			area_class=area_class+[round(area_below[k]-area_below[k-1],5)]			
	#print "area_class"
	#print area_class
	freq_estimada=[]
	for x in area_class:
		freq_estimada=freq_estimada+ [round (float(len(vector))*x,5)]
	#print freq_estimada
	return area_below, area_class, freq_estimada	

def frequency_real(vector,classes):
	freq_real=[]
	for k in range(0,len(classes)):
		if k==0:
			freq_real=freq_real + [sum(1 for p in vector if (p<=classes[k] ))]
		if (0<k<=len(classes)-1):
			freq_real=freq_real + [sum(1 for p in vector if classes[k-1]<p<=classes[k] )]
		if k==len(classes)-1:
			freq_real=freq_real + [sum(1 for p in vector if p>classes[k])]
	print freq_real
	print "Total frecuencia real: " + str(sum(freq_real)) + ", size vector: " + str(len(freq_real))
	return freq_real
			
def redefinir_classes(classes,f_e):
	f_e2=[]
	classes2=[]
	acum_e=0
	for k in range(0,len(f_e)):
		if f_e[k]>=1:
			classes2=classes2+[classes[k]]
			if acum_e==0:
				f_e2=f_e2+[f_e[k]]
			else:
				f_e2=f_e2+[f_e[k]+acum_e]
				acum_e=0
		else:
			acum_e=acum_e+f_e[k]
		if k==len(f_e)-1 and acum_e>0:
			f_e2[-1]=f_e2[-1] + acum_e
			del classes2[-1]
	print classes2, len(classes2)
	print f_e2,
	print "Total frecuencia estimada: "+ str(sum(f_e2)) +", size vector: " + str(len(f_e2))
	return classes2,f_e2

coefficient1=Leer_archivo(name_file)
#print "Total de experimentos: "+ str(len(coefficient1))
#histogram(coefficient1)
histograma_normal(coefficient1)
#count_freq(coefficient1)


Classe= fun_classes(coefficient1)
difX_mean, X_normal= standardized(Classe,np.mean(coefficient1),np.std(coefficient1))
print "MEAN, STANDARD DEVIATION"
print np.mean(coefficient1),np.std(coefficient1)
area_B, area_C, fe=frequency_estimated(coefficient1)
Escribir_tabla1(Classe, difX_mean, X_normal, area_B, area_C, fe)


#Here we redefine the classes because the division of zero is not defined.
r_Classe,r_fe= redefinir_classes(Classe,fe)
fr=frequency_real(coefficient1,r_Classe)
fe=r_fe
Classe=r_Classe
#print fr,fe
f0_fe=[]
for k in range(0,len(fr)):
	f0_fe=f0_fe+[round(fe[k]-fr[k],4)]
f0_fe2=[]
for k in range(0,len(fr)):
	f0_fe2=f0_fe2+[round(pow(f0_fe[k],2),5)]
chi_vector=[]
for k in range(0,len(fr)):
	chi_vector=chi_vector+[round(f0_fe2[k]/fe[k],5)]
chi_square= sum(chi_vector)

print chi_square, len(Classe)
print chi2.ppf(0.95, len(Classe)-3)

Escribir_tabla2(Classe, fe, fr, f0_fe, f0_fe2, chi_vector)

