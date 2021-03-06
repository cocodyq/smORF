import sys
import os
import pytest

def getmore(infile):
    fasta={}
    fa_term=[]
    with open (infile) as f:
        for line in f:
            line=line.strip()
            if line[0]=='>':
                if fa_term:
                    seq=''.join(fa_term)
                    if seq in fasta.keys():
                        fasta[seq][0]+=1
                    else:
                        fasta[seq]=[1]
                        fasta[seq].append(ID)
                    
                    fa_term=[]
                ID=line 
            else:
                fa_term.append(line)
        seq=''.join(fa_term)
        if seq in fasta.keys():
            fasta[seq][0]+=1
        else:
            fasta[seq]=[1]
            fasta[seq].append(ID)
    outfile="./data/moreseq.fasta"
    out=open(outfile,"w")
    for key,value in fasta.items():
        if value[0]>1:
            out.write(value[1]+"\n")
            out.write(key+"\n")
    out.close()
    return outfile

def test_getmore():
    infile="./data/practice.fasta"
    testfile=getmore(infile)
    in_index1=[">@r3",">@r6"]
    in_index2=[">@r6",">@r3"]
    out_index=[]
    with open (testfile) as f:
        for line in f:
            line=line.strip()
            if line[0]=='>':
                out_index.append(line)
            else:
                pass
        assert out_index==in_index1 or out_index==in_index2
