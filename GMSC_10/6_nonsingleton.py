def nonsingle(infile,outfile):
    out=open(outfile, "w")
    with open (infile) as f1:
        for line in f1 :
            line = line.strip()
            linelist=line.split("\t")
            if linelist[0]!="1":
                out.write(linelist[1]+"\n")
    out.close()
if __name__ == '__main__': 
    import sys
    import os
    infile="/home1/duanyq/GMSC_10/allnumber_dedup.txt"
    outfile="/home1/duanyq/GMSC_10/nonsingleton.txt"
    nonsingle(infile,outfile)
