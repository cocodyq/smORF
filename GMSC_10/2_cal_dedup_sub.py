def calseq(infile,outfile1,outfile2):
    from fasta import fasta_iter
    import gzip
    fasta = {}
    for ID,seq in fasta_iter(infile):
        if seq in fasta:
            fasta[seq][1] += 1
        else:
            fasta[seq] = [ID, 1]
    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 =  gzip.open(outfile2, "wt", compresslevel=1)
    for seq,(ID,count) in fasta.items():
        out1.write(f"{count}\t{seq}\n")
        out2.write(f">{ID}\n{seq}\n")
    out1.close()
    out2.close()

if __name__ == '__main__':
    import sys
    import os
    infile="/home1/duanyq/GMSC_10/submetag5.faa.gz"
    outfile1="/home1/duanyq/GMSC_10/submetag5_raw_number.txt.gz"
    outfile2="/home1/duanyq/GMSC_10/submetag5_dedup.faa.gz"
    calseq(infile,outfile1,outfile2)
