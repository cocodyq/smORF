#extract name of query sequences
grep ">" /home1/duanyq/smorf/progenome/data/smorfs_dedup_one.faa | sed 's/>//g' > query.names
#extract length of query sequences
grep -v ">" /home1/duanyq/smorf/progenome/data/smorfs_dedup_one.faa | awk '{print length}' > t
#join name  and length of query sequences
paste -d'\t' query.names t > t2; rm -rf t; mv t2 query.names.list

#extract name of subject sequences
grep ">" /home1/duanyq/smorf/progenome/data/linclust/0.9clu/smorfs_dedup_more_0.9_clu_rep.faa | sed 's/>//g' > ref.names.list
#extract length of subject sequences
grep -v ">" /home1/duanyq/smorf/progenome/data/linclust/0.9clu/smorfs_dedup_more_0.9_clu_rep.faa | awk '{print length}' > t
#join name  and length of subject sequences
paste -d'\t' ref.names.list t > t2; rm -rf t; mv t2 ref.names.list

#select identity > 90 and evalue < 1e-5
awk '$3 >= 90 && $11 <= 1e-5' /home1/duanyq/smorf/progenome/data/diamond/0.9out.tsv > align.tsv.tmp
#sort the subject name
sort -k1,1 ref.names.list > ref
#sort the subject name of the second column of the align result
cat align.tsv.tmp | sort -k2,2 > align.tsv.tmp.1
#join to add length of subject
join -1 1 -2 2 ref align.tsv.tmp.1 | sed 's/ /\t/g' > align.tsv.tmp.2
#sort the query name
sort -k1,1 query.names.list > query_length
#sort the query name of the third column of the align result
cat align.tsv.tmp.2 | sort -k3,3 > align.tsv.tmp.3
#join to add length of query
join -1 1 -2 3 query_length align.tsv.tmp.3 | sed 's/ /\t/g' > align.tsv.tmp.4
#add coverage rate
cat align.tsv.tmp.4 | awk '{print $0"\t"$6/$2"\t"$6/$4}' > align.tsv.tmp.5
#select coverage rate both > 0.9
awk '$15 >= 0.9 && $16 >= 0.9' align.tsv.tmp.5 > align_filt.tsv

#extract uniq name of query sequences that can be align
cat align_filt.tsv|cut -f 1|uniq >align_query
