# For smORF datasets
run extern sorting : 
code : cocodyq/smORF/code/extern_sort.py
test data : cocodyq/smORF/data/practice.fasta
test code : cocodyq/smORF/code/test_split.py
            cocodyq/smORF/code/test_sort.py
            cocodyq/smORF/code/test_merge.py
We can change inputfile and X of `splitseq(inputfile,X)` in the code to select the datasets to be processed and the number of sequences in every split file.
And we can change `outfile` of `splitseq()` and `resultfile` of `merge_sortseq()` to select output dir.
The output file will be `split*.fasta`,`medium*_*.fasta`and`result.fasta`

run reduced amino acid alphabet and extern sorting : 
code : cocodyq/smORF/code/replace_sort.py
test data : cocodyq/smORF/data/test_replacesort.fasta
test code : cocodyq/smORF/codetest_replacesort.py
We can change inputfile and X of `splitseq(inputfile,X)` in the code to select the datasets to be processed and the number of sequences in every split file.
We can change `pattern*` to select reduced amino acid alphabet.
And we can change `outfile` of `splitseq()` and `resultfile` of `merge_sortseq()` to select output dir.
The output file will be `split*.fasta`,`medium*_*.fasta`and`replace_*.fasta`
