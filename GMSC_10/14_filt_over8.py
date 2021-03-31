def filteight(infile,outfile):    
    allname = {}
    out = open(outfile, "w")
    with open (infile) as f1:
        for line in f1 :
            line = line.strip("\n")
            linelist = line.split("\t")
            if linelist[2] != "":
                if linelist[2] in allname.keys():
                    allname[linelist[2]][1] += 1
                    allname[linelist[2]][0].append(linelist[0])
                else:
                    allname[linelist[2]] = [[linelist[0]], 1]
    
    for key,(namelist,count) in sorted(allname.items(), key=lambda item:item[1][1]):
        if count >= 8:
            for i in range(len(namelist)):
                out.write(key+"\t"+namelist[i]+"\n")
    out.close() 

    
infile = "clust_result/result/all_0.5_0.9.tsv"
outfile = "clust_result/result/all_0.5_0.9_filt.tsv"
filteight(infile,outfile)
