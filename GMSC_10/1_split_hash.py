import hashlib
import gzip 
from jug import TaskGenerator
from fasta import fasta_iter
    
@TaskGenerator
def split(infile):
    outputfiles = [
        gzip.open(f'block_{ix:03}.fna.gz',compresslevel=1,  mode='wt')
        for ix in range(256)]
    for ID,seq in fasta_iter(infile):
        h=ID
        h = hashlib.sha256()
        h.update(seq.encode('ascii'))
        ix = int(h.hexdigest()[:2], 16)
        outputfiles[ix].write(f'>{ID}\n{seq}\n')
    for ot in outputfiles:
        ot.close()

split(INPUT_FILE)
