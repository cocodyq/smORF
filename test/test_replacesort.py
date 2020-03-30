import sys
import os
import pytest
import re
#split inputfile according to X
def splitseq(infile,X):
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
            #pattern1=re.compile(r'[ND]')
            pattern2=re.compile(r'[KE]')
            #pattern3=re.compile(r'[TSQ]')
            #pattern4=re.compile(r'[YF]')
            pattern5=re.compile(r'[LIV]')
            #line=re.sub(pattern1,'N',line)
            line=re.sub(pattern2,'K',line)
            #line=re.sub(pattern3,'T',line)
            #line=re.sub(pattern4,'Y',line)
            line=re.sub(pattern5,'L',line)
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
    splitseq('./data/test_replacesort.fasta',3)
    file_list=["./output/split1.fasta","./output/split2.fasta","./output/split3.fasta","./output/split4.fasta"]
    file_index=[['>@r2', '>@r1.1'],['>@r3(2)'],['>@r5(1)','>@r4'],['>@r6','>@r5']]
    file_seq=[['MNKHYADTFYCHLLASQWLLMALLLMNKHYADTFYCHLLAKKSTFYCHLLA','NDKKRHCTSQYFWALLLMNKHYADKCFLRTSQWLLM'],
    ['MNKHYADTFYCHLLATFYCHLLAKKSTFYCHLLAALLN'],['ASQWLLMCHLLASQWLLMALLLMNKHYADTFYCHLLAKKSWLLMHYADTFYCHLLASQWLLMALLLMNKHYADTFYCHLLPPGG','MNKHYADTFYCHLLASQWLLMALLLMNKHYADTFYCHLLAKKSTFYCHLLA'],
    ['ASQWLLMCHLLASQWLLMALLLMNKHYADTFYCHLLAKKSWLLMHYADTFYCHLLASQWLLMALLLMNKHYADTFYCHLLPPGG','MNKHYADTFYCHLLAKKSWLLMHYADTFYCHLLASQWLLMALLLMNKHYADTFYCHLLGGGPPP']]
    for i in range(len(file_list)):
        sortseq(file_list[i])
    j=0
    for filename in file_list:
        index=[]
        seq=[]
        with open (filename) as f:
            for line in f :
                line = line.strip()
                if line.startswith('>'):
                    index.append(line)
                else:
                    seq.append(line)
        assert index==file_index[j]
        assert seq==file_seq[j]
        j+=1
