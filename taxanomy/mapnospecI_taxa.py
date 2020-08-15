# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:11:24 2020

@author: ASUS
"""


def mapnospecI_taxa(no_specI_infile,specI_taxa_infile,nospecI_taxa_outfile):
    no_specI= pd.read_table(no_specI_infile,sep='\t',header=None)
    no_specI.columns=['specI_cluster'] 
    specI_taxanomy=pd.read_table(specI_taxa_infile,sep='\t')
    nospecI_taxa=pd.merge(no_specI,specI_taxanomy,on=['specI_cluster'],how='inner')
    nospecI_taxa.to_csv(path_or_buf=nospecI_taxa_outfile, sep='\t', index=False)
    
def addotu(nospecI_taxa_infile,nospecI_taxonomy_outfile):
    out=open(nospecI_taxonomy_outfile, "w")
    with open (nospecI_taxa_infile) as f1:
        for line in f1 :
            line = line.strip()
            if line.startswith("specI_cluster"):
                continue
            else:
                linelist=line.split("\t")
                linelist.append("noref-mOTU_v2_ID")
                out.write(linelist[0]+"\t"+linelist[10]+"\t"+linelist[1]+"\t"+linelist[2]+"\t"+linelist[3]+"\t"+linelist[4]+"\t"+linelist[5]+"\t"+linelist[6]+"\t"+linelist[7]+"\n")
    out.close() 

if __name__ == '__main__': 
    import sys
    import os
    import pandas as pd
    nospecI="/share2/yiqian/linclust/nospecIlist.txt"
    specItaxa="/share2/yiqian/linclust/specI_taxonomy.tsv"
    nospecItaxa="/share2/yiqian/linclust/nospecI_taxa.tsv"
    nospecItaxonomy="/share2/yiqian/linclust/nospecI_taxonomy.tsv"
    mapnospecI_taxa(nospecI,specItaxa,nospecItaxa)
    addotu(nospecItaxa,nospecItaxonomy)