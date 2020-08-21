# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:18:48 2020

@author: ASUS
"""

def maptaxa(id_infile,node_name_infile,id_taxa_outfile):
    taxadict={}
    id_taxadict={}
    ranklist=["superkingdom","phylum","class","order","family","genus","species"]
    rankdict={}
    for j in range(len(ranklist)):
        rankdict[ranklist[j]]=""
    out=open(id_taxa_outfile, "w")
    with open (node_name_infile) as f1:
        for line in f1 :
            line = line.strip()
            number=line.split("\t")[0]
            last=line.split("\t")[1]
            rank=line.split("\t")[2]
            name=line.split("\t")[3]
            taxadict[number]=[last,rank,name]
    
    with open (id_infile) as f2:
        for line in f2 :
            line = line.strip()
            if line in taxadict.keys():
                id_taxadict[line]=[]
                lastnumber=taxadict[line][0]
                if taxadict[line][1] in rankdict.keys():
                    id_taxadict[line].append(taxadict[line][1])
                    id_taxadict[line].append(line+" "+taxadict[line][2])
                while(lastnumber!="1"):
                    if taxadict[lastnumber][1] in rankdict.keys():
                        id_taxadict[line].append(taxadict[lastnumber][1])
                        id_taxadict[line].append(lastnumber+" "+taxadict[lastnumber][2])
                    lastnumber=taxadict[lastnumber][0]
            else:
                continue
    for key,value in id_taxadict.items():
        out.write(key+"\t")
        for i in range(len(value)-1):
            out.write(value[len(value)-1-i]+"\t")
        out.write(value[0]+"\n")
    out.close() 
    
def checkNA(in_file,out_file):
    ranklist=["superkingdom","phylum","class","order","family","genus","species"]
    rankdict={}
    for j in range(len(ranklist)):
        rankdict[ranklist[j]]=""
    rank_taxa={}
    out=open(out_file, "w")
    with open (in_file) as f1:
        for line in f1 :
            line = line.strip()
            linelist=line.split("\t")
            for i in range(1,len(linelist),2):
                rank_taxa[linelist[i+1]]=linelist[i]
            for key in rankdict.keys():
                if key not in rank_taxa.keys():
                    rank_taxa[key]="NA NA"
            out.write(linelist[0]+"\t"+"noID"+"\t")
            for i in range(len(ranklist)-1):
                out.write(rank_taxa[ranklist[i]]+"\t")
            out.write(rank_taxa[ranklist[len(ranklist)-1]]+"\n")
            rank_taxa={}

    out.close()
    
if __name__ == '__main__': 
    import sys
    import os
    idinfile="/share2/yiqian/linclust/notax.txt"
    nodename="/share2/yiqian/linclust/nodes_name.txt"
    idtaxa="/share2/yiqian/linclust/genome_taxa_sp_name.txt"
    outfile="/share2/yiqian/linclust/genome_taxa_sp_NA.txt"
    maptaxa(idinfile,nodename,idtaxa)
    checkNA(idtaxa,outfile)
