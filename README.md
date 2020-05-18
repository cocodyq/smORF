# For smORF datasets
## run extern sorting : 
code : cocodyq/smORF/code/extern_sort.py                    
test data : cocodyq/smORF/data/practice.fasta               
test code :                         
cocodyq/smORF/code/test_split.py                
cocodyq/smORF/code/test_sort.py                 
cocodyq/smORF/code/test_merge.py                
We can change inputfile and X of `splitseq(inputfile,X)` in the code to select the datasets to be processed and the number of sequences in every split file.                        
We can change `outfile` of `splitseq()` and `resultfile` of `merge_sortseq()` to select output dir.                 
We can change `result` in main to rename result file.   
The output file will be `split*.fasta`,`medium*_*.fasta`and`result.fasta`                       

## run reduced amino acid alphabet and extern sorting : 
code : cocodyq/smORF/code/replace_sort.py                   
test data : cocodyq/smORF/data/test_replacesort.fasta                   
test code : cocodyq/smORF/codetest_replacesort.py                       
We can change inputfile and X of `splitseq(inputfile,X)` in the code to select the datasets to be processed and the number of sequences in every split file.                        
We can change `pattern*` to select reduced amino acid alphabet.                     
We can change `outfile` of `splitseq()` and `resultfile` of `merge_sortseq()` to select output dir.                 
We can change `result` in main to rename result file.   
The output file will be `split*.fasta`,`medium*_*.fasta`and`replace_*.fasta`  

# smORF pipeline  
## decompression  
for example  
```
gunzip -c Zhong_2019_child.smorfs.stats.tsv.gz > /share/yiqian/smorf/data/Zhong_2019_child.smorfs.stats.tsv
```
## tsv to fasta
```
#change file name when using it
python to_fasta.py
```
`/share/yiqian/smorf/data`
## De redundancy
Use `extern_sort.py`with enough disk space.
Take each step apart, delete the intermediate file with not enough disk space.
(Every function has been test)
```
#change file name when using these
python split.py
python sortdedup.py
python merge1.py
```
result 84，142，624 sequences
`/share/yiqian/smorf/output7/dedupsmorf.fasta`
## linclust
```
#make db
mmseqs createdb /share/yiqian/smorf/output7/dedupsmorf.fasta smorf_dedup.DB
#clust with kmer:21,--min-seq-id:0.9
mmseqs linclust /share/yiqian/smorf/linclust/smorf_dedup.DB smorf_dedup_DB_0.9_clu tmp -c 0.9 --min-seq-id 0.9
#Extract representative sequence
mmseqs createsubdb smorf_dedup_DB_0.9_clu /share/yiqian/smorf/linclust/smorf_dedup.DB smorf_dedup_DB_0.9_clu_rep 
mmseqs convert2fasta smorf_dedup_DB_0.9_clu_rep  smorf_dedup_DB_0.9_clu_rep.fasta
#generate tsv
mseqs createtsv /share/yiqian/smorf/linclust/smorf_dedup.DB /share/yiqian/smorf/linclust/smorf_dedup.DB smorf_dedup_DB_0.9_clu smorf_dedup_DB_0.9_clu.tsv
#calculate clusters
cut -f 1 smorf_dedup_DB_0.9_clu.tsv|sort|uniq -c|wc -l
#calculate singleton
cut -f 1  smorf_dedup_DB_0.9_clu.tsv|uniq -u|wc -l
```
change kmer or --min-seq-id and repeat the above process
for example
```
mmseqs linclust /share/yiqian/smorf/linclust/smorf_dedup.DB smorf_dedup_DB_0.9_18_clu tmp -c 0.9 --min-seq-id 0.9 --kmer-per-seq 18
```

## run reduced amino acid alphabet and extern sorting
```
replacesmorf.py
sortdedup.py
merge1.py
```
## linclust
Use dudup result to do linclust.repeat the above process
## swipe
### split 1000 sequences
```
python split1000.py
```
result:
`/share/yiqian/smorf/linclust/replace/l6/sub/sub1.fasta`
`/share/yiqian/smorf/linclust/replace/l6/sub/sub2.fasta`
### split sub2.fasta 
```
#change file name when using it
python split1.py
```
result:  
`/share/yiqian/smorf/linclust/replace/l6/sub/subsplit1.fasta`
`/share/yiqian/smorf/linclust/replace/l6/sub/subsplit2.fasta`
`/share/yiqian/smorf/linclust/replace/l6/sub/subsplit3.fasta`
`/share/yiqian/smorf/linclust/replace/l6/sub/subsplit4.fasta`
`/share/yiqian/smorf/linclust/replace/l6/sub/subsplit5.fasta`
### swipe
```
export PATH=/share/yiqian/software/ncbi-blast-2.10.0+/bin:$PATH
export PATH=/share/yiqian/software/swipe-2.0.5:$PATH
#make db
makeblastdb -in subsplit1.fasta -dbtype prot -blastdb_version 4 -out subsplit1db
#swipe
swipe -d subsplit1db -i sub1.fasta -a 3 -m '8 std qcovs' -o split1out -p 1
```
### calculate result
```
grep ">" subsplit5.fasta | awk '{print "gnl|BL_ORD_ID|"NR-1"\t"$1}' | sed 's/>//g' > ref5.names.list
grep -v ">" subsplit5.fasta | awk '{print length}' > t
paste -d'\t' ref5.names.list t > t2; rm -rf t; mv t2 ref5.names.list
awk '$3 >= 80 && $11 <= 1e-5' split5out > split5tmp
sort -k1,1 ref5.names.list | cut -f1,3 > ref5
cat split5tmp | sort -k2,2 > split5tmp.5
join -1 1 -2 2 ref5 split5tmp.5 | sed 's/ /\t/g' > split5tmp.6
cat split5tmp.6 | sort -k3,3 > split5tmp.7
join -1 1 -2 3 query split5tmp.7 | sed 's/ /\t/g' > split5tmp.8
cat split5tmp.8 | awk '{print $0"\t"$6/$2"\t"$6/$4}' > split5tmp.9
awk '$15 >= 0.9 && $16 >= 0.9' split5tmp.9 > split5tmp.10.filt
cat split5tmp.10.filt | sort -k1,1 | uniq > 0.9filt5
cat 0.9filt5|cut -f1|uniq >0.9filt_uniq5
cat 0.9filt_uniq5|wc -l
```
```
join -a1 -a2 0.9filt_uniq1 0.9filt_uniq2 | sed 's/ /\t/g' > 0.9join1
join -a1 -a2 0.9join1 0.9filt_uniq3 | sed 's/ /\t/g' > 0.9join2
join -a1 -a2 0.9join2 0.9filt_uniq4 | sed 's/ /\t/g' > 0.9join3
join -a1 -a2 0.9join3 0.9filt_uniq5 | sed 's/ /\t/g' > 0.9join4
cat 0.9join4 | wc-l
```


