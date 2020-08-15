# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:23:29 2020

@author: ASUS
"""

def krona(in_file,out_file):
    out=open(out_file, "w")
    #kingdom_dict={}
    sp_dict={}
    with open (in_file) as f1:
        for line in f1 :
            line = line.strip()
            if line.startswith("smorf_lin"):
                continue
            else:
                linelist=line.split("\t")
                sp=""
                for i in range(5,len(linelist)):
                    sp+=linelist[i]+"\t"
                sp=sp.strip()
                if sp in sp_dict.keys():
                    sp_dict[sp]+=1
                else:
                    sp_dict[sp]=1
                
    for key,value in sp_dict.items():
        out.write(str(value)+"\t"+key+"\n")
    out.close() 
    
if __name__ == '__main__': 
    import sys
    import os
    import pandas as pd
    infile="/share2/yiqian/linclust/taxanomy_tsv_change_clust.txt"
    outfile="/share2/yiqian/linclust/taxanomy_tsv_change_clust_krona.txt"
    krona(infile,outfile)