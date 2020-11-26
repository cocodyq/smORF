from jug import TaskGenerator, bvalue

@TaskGenerator
def splitseq(infile,X,outfile):
    '''split inputfile according to max number of sequences X'''
    import gzip
    f = gzip.open(infile,"rt")
    ix = 0
    n = X + 1
    onames = []
    while True:
        index = f.readline().strip()
        seq = f.readline().strip()
        if not seq:
            break
        if n > X:
            oname = outfile.format(ix=ix)
            onames.append(oname)
            out =  gzip.open(oname, "wt", compresslevel=1)
        out.write(index+"\n"+seq+"\n")
    out.close()
    return onames
    
@TaskGenerator
def dedup_fasta(infile):
    from fasta import fasta_iter
    import gzip
    import os
    fasta = {}
    for ID,seq in fasta_iter(infile):
        if seq in fasta:
            fasta[seq][1] += 1
        else:
            fasta[seq] = [ID, 1]

    outfile1 = sp.replace('.faa.gz', 'raw_number.tsv.gz')
    outfile2 = sp.replace('.faa.gz', 'dedup.faa.gz')
    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)
    for seq,(ID,count) in sorted(fasta.items()):
        out1.write(f"{count}\t{seq}\n")
        out2.write(f">{ID}\n{seq}\n")
    out1.close()
    out2.close()
    os.unlink(infile)
    return (outfile1, outfile2)

INPUT_FILE = "data/GMSC10.metag_smorf.faa.gz"
SPLIT_FILE_PAT = "splits/submetag{ix}.faa.gz"

splits = splitseq(INPUT_FILE, 1_000_000_000, SPLIT_FILE_PAT)

for sp in bvalue(splits):
    dedup_fasta(sp)

