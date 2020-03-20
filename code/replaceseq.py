# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:28:49 2020

@author: ASUS
"""
def replace(infile):
    fasta={}
    index={}
    num=1
    fa_term=[]
    with open (infile) as f:
        for line in f:
            line = line.strip()
            if line[0]=='>':
                if fa_term:
                    seq=''.join(fa_term)
                    fasta[ID]=seq
                    fa_term=[]
                if line in index.keys():
                    line=line+"("+str(num)+")"
                    num+=1
                else:
                    index[line]=''
                ID=line
                fasta[ID]=''
            else:
                #pattern1=re.compile(r'[ND]')
                pattern2=re.compile(r'[KE]')
                #pattern3=re.compile(r'[TSQ]')
                #pattern4=re.compile(r'[YF]')
                pattern5=re.compile(r'[LIV]')
                #line=re.sub(pattern1,'N',line)
                line=re.sub(pattern2,'K',line)
                #line=re.sub(pattern3,'T',line)
                #line=re.sub(pattern4,'Y',line)
                line=re.sub(pattern5,'L',line)
                fa_term.append(line)
            seq=''.join(fa_term)
            fasta[ID]=seq

    out=open("D:/project/data/replace_17.fasta","w")
    for key,value in fasta.items():
        out.write(key+"\n")
        out.write(value+"\n")
    out.close()

if __name__ == '__main__': 
    import sys
    import os
    import re
    file="D:/project/data/practice.fasta"
    replace(file)