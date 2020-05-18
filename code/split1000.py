# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:17:01 2020

@author: ASUS
"""

#split inputfile according to X
def splitseq(infile,X):
    f=open(infile,"r")
    outfile1="/share/yiqian/smorf/linclust/replace/l6/sub/sub1.fasta"
    out1=open(outfile1, "w")
    for i in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out1.write(index+"\n"+seq+"\n")
    out1.close()
    outfile2="/share/yiqian/smorf/linclust/replace/l6/sub/sub2.fasta"
    out2=open(outfile2, "w")
    while index:
        index=f.readline().strip()
        seq=f.readline().strip()
        out2.write(index+"\n"+seq+"\n")
    out2.close()
    
   
if __name__ == '__main__':            
    import sys
    import os
    #X=3 #X is the number of sequences in next every splited file
    inputfile="/share/yiqian/smorf/linclust/replace/l6/k21/replacededup_DB_0.9_clu_rep.fasta"
    #split inputfile according to X
    outl=splitseq(inputfile,1000)
