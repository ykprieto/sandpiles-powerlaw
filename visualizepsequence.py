# -*- coding: utf-8 -*-
#============================================================================
# Name        : visualizepsequence.py
# Author      : Aldo Guzmán-Sáenz
# Version     :
# Copyright   : 
# Description : This program processes the file psequence.dat for human reading
# Input       : python visualizepsequence.py pts size seed
#============================================================================
from struct import unpack

import sys
pts=sys.argv[1]
size=sys.argv[2]
seed=sys.argv[3]
ruta="/home/ykprieto/Dropbox/Algoritmos/Algoritmos_principales/pruebita/"

#this assumes that the integer size is 4 bytes
if __name__ == "__main__":
    with  open(ruta+"psequence"+ pts +"pts_" + size + "size_" + seed+"_experiment.dat","rb") as input:
        pseqlen = unpack("i",input.read(4))[0]
        print pseqlen
        points = [ (unpack("i",input.read(4))[0],unpack("i",input.read(4))[0]) for i in xrange(pseqlen )]
    print points
    
