def extract(infile1,infile2,outfile):
    fasta={}
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            fasta[line]=""
            
    out=open(outfile,"w")
    for seq_record in SeqIO.parse(infile2, "fasta"):
        if str(seq_record.seq) in fasta.keys():
            out.write(f'>{seq_record.id}\n{seq_record.seq}\n')
    out.close()
    
if __name__ == '__main__': 
    import Bio
    from Bio import SeqIO

    infile1="/home1/duanyq/GMSC_10/nonsingleton.txt"
    infile2="/home1/duanyq/GMSC_10/medium_r4_1_1.fasta"
    outfile="/home1/duanyq/GMSC_10/GMSC10.metag_smorf_nonsingleton.faa"
    extract(infile1,infile2,outfile)
