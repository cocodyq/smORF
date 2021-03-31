def join(infile1,infile2,infile3,outfile):
    import gzip
    out=open(outfile, "w")
    query={}
    subject={}
    with gzip.open(infile1,"rt") as f1:
        for line in f1:
            if line.startswith(">"):
                line = line.strip()
                index = line.strip(">")
            else:
                line = line.strip()
                query[index]=str(len(line))          
    with open(infile2) as f2:
        for line in f2:
            if line.startswith(">"):
                line = line.strip()
                index = line.strip(">")
            else:
                line = line.strip()
                subject[index]=str(len(line))
    
    with open(infile3) as f3:
        for line in f3:
            line = line.strip()
            linelist = line.split("\t")
            out.write(linelist[0]+"\t"+query[linelist[0]]+"\t"+linelist[1]+"\t"+subject[linelist[1]]+"\t"+linelist[2]+"\t"+linelist[3]+"\t"+linelist[10]+"\n")
    out.close()

infile2="/home1/duanyq/GMSC/clust_result/0.5_result/metag_ProG_nonsingleton_0.5_clu_rep.faa"
for i in range(24):
  infile1="/home1/duanyq/GMSC/diamond/split/sub"+str(i)+".faa.gz"
  infile3="/home1/duanyq/GMSC/diamond/result/sub"+str(i)+".faa.gz.tsv"
  outfile="/home1/duanyq/GMSC/diamond/analysis/sub"+str(i)+".faa.gz.tsv.tmp.1"
  join(infile1,infile2,infile3,outfile)
