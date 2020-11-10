def extract(infile,outfile):    
    resultlist=random.sample(range(1,232030377),1000)
    resultdict={}
    for i in range(1000):
        resultdict[resultlist[i]]=""
    out=open(outfile,"w")
    n=0
    for seq_record in SeqIO.parse(infile, "fasta"):
       n+=1
       if n in resultdict.keys():
           out.write(f'>{seq_record.id}\n{seq_record.seq}\n')
    out.close()
    
if __name__ == '__main__': 
    import Bio
    from Bio import SeqIO
    import random

    infile="/home1/duanyq/GMSC_10/linclust/0.9/0.9clu_singleton.faa"
    outfile="/home1/duanyq/GMSC_10/linclust/0.9/0.9clu_singleton_1000.faa"
    extract(infile,outfile)
