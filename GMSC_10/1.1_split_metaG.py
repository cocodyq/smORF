#split inputfile according to X
def splitseq(infile,X,outfile):
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
    
   
if __name__ == '__main__':            
    import sys
    import os
    infile="/home1/duanyq/GMSC_10/GMSC10.metag_smorf.faa.gz"
    outfile="/home1/duanyq/GMSC_10/submetag{ix}.faa.gz"
    splitseq(infile, 1_000_000_000, outfile)
