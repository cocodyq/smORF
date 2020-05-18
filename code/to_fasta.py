# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:48:30 2020

@author: ASUS
"""
import os
import sys
tsvfile="/share/yiqian/smorf/code/name2.txt"
file=[]
with open(tsvfile) as tsvf:
    for tsv in tsvf:
        tsv=tsv.strip()
        file.append(tsv)
#file=["Odonovan_2020_athlete.smorfs.stats","Nagy-Szakal_2017_CFS.smorfs.stats","Lundgren_2018_infants.smorfs.stats","Korpela_2018.smorfs.stats","PRJEB32135_infant_canada.smorfs.stats","Dhakan_2019.smorfs.stats","Sankaranarayanan_2015_nativeAmericans.smorfs.stats","","","","","","","","","","","","",]
for name in file:
    infile="/share/yiqian/smorf/data/"+name+".tsv"
    outfile="/share/yiqian/smorf/data/"+name+".fasta"
    outfile=open(outfile,"w")
    with open (infile) as f:
        line=f.readline()
        for line in f:
            line=line.strip()
            linelist=line.split("\t")
            #print(">"+linelist[0]+"\n"+linelist[1])
            outfile.write(">"+linelist[0]+"\n"+linelist[1]+"\n")
    outfile.close()
