import sys
import os
import pytest
#split inputfile according to X
def splitseq(infile,X):
    #X is the number of sequences in next every splited file
    fa_info = []
    fa_term = []
    fa_seq=[]
    fa_num = 0
    outlist=[]
    #open inputfile and store FASTA in the list according to ID and seq
    with open (infile) as f:
        for line in f :
            line = line.strip()
            if line.startswith('>'):
                fa_num += 1
                fa_info.append(line)
                if fa_term:
                    seq=''.join(fa_term)
                    fa_seq.append(seq)
                    fa_term=[]
            else:
                fa_term.append(line)
        seq=''.join(fa_term)
        fa_seq.append(seq)
    #split according to X
        if (fa_num%X) == 0:
            file_num=fa_num//X
        else:
            file_num = fa_num//X+1
        for i in range(file_num):
            outfile="./output/split"+str(i+1)+".fasta"
            out1=open(outfile, "w")
            outlist.append(outfile)
            start=i*X
            end=(i+1)*X
            if end > fa_num:
                end=fa_num
            for j in range(start,end,1):
                out1.write(fa_info[j]+"\n")
                out1.write(fa_seq[j]+"\n")
            out1.close()
    return outlist

def test_splitseq():
    infile="./data/practice.fasta"
    testlist=splitseq(infile,3)
    file_list=["D:/project/output/split1.fasta","D:/project/output/split2.fasta","D:/project/output/split3.fasta"]
    assert testlist == file_list

    file_index=[['>@r4', '>@r2', '>@r3'],['>@r8', '>@r5', '>@r7'],['>@r6', '>@r1']]
    i=0
    for filename in testlist:
        index=[]
        with open (filename) as f:
            for line in f :
                if line.startswith('>'):
                    line = line.strip()
                    index.append(line)
                else:
                    pass
        assert index==file_index[i]
        i+=1

   
    
 
   
