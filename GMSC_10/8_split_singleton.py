#Rescue singletons
#Split singletons for diamond,because of its large number

def splitseq(infile,X,outfile):
    '''split inputfile according to max number of sequences X'''
    import gzip
    from fasta import fasta_iter
    
    ix = 0
    n = 0
    oname = outfile.format(ix=ix)
    out =  gzip.open(oname, "wt", compresslevel=1)
    for ID,seq in fasta_iter(infile):
        if n < X:
            n += 1
            out.write(f'>{ID}\n{seq}\n')
        else:
            n = 1
            ix += 1
            oname = outfile.format(ix=ix)
            out =  gzip.open(oname, "wt", compresslevel=1)
            out.write(f'>{ID}\n{seq}\n')
        if not ID:
            break
    out.close()
    
INPUT_FILE = "data/metag_ProG_singleton.faa.gz"
SPLIT_FILE_PAT = "diamond/split/sub{ix}.faa.gz"

splitseq(INPUT_FILE, 100000000, SPLIT_FILE_PAT)
