#!/usr/bin/python
# -*- coding: utf-8 -*-
#============================================================================
# Name        : yu_sandpile.py
# Author      : Yulieth Prieto
# Version     :
# Copyright   : 
# Description : This program computes the minimal degree from 5000 experiments.
# Input	      : python yu_sandpile.py N p 
#Output	      : 
#============================================================================
from struct import unpack
import sys
import numpy as np
import random
import time
#============================================================================
N=int(sys.argv[1])			#size of grid
p=int(sys.argv[2])			#number of points
S=3*np.ones((N,N))
def abelian_sandpile():
	unstable=[]
	areas=[]
	for cont in range (1,p+1):
		A=np.zeros((N, N))			#Cuenta los puntos que cambian
		pi=random.randint(2, N-2)
		pj=random.randint(2, N-2)
		S[pi,pj]=S[pi,pj]+1
		#print "S="+str(S[1:N-1,1:N-1]) + "\n"
		if S[pi,pj]>3:
			unstable=unstable+[(pi,pj)]
		while	verificar(S[1:N-1,1:N-1])>0:
			for element in unstable:
				i=element[0]
				j=element[1]
				unstable=estabilizar(i,j,unstable)
				A[i][j]=A[i][j]+1
				#print str(S[1:N-1,1:N-1])+"\n"
		areas=areas+[int(sum(sum(A)))]
	return areas
def estabilizar(I,J,unstable):
	S[I][J]=S[I][J]-4
	if S[I][J]<4:
		unstable.remove((I,J))

	S[I-1][J]=S[I-1][J]+1
	if S[I-1][J]>3 and I!=1 and I!=N:
		unstable=unstable+[(I-1,J)]

	S[I+1][J]=S[I+1][J]+1
	if S[I+1][J]>3 and I!=N-2:
		unstable=unstable+[(I+1,J)]

	S[I][J-1]=S[I][J-1]+1
	if S[I][J-1]>3 and J!=1 and J!=N:
		unstable=unstable+[(I,J-1)]

	S[I][J+1]=S[I][J+1]+1
	if S[I][J+1]>3 and J!=N-2:
		unstable=unstable+[(I,J+1)]
	unstable=list(set(unstable))
	#print unstable
	return unstable

def verificar(SS):
	if str(len(SS[np.where( SS > 3 )]))=="":
		return 0
	else:
		return len(S[np.where( SS > 3 )])

start_time = time.time()
v_areas=abelian_sandpile()
print("--- %s seconds ---" % (time.time() - start_time))
print v_areas
#print S[1:N-1,1:N-1]
#print verificar(S[1:N-1,1:N-1])
