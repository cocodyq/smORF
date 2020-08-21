# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:17:34 2020

@author: ASUS
"""

def join_genome_taxa(taxa_infile,genome_infile,genome_taxa_outfile):
    in_taxa= pd.read_table(taxa_infile,sep='\t')
    in_taxa.columns=["taxa","ref-mOTU_v2_ID","kingdom","phylum","class","order","family","genus","species"] 
    in_genome= pd.read_table(genome_infile,sep='\t')
    in_genome.columns=["genome","taxa"] 
    genome_taxa=pd.merge(in_genome,in_taxa,on=['taxa'],how='inner')
    genome_taxa.columns=["genome","specI_cluster","ref-mOTU_v2_ID","kingdom","phylum","class","order","family","genus","species"] 
    genome_taxa["specI_cluster"]="nospecI"
    genome_taxa.to_csv(path_or_buf=genome_taxa_outfile, sep='\t', index=False)

def join_smorf_genome(smorf_infile,genome_infile,out_file):
    in_smorf= pd.read_table(smorf_infile,sep='\t')
    in_smorf.columns=["smorf","genome"] 
    in_genome= pd.read_table(genome_infile,sep='\t')
    smorf_genome=pd.merge(in_smorf,in_genome,on=['genome'],how='inner')
    smorf_genome.to_csv(path_or_buf=out_file, sep='\t', index=False,header=0)
    
if __name__ == '__main__': 
    import sys
    import os
    import pandas as pd
    taxa="/share2/yiqian/linclust/genome_taxa_sp_NA.txt"
    genome="/share2/yiqian/linclust/nogenome_tax.txt"
    smorf="/share2/yiqian/linclust/nosmorf_genome_2.txt"
    genometaxa="/share2/yiqian/linclust/genome_specI_inname.txt"
    outfile="/share2/yiqian/linclust/smorf_genome_specI_inname.txt"
    join_genome_taxa(taxa,genome,genometaxa)
    join_smorf_genome(smorf,genometaxa,outfile)