# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:10:30 2020

@author: ASUS
"""

def do_tsv(infile):
    index={}
    fa_term=[]
    infoseq={}
    num=1
    with open (infile) as f:
        for line in f :
            line = line.strip()
            if line[0]=='>':    
                if fa_term:
                    seq=''.join(fa_term)
                    fa_term=[]
                    if seq in infoseq.keys():
                        infoseq[seq].append(ID)
                    else:
                        infoseq[seq]=[]
                        infoseq[seq].append(ID)
                if line in index.keys():
                    line=line+"("+str(num)+")"
                    num+=1
                else:
                    index[line]=''
                ID=line
            else:
                fa_term.append(line)
        seq=''.join(fa_term)
        if seq in infoseq.keys():
            infoseq[seq].append(ID)
        else:
            infoseq[seq]=[]
            infoseq[seq].append(ID)
    out=open("D:/project/data/practice.tsv","w")
    for value in infoseq.values():
        for i in range(len(value)):
            out.write(value[0]+"\t"+value[i]+"\n")
            #print(value[0]+"\t"+value[i]+"\n")
    out.close()

if __name__ == '__main__': 
    import sys
    import os
    file="D:/project/data/practice.fasta"
    do_tsv(file)