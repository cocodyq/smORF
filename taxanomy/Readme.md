# 1. 100% de redundant and sort with all smORFs
`sortdedup.py`

# 2. Linclust
```
#make db
mmseqs createdb smorfs_dedup.faa smorfs_dedup.DB
#clust with kmer:21,--min-seq-id:0.9
mmseqs linclust smorfs_dedup.DB smorfs_dedup_DB_0.9_clu tmp -c 0.9 --min-seq-id 0.9 
#Extract representative sequence
mmseqs createsubdb smorfs_dedup_DB_0.9_clu smorfs_dedup.DB smorfs_dedup_DB_0.9_clu_rep 
mmseqs convert2fasta smorfs_dedup_DB_0.9_clu_rep  smorfs_dedup_DB_0.9_clu_rep.faa
#generate tsv
mmseqs createtsv smorfs_dedup.DB smorfs_dedup.DB smorfs_dedup_DB_0.9_clu smorfs_dedup_DB_0.9_clu.tsv 
```

# 3. Pre process the two Progenome2.2 files(One is specI-genome,the other is specI-taxonomy)
## (1) Change the name of the first column in specI-taxonomy file.Join specI-genome file and specI-taxanomy file.Find missing specI.
In specI-genome file,the specI name is like `specI_v3_Cluster1`,but in specI-taxanomy file,the specI name is like `specI_v3_02118`.So we need to unify the name format first.

`changespecI.py`

get `ref_specI_taxonomy_change.tsv`
## (2) Map missing specI to Celio's specI-taxonomy file and merge.
- `mapnospecI_taxa.py`
  
  get `nospecI_taxonomy.tsv`
- cat ref_specI_taxonomy_change.tsv nospecI_taxonomy.tsv >ref_specI_taxonomy_all.tsv
## (3) map smORFs to ref_specI_taxonomy_all.tsv,get taxonomy of all smORFs
`taxa_smorf.py`

get `smorfs_dedup_specI_genome_taxa_2.txt`

# 4. Change taxonomy based on clusters
## (1) Map all annotated smORFs to tsv file of linclust
`mapall_lintsv.py`

`smorfs_dedup_DB_0.9_clu.tsv` + `smorfs_dedup_specI_genome_taxa_2.txt` → `taxanomy_tsv.txt`
## (2) Change taxonomy that is different in clusters
`changetaxa.py`

`taxanomy_tsv.txt` → `taxanomy_tsv_change.txt`
## (3) extrat ref smORF and taxonomy in clusters
`extratlin_taxa.py`

`taxanomy_tsv_change.txt` → `taxanomy_tsv_change_clust.txt`

# 5.Krona
## (1) Change format for krona
`krona.py`

`taxanomy_tsv_change_clust.txt` → `taxanomy_tsv_change_clust_krona.txt`
## (2) Krona
ktImportText taxanomy_tsv_change_clust_krona.txt -o linclust_krona.html

# 6.Calculate the number of smORFs and genomes of each taxonomy
`r_format.py`

`taxanomy_tsv_change_clust.txt` → `taxanomy_tsv_change_clust_rformat.txt`

