# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:38:30 2020

@author: ASUS
"""
import sys
fasta={}
with open ("practice.fasta.txt") as f:
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
        
    #sort
    
    #seq
    fasta = sorted(fasta.items(),key=lambda i:i[1]) 
    #id
    #fasta = sorted(fasta.items(),key=lambda i:i[0]) 
    #seqlength
    #fasta = sorted(fasta.items(),key=lambda i:len(i[1])) 
    print(fasta)
    