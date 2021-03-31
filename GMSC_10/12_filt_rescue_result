#filt rescued singletons with clusters they belong to based on best e-value

def filt(infile,outfile):
    lineset = set()
    out = open(outfile, "w")
    with open (infile) as f1:
        for line in f1 :
            line = line.strip()
            linelist = line.split("\t")
            if linelist[0] in lineset:
                continue
            else:
                lineset.add(linelist[0])
                out.write(linelist[0]+"\t"+linelist[2]+"\n")
    out.close()

for i in range(24):
    infile1="diamond/analysis/analysis_0.5/sub"+str(i)+".faa.gz.tsv.tmp.3"
    infile2="diamond/analysis/analysis_0.9/sub"+str(i)+".faa.gz.tsv.tmp.3"
    outfile3="diamond/analysis/analysis_0.5/sub"+str(i)+".faa.gz.tsv.tmp.4"
    outfile4="diamond/analysis/analysis_0.9/sub"+str(i)+".faa.gz.tsv.tmp.4"
    filt(infile1,outfile3)
    filt(infile2,outfile4)
