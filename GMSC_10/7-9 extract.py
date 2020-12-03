#calculate occured times of every sequences
def count_number(infile,outfile):
    import gzip
    f = gzip.open(infile,"rt")
    out =  gzip.open(outfile, "wt", compresslevel=1)
    seq={}

    for line in f:
        line = line.strip()
        linelist = line.split("\t")
        if linelist[1] not in seq.keys():
            seq[linelist[1]] = int(linelist[0])
        else:
            seq[linelist[1]] += int(linelist[0])
    for key,value in seq.items():
        out.write(str(value)+"\t"+key+"\n")
    f.close
    out.close()
   
#extract singletons and non-singletons    
def extract_seq(infile1,infile2,outfile1,outfile2):
    from fasta import fasta_iter
    import gzip
    fasta={}
    f = gzip.open(infile1,"rt")
    for line in f:
        line = line.strip()
        linelist = line.split("\t")
        if linelist[0] != "1":
            fasta[line[1]] = ""
    f.close()
    
    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)
    for ID,seq in fasta_iter(infile2):
        if seq in fasta.keys():
            out1.write(f'>{ID}\n{seq}\n')
        else:
            out2.write(f'>{ID}\n{seq}\n')
    out1.close()
    out2.close()
    
if __name__ == '__main__': 
    infile1="splits/all_number.tsv.gz"
    infile2="splits/smorf_dedup.faa.gz"
    outfile1="splits/all_number_dedup.tsv.gz"
    outfile2="splits/smorf_nonsingleton.faa.gz"
    outfile3="splits/smorf_singleton.faa.gz"
    count_number(infile1,outfile1)
    extract_seq(outfile1,infile2,outfile2,outfile3)
