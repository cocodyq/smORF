from jug import TaskGenerator, bvalue
import hashlib
import gzip
from fasta import fasta_iter

@TaskGenerator
def splitseq(infile):
    print("start splitseq")
    outputlist = [
        f'split/submetag_{ix:03}.faa.gz'
        for ix in range(256)]
    outputfiles = [
        gzip.open(f'split/submetag_{ix:03}.faa.gz',compresslevel=1,  mode='wt')
        for ix in range(256)]
    for ID,seq in fasta_iter(infile):
        h = hashlib.sha256()
        h.update(seq.encode('ascii'))
        ix = int(h.hexdigest()[:2], 16)
        outputfiles[ix].write(f'>{ID}\n{seq}\n')
    for ot in outputfiles:
        ot.close()
    print("finish splitseq")
    return (outputlist)

@TaskGenerator
def dedup_fasta(infile):
    from fasta import fasta_iter
    import gzip
    import os
    print("start dedup")
    fasta = {}
    for ID,seq in fasta_iter(infile):
        if seq in fasta:
            fasta[seq][1] += 1
        else:
            fasta[seq] = [ID, 1]

    outfile1 = sp.replace('.faa.gz', '.raw_number.tsv.gz')
    outfile2 = sp.replace('.faa.gz', '.dedup.faa.gz')
    out1 = gzip.open(outfile1, "wt", compresslevel=1)
    out2 = gzip.open(outfile2, "wt", compresslevel=1)
    print("start sort")
    for seq,(ID,count) in sorted(fasta.items()):
        out1.write(f"{count}\t{seq}\n")
        out2.write(f">{ID}\n{seq}\n")
    out1.close()
    out2.close()
    os.unlink(infile)
    print("finish dedup and sort")
    return (outfile1, outfile2)

INPUT_FILE = "data/GMSC10.metag_smorfs.faa.gz"

splits = splitseq(INPUT_FILE)

for sp in bvalue(splits):
    dedup_fasta(sp)
