def calseq(infile,outfile1,outfile2):
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
    for key,value in fasta.items():
        out1.write(str(value[1])+"\t"+key+"\n")
        out2.write(value[0]+"\n"+key+"\n")
    out1.close()
    out2.close()    
if __name__ == '__main__':            
    import sys
    import os
    infile="/home1/duanyq/GMSC_10/submetag5.faa"
    outfile1="/home1/duanyq/GMSC_10/submetag5_raw_number.txt"
    outfile2="/home1/duanyq/GMSC_10/submetag5_dedup.faa"
    calseq(infile,outfile1,outfile2)
