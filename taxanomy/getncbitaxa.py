# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:58:05 2020

@author: ASUS
"""

def getname(name_in_file,name_out_file):
    out=open(name_out_file, "w")
    with open (name_in_file) as f1:
        for line in f1 :
            line = line.strip()
            number=line.split("|")[0].strip()
            name=line.split("|")[1].strip()
            sciname=line.split("|")[3].strip()
            if sciname == "scientific name":
                out.write(number+"\t"+name+"\n")
    out.close() 
def getnode(node_in_file,node_out_file):
    out=open(node_out_file, "w")
    with open (node_in_file) as f2:
        for line in f2 :
            line = line.strip()
            number=line.split("|")[0].strip()
            last=line.split("|")[1].strip()
            rank=line.split("|")[2].strip()
            out.write(number+"\t"+last+"\t"+rank+"\n")
    out.close() 
def join_node_name(node_infile,name_infile,node_name_outfile):
    in_node= pd.read_table(node_infile,sep='\t')
    in_node.columns=['number','last','rank'] 
    in_name= pd.read_table(name_infile,sep='\t')
    in_name.columns=['number','name'] 
    node_name=pd.merge(in_node,in_name,on=['number'],how='left')
    node_name.to_csv(path_or_buf=node_name_outfile, sep='\t', index=False)

if __name__ == '__main__': 
    import sys
    import os
    import pandas as pd
    nameinfile="/share/yiqian/progenome/names.dmp"
    nodeinfile="/share/yiqian/progenome/nodes.dmp"
    nameoutfile="/share/yiqian/progenome/scinames.txt"
    nodeoutfile="/share/yiqian/progenome/nodes.txt"
    nodename="/share/yiqian/progenome/nodes_names.txt"
    getname(nameinfile,nameoutfile)
    getnode(nodeinfile,nodeoutfile)
    join_node_name(nodeoutfile,nameoutfile,nodename)
