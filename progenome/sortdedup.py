def sortseq(infile,outfile):
    ##open inputfile and store FASTA in the dictionary according to ID and seq
    f=open(infile, "r")
    fasta={}
    index={}
    fa_term=[]
    num=1
    #duplicate
    for line in f :
        line = line.strip()
        if line[0]=='>':
            if fa_term:
                seq=''.join(fa_term)
                fasta[seq]=ID
                fa_term=[]
            if line in index.keys():
                line=line+"("+str(num)+")"
                num+=1
            else:
                index[line]=''
            ID=line
        else:
            fa_term.append(line)
    seq=''.join(fa_term)
    fasta[seq]=ID
    #sort seq
    fasta = sorted(fasta.items(),key=lambda i:i[0])
    f.close()
    sort = open(outfile,"w")
    for i in range(len(fasta)):
        sort.write(fasta[i][1]+"\n")
        sort.write(fasta[i][0]+"\n")
    sort.close()
if __name__ == '__main__':
    import sys
    import os
    infile="/home1/duanyq/smorf/progenome/data/ProGenomes2.smorfs.faa"
    outfile="/home1/duanyq/smorf/progenome/data/smorfs_dedup.faa"
    sortseq(infile,outfile)
