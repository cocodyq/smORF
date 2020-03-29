import sys
import os
import pytest
#sort every splited file
def sortseq(out):
    ##open inputfile and store FASTA in the dictionary according to ID and seq
    fasta={}
    f=open(out, "r")
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
    sort = open(out,"w")
    for i in range(len(fasta)):
        sort.write(fasta[i][1]+"\n")
        sort.write(fasta[i][0]+"\n")
    sort.close()    

def test_sortseq():
    file_list=["./output/split1.fasta","./output/split2.fasta","./output/split3.fasta"]
    file_index1=[['>@r3', '>@r2', '>@r4'],['>@r5', '>@r7', '>@r8'],['>@r6']]
    file_index2=[['>@r3', '>@r2', '>@r4'],['>@r5', '>@r7', '>@r8'],['>@r1']]
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
        assert index==file_index1[j] or index==file_index2[j]
        j+=1
