# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:51:40 2020

@author: ASUS
"""
def getmore(infile):
    fasta={}
    fa_term=[]
    with open (infile) as f:
        for line in f:
            line=line.strip()
            if line[0]=='>':
                if fa_term:
                    seq=''.join(fa_term)
                    if seq in fasta.keys():
                        fasta[seq][0]+=1
                    else:
                        fasta[seq]=[1]
                        fasta[seq].append(ID)
                    
                    fa_term=[]
                ID=line 
            else:
                fa_term.append(line)
        seq=''.join(fa_term)
        if seq in fasta.keys():
            fasta[seq][0]+=1
        else:
            fasta[seq]=[1]
            fasta[seq].append(ID)
    out=open("D:/project/data/moreseq.fasta","w")
    for key,value in fasta.items():
        if value[0]>1:
            out.write(value[1]+"\n")
            out.write(key+"\n")
    out.close()

if __name__ == '__main__': 
    import sys
    import os
    file="D:/project/data/practice.fasta"
    getmore(file)