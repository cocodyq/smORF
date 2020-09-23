export PATH=/home1/duanyq/software:$PATH
diamond makedb --in smorfs_dedup_more_0.5_clu_rep.faa -d smorf_dedup_0.5
diamond makedb --in smorfs_dedup_more_0.9_clu_rep.faa -d smorf_dedup_0.9

diamond blastp -q smorfs_dedup_one.faa -d smorf_dedup_0.5 -o 0.5out.tsv --very-sensitive 
diamond blastp -q smorfs_dedup_one.faa -d smorf_dedup_0.9 -o 0.9out.tsv --very-sensitive 
