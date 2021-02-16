def extract(infile,outfile,NR_SINGLETONS):
    selected=frozenset(random.sample(range(NR_SINGLETONS),1000))
    with open(outfile,'w') as out:
        n=0
        for ID,seq in fasta_iter(infile):
           n+=1
           if n in selected:
               out.write(f'>{ID}\n{seq}\n')

if __name__ == '__main__':
    from fasta import fasta_iter
    import random
    
    NR_SINGLETONS_1 = 232027144
    NR_SINGLETONS_2 = 171242722
    
    infile1="clust_result/0.9_result/0.9clu_singleton.faa"
    infile2="clust_result/0.5_result/0.5clu_singleton.faa"
    outfile1="clust_result/0.9_result/0.9clu_singleton_1000.faa"
    outfile2="clust_result/0.5_result/0.5clu_singleton_1000.faa"
    extract(infile1,outfile1,NR_SINGLETONS_1)
    extract(infile2,outfile2,NR_SINGLETONS_2)
