# -*- coding: utf-8 -*-
#============================================================================
# Name        : visualizeactive.py
# Author      : 
# Version     :
# Copyright   : 
# Description : This program processes the file active.dat for human reading
# Input       : python visualizeactive.py pts size seed
#============================================================================
from struct import unpack
import sys
pts=sys.argv[1]	#input points
size=sys.argv[2] #input size
seed=sys.argv[3] #input number of experiment
#active10pts_100size_3_experiment
#this assumes that the integer size is 4 bytes
if __name__ == "__main__":
    with  open("./active"+pts+"pts_"+size+"size_"+seed+"_experiment.dat","rb") as input:
        pseqlen = unpack("i",input.read(4))[0]
        #print pseqlen
        points = [(unpack("i",input.read(4))[0],unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]) for i in xrange(pseqlen )]
    #print points

V_i=[]
V_j=[]
V_Cij=[]
for x in points:
	V_i=V_i+[x[0]]
	V_j=V_j+[x[1]]
	V_Cij=V_Cij+[x[2]]

print V_i
print V_j
print V_Cij
    


