export PATH=/home1/duanyq/software/swipe-2.0.5:$PATH
export PATH=/home1/duanyq/software/ncbi-blast-2.10.1+/bin:$PATH

#makedb using blast+
makeblastdb -in /home1/duanyq/smorf/progenome/data/linclust/0.5clu/smorfs_dedup_more_0.5_clu_rep.faa -dbtype prot -blastdb_version 4 -out smorf_dedup_more_0.5rep_db
makeblastdb -in /home1/duanyq/smorf/progenome/data/linclust/0.9clu/smorfs_dedup_more_0.9_clu_rep.faa -dbtype prot -blastdb_version 4 -out smorf_dedup_more_0.9rep_db

#align smORFs that only occurred once to 0.5 identity clusters and 0.9 identity clusters using swipe 
swipe -d smorf_dedup_more_0.5rep_db -i /home1/duanyq/smorf/progenome/data/smorfs_dedup_one.faa -a 3 -m '8 std qcovs' -o singleton_align_rep -p 1
swipe -d smorf_dedup_more_0.9rep_db -i /home1/duanyq/smorf/progenome/data/smorfs_dedup_one.faa -a 3 -m '8 std qcovs' -o singleton_align_0.9rep -p 1
