def order(infile1,infile2,output):
    namedict = {}
    out = open(outfile, "w")
    with open (infile1) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")   
            name = linelist[0]+"\t"+linelist[1]
            namedict[name] = linelist[2]
    with open (infile2) as f1:
        for line in f1 :
            line = line.strip()
            if line in namedict.keys():
                out.write(line+"\t"+namedict[line]+"\n")    
    out.close()                  
        
infile1 = "RNAcode_result/all_0.5_0.9_filt_fna.tsv"
infile2 = "clust_result/result/all_0.5_0.9_filt.tsv"
outfile = "RNAcode_result/all_0.5_0.9_filt_fna_order.tsv"
order(infile1,infile2,outfile)
