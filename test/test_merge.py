import sys
import os
import pytest
import shutil
circle=0

#merge every sorted and splited file
def merge_sortseq(sortout):
    mediumlist=[]
    resultfile="D:/project/output/medium"
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
        if seq1 != seq2:
            merge[info1]=seq1
            merge[info2]=seq2
        else:
            info1=merge1.readline().strip()
            seq1=merge1.readline().strip()
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
                if seq1 in merge.values():
                    info1=merge1.readline().strip()
                    seq1=merge1.readline().strip()
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
                if seq2 in merge.values():
                    info2=merge2.readline().strip()
                    seq2=merge2.readline().strip()
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

def test_mergeseq():
    file_list=["D:/project/output/split1.fasta","D:/project/output/split2.fasta","D:/project/output/split3.fasta"]
    merge_list=["D:/project/output/medium2_1.fasta"]
    testlist=merge_sortseq(file_list)
    assert testlist == merge_list

    file_index=['>@r5', '>@r6', '>@r7','>@r2', '>@r4', '>@r8']
    index=[]
    with open (testlist[0]) as f:
        for line in f :
            if line.startswith('>'):
                line = line.strip()
                index.append(line)
            else:
                pass
    assert index==file_index
        
