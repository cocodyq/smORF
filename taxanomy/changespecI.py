# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:09:34 2020

@author: ASUS
"""

def change(in_file,out_file):

    out=open(out_file, "w")
    with open (in_file) as f1:
        for line in f1 :
            line = line.strip()
            if line.startswith("specI_cluster"):
                out.write(line+"\n")
            else:
                linelist=line.split("\t")
                specIlist=linelist[0].split("_")
                specIlist[2] = re.sub(r"\b0*([1-9][0-9]*|0)", r"Cluster\1", specIlist[2])
                linelist[0]="_".join(specIlist)
                line="\t".join(linelist)
                out.write(line+"\n")
    out.close()
def mapspecI_genome_taxa(specI_genome_infile,specI_taxa_infile,specI_genome_taxa_outfile):
    specI_genome= pd.read_table(specI_genome_infile,sep='\t',header=None)
    specI_genome.columns=['specI_cluster','genome'] 
    specI_taxanomy=pd.read_table(specI_taxa_infile,sep='\t')
    specI_genome_taxa=pd.merge(specI_genome,specI_taxanomy,on=['specI_cluster'],how='inner')
    specI_genome_taxa.to_csv(path_or_buf=specI_genome_taxa_outfile, sep='\t', index=False)
    
def getnospecI(in_file1,in_file2,out_file):
    out=open(out_file, "w")
    specIdict2={}
    with open (in_file2) as f2:
        for line in f2 :
            line = line.strip()
            specI2=line.split("\t")[0]
            specIdict2[specI2]=""
    with open (in_file1) as f1:
        for line in f1 :
            line = line.strip()
            if line == "specI_cluster":
                continue
            else:
                specI1=line.split("\t")[0]
                if specI1 not in specIdict2.keys():
                    out.write(specI1+"\n")
    out.close() 
    

if __name__ == '__main__': 
    import sys
    import os
    import re
    import pandas as pd
    infile="/share2/yiqian/linclust/ref_specI_taxonomy.tsv"
    outfile="/share2/yiqian/linclust/ref_specI_taxonomy_change.tsv"
    specIgenome="/share2/yiqian/linclust/ref_genome_specI.tsv"
    specItaxa="/share2/yiqian/linclust/ref_specI_taxonomy_change.tsv"
    specIgenometaxa="/share2/yiqian/linclust/specI_genome_taxa.txt"
    nospecI="/share2/yiqian/linclust/nospecI.txt"
    change(infile,outfile)
    mapspecI_genome_taxa(specIgenome,specItaxa,specIgenometaxa)
    getnospecI(specIgenome,specIgenometaxa,nospecI)
