def split(infile,outfile):
    name = set()
    n = 1
    m = 1
    x = 1
    with open (infile) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t") 
            if linelist[0] not in name:
                name.add(linelist[0])
                if x > 300:
                    m += 1
                    x = 1
                if m > 300:
                    n += 1
                    m = 1
                    x = 1
                out = open(outfile+"first"+str(n)+"/second"+str(m)+"/"+linelist[0]+".fna", "w")
                out.write(">"+linelist[1]+"\n"+linelist[2]+"\n")
                x += 1
            else:
                out.write(">"+linelist[1]+"\n"+linelist[2]+"\n")

    out.close()                  
        
infile = "RNAcode_result/all_0.5_0.9_filt_fna_order.tsv"
outfile = "RNAcode_result/split/"
split(infile,outfile)
