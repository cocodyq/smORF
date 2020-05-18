# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:59:32 2020

@author: ASUS
"""

def replace(file):
    fasta={}
    inputf="/share/yiqian/smorf/output8/"+file
    with open (inputf) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                ID=line
                fasta[ID]=''
            else:
                pattern1=re.compile(r'[ND]')
                pattern2=re.compile(r'[KER]')
                pattern3=re.compile(r'[HCTSQ]')
                pattern4=re.compile(r'[YFW]')
                pattern5=re.compile(r'[ALIVM]')
                line=re.sub(pattern1,'N',line)
                line=re.sub(pattern2,'K',line)
                line=re.sub(pattern3,'H',line)
                line=re.sub(pattern4,'Y',line)
                line=re.sub(pattern5,'L',line)
                fasta[ID]=line
    outfile="/share/yiqian/smorf/output9/"+file
    out=open(outfile,"w")
    for key,value in fasta.items():
        out.write(key+"\n")
        out.write(value+"\n")
    out.close()

if __name__ == '__main__': 
    import sys
    import os
    import re
    name=[]
    infile="/share/yiqian/smorf/code/rename.txt"
    with open (infile) as file:
        for line in file:
            line=line.strip()
            name.append(line)
    for i in range(len(name)):
        inputfile=name[i]
        replace(inputfile)
