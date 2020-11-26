#split inputfile according to X
def splitseq(infile,X,outfile1,outfile2,outfile3,outfile4,outfile5):
    import gzip
    f=gzip.open(infile,"rt")
    out1=gzip.open(outfile1, "wt", compresslevel=1)
    for i in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out1.write(index+"\n"+seq+"\n")
    out1.close()
    out2=gzip.open(outfile2, "wt", compresslevel=1)
    for j in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out2.write(index+"\n"+seq+"\n")
    out2.close()
    out3=gzip.open(outfile3, "wt", compresslevel=1)
    for x in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out3.write(index+"\n"+seq+"\n")
    out3.close()
    out4=gzip.open(outfile4, "wt", compresslevel=1)
    for y in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out4.write(index+"\n"+seq+"\n")
    out4.close()
    out5=gzip.open(outfile5, "wt", compresslevel=1)
    for z in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        if not seq:
            break
        out5.write(index+"\n"+seq+"\n")
    out5.close()

    if f.read(1):
        raise ValueError("Unexpected data")
    
   
if __name__ == '__main__':            
    import sys
    import os
    infile="/home1/duanyq/GMSC_10/GMSC10.metag_smorf.faa.gz"
    outfile1="/home1/duanyq/GMSC_10/submetag1.faa.gz"
    outfile2="/home1/duanyq/GMSC_10/submetag2.faa.gz"
    outfile3="/home1/duanyq/GMSC_10/submetag3.faa.gz"
    outfile4="/home1/duanyq/GMSC_10/submetag4.faa.gz"
    outfile5="/home1/duanyq/GMSC_10/submetag5.faa.gz"
    splitseq(infile,1000000000,outfile1,outfile2,outfile3,outfile4,outfile5)
