def extract(infile1,infile2,outfile1,outfile2):
    fasta=set()
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            fasta.add(line)

    with open(outfile1,"w") as out1, \
        open(outfile2,"w") as out2:
        for seq_record in SeqIO.parse(infile2, "fasta"):
            if str(seq_record.id) in fasta:
                out1.write(f'>{seq_record.id}\n{seq_record.seq}\n')
            else:
                out2.write(f'>{seq_record.id}\n{seq_record.seq}\n')

if __name__ == '__main__':
    import Bio
    from Bio import SeqIO

    infile1="/home1/duanyq/GMSC_10/linclust/0.9/0.9clu_singleton_name"
    infile2="/home1/duanyq/GMSC_10/linclust/0.9/GMSC10_smorf_nonsingleton_0.9_clu_rep.faa"
    outfile1="/home1/duanyq/GMSC_10/linclust/0.9/0.9clu_singleton.faa"
    outfile2="/home1/duanyq/GMSC_10/linclust/0.9/0.9clu_nonsingleton.faa"
    extract(infile1,infile2,outfile1,outfile2)
