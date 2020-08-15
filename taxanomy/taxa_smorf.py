# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:13:42 2020

@author: ASUS
"""
def getsmorf_genome(in_file,smorf_genome_outfile):
    out=open(smorf_genome_outfile, "w")
    out.write('smorf'+'\t'+'genome'+'\n')
    with open (in_file) as f:
        for line in f :
            line = line.strip()
            if line.startswith('>'):
                line=line[1:]
                genome=line.split(".")[0]+"."+line.split(".")[1]
                out.write(line+'\t'+genome+'\n')
            else:
                continue
    out.close() 

def mapspecI_genome_taxa(specI_genome_infile,specI_taxa_infile,specI_genome_taxa_outfile):
    specI_genome= pd.read_table(specI_genome_infile,sep='\t',header=None)
    specI_genome.columns=['specI_cluster','genome'] 
    specI_taxanomy=pd.read_table(specI_taxa_infile,sep='\t')
    specI_genome_taxa=pd.merge(specI_genome,specI_taxanomy,on=['specI_cluster'],how='inner')
    specI_genome_taxa.to_csv(path_or_buf=specI_genome_taxa_outfile, sep='\t', index=False)

def mapspecI_taxa(smorf_genome_infile,specI_genome_taxa_infile,smorf_specI_genome_taxa_outfile):
    smorf_genome= pd.read_table(smorf_genome_infile,sep='\t')
    specI_genome_taxa=pd.read_table(specI_genome_taxa_infile,sep='\t')
    smorf_specI_genome_taxa=pd.merge(smorf_genome,specI_genome_taxa,on=['genome'],how='inner')
    smorf_specI_genome_taxa.to_csv(path_or_buf=smorf_specI_genome_taxa_outfile, sep='\t', index=False)
    
if __name__ == '__main__': 
    import sys
    import os
    import pandas as pd
    infile="/share2/yiqian/linclust/smorfs_dedup.faa"
    specIgenome="/share2/yiqian/linclust/ref_genome_specI.tsv"
    specItaxa="/share2/yiqian/linclust/ref_specI_taxonomy_all.tsv"
    smorfgenome="/share2/yiqian/linclust/smorfs_dedup_genome_2.txt"
    specIgenometaxa="/share2/yiqian/linclust/specI_genome_taxa_2.txt"
    smorfspecIgenometaxa="/share2/yiqian/linclust/smorfs_dedup_specI_genome_taxa_2.txt"
    getsmorf_genome(infile,smorfgenome)
    mapspecI_genome_taxa(specIgenome,specItaxa,specIgenometaxa)
    mapspecI_taxa(smorfgenome,specIgenometaxa,smorfspecIgenometaxa)
