# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:25:07 2020

@author: ASUS
"""

#split inputfile according to X
def splitseq(infile,X):
    fa_info = []
    fa_seq=[]
    fa_num = 0
    i=1
    outlist=[]
    #open inputfile and store FASTA in the list according to ID and seq
    with open (infile) as f:
        for line in f :
            line = line.strip()
            if line.startswith('>'):
                fa_info.append(line)
            else:
                fa_seq.append(line)
                fa_num += 1
                if fa_num ==X:
                    outfile="/share/yiqian/smorf/linclust/replace/l6/sub/subsplit"+str(i)+".fasta"
                    i+=1
                    out1=open(outfile, "w")
                    for j in range(X):
                        out1.write(fa_info[j]+"\n")
                        out1.write(fa_seq[j]+"\n")
                    out1.close()
                    fa_info=[]
                    fa_seq=[]
                    fa_num=0
    outfile="/share/yiqian/smorf/linclust/replace/l6/sub/subsplit"+str(i)+".fasta"
    out1=open(outfile, "w")
    for j in range(fa_num):
        out1.write(fa_info[j]+"\n")
        out1.write(fa_seq[j]+"\n")
    out1.close()
if __name__ == '__main__':            
    import sys
    import os
    #X=3 #X is the number of sequences in next every splited file
    circle=0
    inputfile="/share/yiqian/smorf/linclust/replace/l6/sub/sub2.fasta"
    #split inputfile according to X
    outl=splitseq(inputfile,8400000)

