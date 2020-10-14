def sortsequence(infile,outfile):
    ##open inputfile and store FASTA in the dictionary according to ID and seq
    fasta={}
    with open (infile) as f1:
        for line in f1 :
            line = line.strip()
            if line[0]=='>':
                ID=line
            else:
                fasta[line]=ID
    #sort seq
    fasta = sorted(fasta.items(),key=lambda i:i[0])
    sort = open(outfile,"w")
    for i in range(len(fasta)):
        sort.write(fasta[i][1]+"\n")
        sort.write(fasta[i][0]+"\n")
    sort.close()
if __name__ == '__main__':
    import sys
    import os
    infile="/home1/duanyq/GMSC_10/GMSC10.ProG_smorfs_dedup_more.faa"
    outfile="/home1/duanyq/GMSC_10/GMSC10.ProG_smorfs_dedup_sort_more.faa"
    sortsequence(infile,outfile)
