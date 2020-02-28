import sys
import os
import pytest

#sort every splited file
def sortseq(out):
    ##open inputfile and store FASTA in the dictionary according to ID and seq
    fasta={}
    f=open(out, "r")
    for line in f :
        line = line.strip()
        if line.startswith('>'):
            ID=line
            fasta[ID]=[]
        else:
            fasta[ID].append(line)
            
    #duplicate     
    for key , value in list(fasta.items()):
        seq=''.join(value)
        if seq in fasta.values():
            fasta.pop(key)
            continue
        fasta[key]=seq
    
    #sort seq
    fasta = sorted(fasta.items(),key=lambda i:i[1]) 
    f.close() 
    sort = open(out,"w")
    for i in range(len(fasta)):
        sort.write(fasta[i][0]+"\n")
        sort.write(fasta[i][1]+"\n")
    sort.close()    

def test_sortseq():
    file_list=["./output/split1.fasta","./output/split2.fasta","./output/split3.fasta"]
    file_index=[['>@r3', '>@r2', '>@r4'],['>@r5', '>@r7', '>@r8'],['>@r6']]
    for i in range(len(file_list)):
        sortseq(file_list[i])
    j=0
    for filename in file_list:
        index=[]
        with open (filename) as f:
            for line in f :
                if line.startswith('>'):
                    line = line.strip()
                    index.append(line)
                else:
                    pass
        assert index==file_index[j]
        j+=1
