def calseq(infile,outfile1,outfile2,outfile3):
    fasta={}
    fa_term=[]
    with open (infile) as f1:
        for line in f1 :
            line = line.strip()
            if line[0]=='>':
                if fa_term:
                    seq=''.join(fa_term)
                    if seq in fasta.keys():
                        fasta[seq][1]+=1
                        fa_term=[]
                    else:
                        fasta[seq]=[]
                        fasta[seq].append(ID)
                        fasta[seq].append(1)
                        fa_term=[]
                ID=line
            else:
                fa_term.append(line)
        seq=''.join(fa_term)
        if seq in fasta.keys():
            fasta[seq][1]+=1
        else:
            fasta[seq]=[]
            fasta[seq].append(ID)
            fasta[seq].append(1)
    out1=open(outfile1, "w")
    out2=open(outfile2, "w")
    out3=open(outfile3, "w")
    for key,value in fasta.items():
        out1.write(str(value[1])+"\t"+value[0]+"\n")
        if value[1]==1:
            out2.write(value[0]+"\n"+key+"\n")
        else:
            out3.write(value[0]+"\n"+key+"\n")
    out1.close()
    out2.close()
    out3.close() 
if __name__ == '__main__':            
    import sys
    import os
    infile="/home1/duanyq/smorf/progenome/data/ProGenomes2.smorfs.faa"
    outfile1="/home1/duanyq/smorf/progenome/data/smorfs_raw_number.txt"
    outfile2="/home1/duanyq/smorf/progenome/data/smorfs_dedup_one.faa"
    outfile3="/home1/duanyq/smorf/progenome/data/smorfs_dedup_more.faa"
    calseq(infile,outfile1,outfile2,outfile3)
