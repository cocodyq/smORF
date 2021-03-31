def addseq(infile1,infile2,output):
    import lzma
    name = {}
    out = open(outfile, "w")
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")    
            name[linelist[1]] = linelist[0]
            
    with lzma.open(infile2, 'rt') as f2:
        for line in f2:
            line = line.strip()
            if line.startswith(">"):
                index = line.strip(">")
            else:
                if index in name.keys():
                    out.write(name[index]+"\t"+index+"\t"+line+"\n")
    out.close()                  
        
infile1 = "clust_result/result/all_0.5_0.9_filt.tsv"
infile2 = "data/GMSC.ProGenomes2.smorfs.fna.xz"
infile3 = "data/GMSC10.metag_smorfs.fna.xz"
outfile1 = "RNAcode_result/all_0.5_0.9_filt_progfna.tsv"
outfile2 = "RNAcode_result/all_0.5_0.9_filt_metagfna.tsv"
addseq(infile1,infile2,outfile1)
addseq(infile1,infile3,outfile2)
