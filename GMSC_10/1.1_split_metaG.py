#split inputfile according to X
def splitseq(infile,X,outfile1,outfile2,outfile3,outfile4,outfile5):
    f=open(infile,"r")
    out1=open(outfile1, "w")
    for i in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out1.write(index+"\n"+seq+"\n")
    out1.close()
    out2=open(outfile2, "w")
    for j in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out2.write(index+"\n"+seq+"\n")
    out2.close()
    out3=open(outfile3, "w")
    for x in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out3.write(index+"\n"+seq+"\n")
    out3.close()
    out4=open(outfile4, "w")
    for y in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out4.write(index+"\n"+seq+"\n")
    out4.close()
    out5=open(outfile5, "w")
    for z in range(X):
        index=f.readline().strip()
        seq=f.readline().strip()
        out5.write(index+"\n"+seq+"\n")
    out5.close()
    
   
if __name__ == '__main__':            
    import sys
    import os
    infile="/home1/duanyq/GMSC_10/GMSC10.metag_smorf.faa"
    outfile1="/home1/duanyq/GMSC_10/submetag1.faa"
    outfile2="/home1/duanyq/GMSC_10/submetag2.faa"
    outfile3="/home1/duanyq/GMSC_10/submetag3.faa"
    outfile4="/home1/duanyq/GMSC_10/submetag4.faa"
    outfile5="/home1/duanyq/GMSC_10/submetag5.faa"
    splitseq(infile,1000000000,outfile1,outfile2,outfile3,outfile4,outfile5)