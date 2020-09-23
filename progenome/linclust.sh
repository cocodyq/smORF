export PATH=/home1/duanyq/software/mmseqs/bin:$PATH

#make db
mmseqs createdb smorfs_dedup_more.faa smorfs_dedup_more.DB

#clust with kmer:21,-c 0.9,--min-seq-id:0.5
mmseqs linclust /home1/duanyq/smorf/progenome/data/linclust/smorfs_dedup_more.DB smorfs_dedup_more_0.5_clu tmp -c 0.9 --min-seq-id 0.5 

#Extract representative sequence
mmseqs createsubdb smorfs_dedup_more_0.5_clu /home1/duanyq/smorf/progenome/data/linclust/smorfs_dedup_more.DB smorfs_dedup_more_0.5_clu_rep 
mmseqs convert2fasta smorfs_dedup_more_0.5_clu_rep  smorfs_dedup_more_0.5_clu_rep.faa

#generate tsv
mmseqs createtsv /home1/duanyq/smorf/progenome/data/linclust/smorfs_dedup_more.DB /home1/duanyq/smorf/progenome/data/linclust/smorfs_dedup_more.DB smorfs_dedup_more_0.5_clu smorfs_dedup_more_0.5_clu.tsv


#clust with kmer:21,-c 0.9,--min-seq-id:0.9
mmseqs linclust /home1/duanyq/smorf/progenome/data/linclust/smorfs_dedup_more.DB smorfs_dedup_more_0.9_clu tmp -c 0.9 --min-seq-id 0.9 

#Extract representative sequence
mmseqs createsubdb smorfs_dedup_more_0.9_clu /home1/duanyq/smorf/progenome/data/linclust/smorfs_dedup_more.DB smorfs_dedup_more_0.9_clu_rep 
mmseqs convert2fasta smorfs_dedup_more_0.9_clu_rep  smorfs_dedup_more_0.9_clu_rep.faa

#generate tsv
mmseqs createtsv /home1/duanyq/smorf/progenome/data/linclust/smorfs_dedup_more.DB /home1/duanyq/smorf/progenome/data/linclust/smorfs_dedup_more.DB smorfs_dedup_more_0.9_clu smorfs_dedup_more_0.9_clu.tsv 
