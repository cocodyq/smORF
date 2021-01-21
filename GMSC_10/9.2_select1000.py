NR_NON_SINGLETONS = 232030377
def extract(infile,outfile):
    selected=frozenset(random.sample(range(NR_NON_SINGLETONS),1000))
    with open(outfile,'w') as out:
        for n, seq_record in enumerate(SeqIO.parse(infile, "fasta")):
           if n in selected:
               out.write(f'>{seq_record.id}\n{seq_record.seq}\n')

if __name__ == '__main__':
    import Bio
    from Bio import SeqIO
    import random

    infile="/home1/duanyq/GMSC_10/linclust/0.9/0.9clu_singleton.faa"
    outfile="/home1/duanyq/GMSC_10/linclust/0.9/0.9clu_singleton_1000.faa"
    extract(infile,outfile)
