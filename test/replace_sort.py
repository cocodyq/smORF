# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:30:32 2020

@author: ASUS
"""

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
            outfile="D:/project/output3/split"+str(i+1)+".fasta"
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

#merge every sorted and splited file
def merge_sortseq(sortout):
    mediumlist=[]
    resultfile="D:/project/output3/medium"
    global circle
    circle+=1
    no=1
    i=0
    while i < len(sortout)-1:
        merge={}
        mediumfile=resultfile+str(circle)+'_'+str(no)+".fasta"
        mediumlist.append(mediumfile)
        mediumf = open(mediumfile, "w")
        merge1=open(sortout[i],"r")
        merge2=open(sortout[i+1],"r")
        i+=2
        #store first seq in every file in dictionary
        info1=merge1.readline().strip()
        seq1=merge1.readline().strip()
        info2=merge2.readline().strip()
        seq2=merge2.readline().strip()
        if info1==info2:
            info2=info2+"(1)"        
        if seq1 != seq2:
            merge[info1]=seq1
            merge[info2]=seq2
        else:
            info1=merge1.readline().strip()
            seq1=merge1.readline().strip()
            if info1==info2:
                info2=info2+"(1)"   
            merge[info1]=seq1
            merge[info2]=seq2
    
        while(True):
        #sort
            merge_sort = sorted(merge.items(),key=lambda i:i[1]) 
            mediumf.write(merge_sort[0][0]+'\n'+ merge_sort[0][1]+'\n')
        
            key=merge_sort[0][0]
            merge.pop(merge_sort[0][0])
        #store next seq
            if key == info1:
                info1=merge1.readline().strip()
                seq1=merge1.readline().strip()
                if info1 in merge.keys():
                    info1=info1+"(1)"
                if seq1 in merge.values():
                    info1=merge1.readline().strip()
                    seq1=merge1.readline().strip()
                    if info1 in merge.keys():
                        info1=info1+"(1)"
                    if seq1:
                        merge[info1]=seq1
                    else:
                        break
                else:
                    if seq1:
                        merge[info1]=seq1
                    else:
                        break
                
            if key == info2:
                info2=merge2.readline().strip()
                seq2=merge2.readline().strip()
                if info2 in merge.keys():
                    info2=info2+"(1)"  
                if seq2 in merge.values():
                    info2=merge2.readline().strip()
                    seq2=merge2.readline().strip()
                    if info2 in merge.keys():
                        info2=info2+"(1)"
                    if seq2:
                        merge[info2]=seq2
                    else:
                        break
                else:
                    if seq2:
                        merge[info2]=seq2
                    else:
                        break
        while info1:
            mediumf.write(info1+'\n'+seq1+'\n') 
            info1=merge1.readline().strip()
            seq1=merge1.readline().strip()
        while info2:
            mediumf.write(info2+'\n'+seq2+'\n') 
            info2=merge2.readline().strip()
            seq2=merge2.readline().strip()
        no+=1
        mediumf.close()
        merge1.close()
        merge2.close()
    #change the name of last file    
    mediumfile=resultfile+str(circle)+'_'+str(no)+".fasta"
    if i<len(sortout):
        mediumlist.append(mediumfile)
        shutil.copyfile(sortout[i], mediumfile)
    mediumf.close()
    merge1.close()
    merge2.close()   
    if len(mediumlist)!=1:
        mediumlist=merge_sortseq(mediumlist)
    return mediumlist
    
if __name__ == '__main__':            
    import sys
    import os
    import shutil
    import re
    #X=3 #X is the number of sequences in next every splited file
    circle=0
    inputfile="D:/project/data/test.fasta"
    #split inputfile according to X
    outl=splitseq(inputfile,3)
    #sort every splited file
    for i in range(len(outl)):
        sortseq(outl[i])
    #merge every sorted and splited file
    resultlist=merge_sortseq(outl)  
    result="D:/project/output3/replace_17.fasta"
    shutil.copyfile(resultlist[0],result)

