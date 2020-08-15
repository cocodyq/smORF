# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:23:06 2020

@author: ASUS
"""

def changetaxa(in_file,out_file):
    out=open(out_file, "w")
    with open (in_file) as f1:
        for line in f1 :
            line = line.strip()
            if line.startswith("smorf_lin"):
                out.write(line+"\n")
            else:
                linelist=line.split("\t")
                if linelist[0]==linelist[1]:
                    out.write(line+"\n")
    out.close() 

if __name__ == '__main__': 
    import sys
    import os
    infile="/share2/yiqian/linclust/taxanomy_tsv_change.txt"
    outfile="/share2/yiqian/linclust/taxanomy_tsv_change_clust.txt"
    changetaxa(infile,outfile)