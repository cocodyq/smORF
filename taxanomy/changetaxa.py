# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:33:39 2020

@author: ASUS
"""
def changetaxa(in_file,out_file):
    out=open(out_file, "w")
    smorf_lin={}
    with open (in_file) as f1:
        for line in f1 :
            line = line.strip()
            if line.startswith("smorf_lin"):
                out.write(line+"\n")
            else:
                linelist=line.split("\t")
                if linelist[0] in smorf_lin.keys():
                    smorf_lin[linelist[0]].append(linelist)
                else:
                    if smorf_lin:
                        for key,value in smorf_lin.items():
                            rankchange=-1
                            for rank in range(5,12):
                                rankchange+=1
                                rankdict={}
                                rankdict[value[0][16-rank]]=""
                                flag=0
                                for i in range(len(value)):
                                    if value[i][16-rank] in rankdict.keys():
                                        continue
                                    else:
                                        flag=1
                                        break
                                if flag == 0:
                                    break
                            for j in range(len(value)):
                                for rank_c in range(12-rankchange):
                                    out.write(value[j][rank_c]+"\t")
                                out.write("\n")
                    smorf_lin={}
                    smorf_lin[linelist[0]]=[]
                    smorf_lin[linelist[0]].append(linelist)
    for key,value in smorf_lin.items():
        rankchange=-1
        for rank in range(5,12):
            rankchange+=1
            rankdict={}
            rankdict[value[0][16-rank]]=""
            flag=0
            for i in range(len(value)):
                if value[i][16-rank] in rankdict.keys():
                    continue
                else:
                    flag=1
                    break
            if flag == 0:
                break
        for j in range(len(value)):
            for rank_c in range(12-rankchange):
                out.write(value[j][rank_c]+"\t")
            out.write("\n")
    out.close() 

if __name__ == '__main__': 
    import sys
    import os
    infile="/share2/yiqian/linclust/taxanomy_tsv.txt"
    outfile="/share2/yiqian/linclust/taxanomy_tsv_change.txt"
    changetaxa(infile,outfile)