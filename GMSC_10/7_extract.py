def extract(infile1,infile2,outfile1,outfile2):
    fasta={}
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            fasta[line]=""
            
    out1=open(outfile1,"w")
    out2=open(outfile1,"w")
    for seq_record in SeqIO.parse(infile2, "fasta"):
        if str(seq_record.seq) in fasta.keys():
            out1.write(f'>{seq_record.id}\n{seq_record.seq}\n')
        else:
            out2.write(f'>{seq_record.id}\n{seq_record.seq}\n')
    out1.close()
    out2.close()
if __name__ == '__main__': 
    import Bio
    from Bio import SeqIO

    infile1="/home1/duanyq/GMSC_10/nonsingleton.txt"
    infile2="/home1/duanyq/GMSC_10/medium_r4_1_1.fasta"
    outfile1="/home1/duanyq/GMSC_10/GMSC10.metag_smorf_nonsingleton.faa"
    outfile2="/home1/duanyq/GMSC_10/GMSC10.metag_smorf_singleton.faa"
    extract(infile1,infile2,outfile1,outfile2)
