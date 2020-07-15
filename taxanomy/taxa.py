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
    specI_genome= pd.read_table(specI_genome_infile,sep=' ',header=None)
    specI_genome.columns=['specI_cluster','genome'] 
    specI_taxanomy=pd.read_table(specI_taxa_infile,sep='\t')
    specI_genome_taxa=pd.merge(specI_genome,specI_taxanomy,on=['specI_cluster'],how='inner')
    specI_genome_taxa.to_csv(path_or_buf=specI_genome_taxa_outfile, sep='\t', index=False)

def mapsmorf_taxa(smorf_genome_infile,specI_genome_taxa_infile,smorf_specI_genome_taxa_outfile):
    smorf_genome= pd.read_table(smorf_genome_infile,sep='\t')
    specI_genome_taxa=pd.read_table(specI_genome_taxa_infile,sep='\t')
    smorf_specI_genome_taxa=pd.merge(smorf_genome,specI_genome_taxa,on=['genome'],how='left')
    smorf_specI_genome_taxa.to_csv(path_or_buf=smorf_specI_genome_taxa_outfile, sep='\t', index=False)
    
if __name__ == '__main__': 
    import sys
    import os
    import pandas as pd
    infile="/share/yiqian/progenome/ProGenomes2.smorfs.faa"
    specIgenome="/share/yiqian/progenome/specI_cluster_list_genomes.txt"
    specItaxa="/share/yiqian/progenome/specI_taxonomy.tsv"
    smorfgenome="/share/yiqian/progenome/allsmorf_genome.txt"
    specIgenometaxa="/share/yiqian/progenome/allspecI_genome_taxa.txt"
    smorfspecIgenometaxa="/share/yiqian/progenome/allsmorf_specI_genome_taxa.txt"
    getsmorf_genome(infile,smorfgenome)
    mapspecI_genome_taxa(specIgenome,specItaxa,specIgenometaxa)
    mapsmorf_taxa(smorfgenome,specIgenometaxa,smorfspecIgenometaxa)
