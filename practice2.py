# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:40:34 2020

@author: ASUS
"""
#sort
def sortseq(out):
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

#merge
def merge_sortseq(sortout):
    mediumlist=[]
    resultfile="medium"
    global circle
    circle+=1
    no=1
    i=0
    while i < len(sortout)-1:
        merge={}
        mediumfile=resultfile+str(circle)+'_'+str(no)
        mediumlist.append(mediumfile)
        print(mediumlist)
        mediumf = open(mediumfile, "w")
        merge1=open(sortout[i],"r")
        merge2=open(sortout[i+1],"r")
        i+=2
        info1=merge1.readline().strip()
        seq1=merge1.readline().strip()
        merge[info1]=seq1
        info2=merge2.readline().strip()
        seq2=merge2.readline().strip()
        merge[info2]=seq2
        print(merge)
    
        while(True):
        
            merge_sort = sorted(merge.items(),key=lambda i:i[1]) 
    
            mediumf.write(merge_sort[0][0]+'\n'+ merge_sort[0][1]+'\n')
        
            key=merge_sort[0][0]
            merge.pop(merge_sort[0][0])
    
            if key == info1:
                info1=merge1.readline().strip()
                seq1=merge1.readline().strip()
                if info1:
                    merge[info1]=seq1
                else:
                    break
            if key == info2:
                info2=merge2.readline().strip()
                seq2=merge2.readline().strip()
                if info2:
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
    if len(mediumlist)!=1:
        mediumlist=merge_sortseq(mediumlist)
    return mediumlist
    
if __name__ == '__main__':            
    import sys
    #split
    X=2
    fa_info = []
    fa_term = []
    fa_seq=[]
    fa_num = 0
    outlist=[]
    circle=0
    with open ("practice.fasta.txt") as f:
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
        if (fa_num%2) == 0:
            file_num=fa_num//X
        else:
            file_num = fa_num//X+1
        for i in range(file_num):
            outfile="split"+str(i+1)+".fasta"
            out1=open(outfile, "w")
            outlist.append(outfile)
            start=i*X
            end=(i+1)*X
            if end > fa_num:
                end=fa_num
            #print(start,end,file_num)
            for j in range(start,end,1):
                out1.write(fa_info[j]+"\n")
                out1.write(fa_seq[j]+"\n")
            out1.close()
    for i in range(len(outlist)):
        sortseq(outlist[i])
    resultlist=merge_sortseq(outlist)  
    print(resultlist)