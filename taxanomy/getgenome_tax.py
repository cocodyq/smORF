# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:31:56 2020

@author: ASUS
"""

def gettax(in_file,out_file):
    taxdict={}
    out=open(out_file, "w")
    with open (in_file) as f1:
        for line in f1 :
            line = line.strip()
            tax=line.split(".")[0]
            taxdict[tax]=""
    for key in taxdict.keys():
        out.write(key+"\n")
    out.close() 

def getgenometax(in_file,out_file):
    out=open(out_file, "w")
    with open (in_file) as f2:
        for line in f2 :
            line = line.strip()
            tax=line.split(".")[0]
            out.write(line+"\t"+tax+"\n")
    out.close() 

if __name__ == '__main__': 
    import sys
    import os
    infile="/share2/yiqian/linclust/nogenome_2.txt"
    outfile1="/share2/yiqian/linclust/notax.txt"
    outfile2="/share2/yiqian/linclust/nogenome_tax.txt"
    gettax(infile,outfile1)
    getgenometax(infile,outfile2)
