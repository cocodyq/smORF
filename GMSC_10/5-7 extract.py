from jug import TaskGenerator

@TaskGenerator
def extract_seq(infile1,infile2,outfile1,outfile2):
    from fasta import fasta_iter
    import gzip
    fasta={}
    f = gzip.open(infile1,"rt")
    for line in f:
        line = line.strip()
        linelist = line.split("\t")
        if linelist[0] != "1":
            fasta[linelist[1]] = ""
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
    

infile1="data/pro_raw_number.tsv.gz"
infile2="data/pro_dedup.faa.gz"
outfile1="data/pro_nonsingleton.faa.gz"
outfile2="data/pro_singleton.faa.gz"
extract_seq(infile1,infile2,outfile1,outfile2)
