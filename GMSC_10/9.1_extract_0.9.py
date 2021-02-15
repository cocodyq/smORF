def extract(infile1,infile2,outfile1,outfile2):
    fastaset=set()
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            fastaset.add(line)
    
    with open(outfile1,"w") as out1, \
        open(outfile2,"w") as out2:
        for ID,seq in fasta_iter(infile2):
            if ID in fastaset:
                out1.write(f'>{ID}\n{seq}\n')
            else:
                out2.write(f'>{ID}\n{seq}\n')

if __name__ == '__main__':
    from fasta import fasta_iter

    infile1="clust_result/0.9_result/0.9clu_singleton_name"
    infile2="clust_result/0.9_result/metag_ProG_nonsingleton_0.9_clu_rep.faa"
    infile3="clust_result/0.5_result/0.5clu_singleton_name"
    infile4="clust_result/0.5_result/metag_ProG_nonsingleton_0.5_clu_rep.faa"
    outfile1="clust_result/0.9_result/0.9clu_singleton.faa"
    outfile2="clust_result/0.9_result/0.9clu_nonsingleton.faa"
    outfile3="clust_result/0.5_result/0.5clu_singleton.faa"
    outfile4="clust_result/0.5_result/0.5clu_nonsingleton.faa"
    extract(infile1,infile2,outfile1,outfile2)
    extract(infile3,infile4,outfile3,outfile4)
