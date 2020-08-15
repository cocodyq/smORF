# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:15:52 2020

@author: ASUS
"""

def r_format(in_file,out_file):
    out=open(out_file, "w")
    species_dict={}
    with open (in_file) as f1:
        for line in f1 :
            line = line.strip()
            if line.startswith("smorf_lin"):
                out.write("smorf"+"\t"+"genome"+"\t"+"taxa"+"\n")
                continue
            else:
                linelist=line.split("\t")
                genome=linelist[2]
                species=""
                if len(linelist)>=12:
                    for i in range(5,12):
                        species+=linelist[i]+"\t"
                    species=species.strip()
                    if species in species_dict.keys():
                        species_dict[species][0]+=1
                        if genome not in species_dict[species][2].keys():
                            species_dict[species][2][genome]=""
                            species_dict[species][1]+=1
                    else:
                        species_dict[species]=[1,1,{}]
                        species_dict[species][2][genome]=""       
    for key,value in species_dict.items():
        out.write(str(value[0])+"\t"+str(value[1])+"\t"+key+"\n")
    out.close() 
    
if __name__ == '__main__': 
    import sys
    import os
    infile="/share2/yiqian/linclust/taxanomy_tsv_change_clust.txt"
    outfile="/share2/yiqian/linclust/taxanomy_tsv_change_clust_rformatsp.txt"
    r_format(infile,outfile)