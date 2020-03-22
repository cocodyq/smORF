import sys
import os
import pytest

def do_tsv(infile):
    index={}
    fa_term=[]
    infoseq={}
    num=1
    with open (infile) as f:
        for line in f :
            line = line.strip()
            if line[0]=='>':    
                if fa_term:
                    seq=''.join(fa_term)
                    fa_term=[]
                    if seq in infoseq.keys():
                        infoseq[seq].append(ID)
                    else:
                        infoseq[seq]=[]
                        infoseq[seq].append(ID)
                if line in index.keys():
                    line=line+"("+str(num)+")"
                    num+=1
                else:
                    index[line]=''
                ID=line
            else:
                fa_term.append(line)
        seq=''.join(fa_term)
        if seq in infoseq.keys():
            infoseq[seq].append(ID)
        else:
            infoseq[seq]=[]
            infoseq[seq].append(ID)
    outfile="./output/test.tsv"
    out=open(outfile,"w")
    for value in infoseq.values():
        for i in range(len(value)):
            out.write(value[0]+"\t"+value[i]+"\n")
    out.close()
    return outfile

def test_do_tsv():
    infile="./data/test.fasta"
    testfile=do_tsv(infile)
    i=1
    out_dic={}
    file_dic={1：['>@r1', '>@r1'],2：['>@r1', '>@r1.1'],3：['>@r2', '>@r2']}
    with open (testfile) as f:
        for line in f:
            line=line.strip()
            index=line.split('\t',1)
            out_dic[i]=index
            i+=1
        assert out_dic.values()==file_dic.values()
