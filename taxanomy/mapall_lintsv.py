# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:47:03 2020

@author: ASUS
"""

def maptaxa_tsv(lintsv_infile,taxa_infile,taxa_tsv_outfile):
    lin_tsv= pd.read_table(lintsv_infile,sep='\t',header=None)
    lin_tsv.columns=['smorf_lin','smorf'] 
    taxonomy=pd.read_table(taxa_infile,sep='\t')
    taxa_tsv=pd.merge(lin_tsv,taxonomy,on=['smorf'],how='inner')
    taxa_tsv.to_csv(path_or_buf=taxa_tsv_outfile, sep='\t', index=False)

if __name__ == '__main__': 
    import sys
    import os
    import pandas as pd
    lintsv="/share2/yiqian/linclust/smorfs_dedup_DB_0.9_clu.tsv"
    taxa="/share2/yiqian/linclust/smorfs_dedup_specI_genome_taxa_2.txt"
    taxa_tsv="/share2/yiqian/linclust/taxanomy_tsv.txt"
    maptaxa_tsv(lintsv,taxa,taxa_tsv)
