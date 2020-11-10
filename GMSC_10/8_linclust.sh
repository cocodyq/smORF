#make db
mmseqs createdb GMSC10_smorf_nonsingleton.faa GMSC10_smorf_nonsingleton.DB

#clust with kmer:21,-c 0.9,--min-seq-id:0.9
mmseqs linclust GMSC10_smorf_nonsingleton.DB GMSC10_smorf_nonsingleton_0.9_clu tmp -c 0.9 --min-seq-id 0.9 

#Extract representative sequence
mmseqs createsubdb GMSC10_smorf_nonsingleton_0.9_clu GMSC10_smorf_nonsingleton.DB GMSC10_smorf_nonsingleton_0.9_clu_rep 

mmseqs convert2fasta GMSC10_smorf_nonsingleton_0.9_clu_rep  GMSC10_smorf_nonsingleton_0.9_clu_rep.faa

#generate tsv
mmseqs createtsv GMSC10_smorf_nonsingleton.DB GMSC10_smorf_nonsingleton.DB GMSC10_smorf_nonsingleton_0.9_clu GMSC10_smorf_nonsingleton_0.9_clu.tsv

#calculate clusters
cut -f 1 GMSC10_smorf_nonsingleton_0.5_clu.tsv|sort|uniq -c|wc -l
#calculate singleton
cut -f 1 GMSC10_smorf_nonsingleton_0.5_clu.tsv|uniq -u|wc -l

#clust with kmer:21,-c 0.9,--min-seq-id:0.5
mmseqs linclust GMSC10_smorf_nonsingleton.DB GMSC10_smorf_nonsingleton_0.5_clu tmp -c 0.9 --min-seq-id 0.5
#Extract representative sequence
mmseqs createsubdb GMSC10_smorf_nonsingleton_0.5_clu GMSC10_smorf_nonsingleton.DB GMSC10_smorf_nonsingleton_0.5_clu_rep 

mmseqs convert2fasta GMSC10_smorf_nonsingleton_0.5_clu_rep  GMSC10_smorf_nonsingleton_0.5_clu_rep.faa

#generate tsv
mmseqs createtsv GMSC10_smorf_nonsingleton.DB GMSC10_smorf_nonsingleton.DB GMSC10_smorf_nonsingleton_0.5_clu GMSC10_smorf_nonsingleton_0.5_clu.tsv

#calculate clusters
cut -f 1 GMSC10_smorf_nonsingleton_0.5_clu.tsv|sort|uniq -c|wc -l
#calculate singleton
cut -f 1 GMSC10_smorf_nonsingleton_0.5_clu.tsv|uniq -u|wc -l
