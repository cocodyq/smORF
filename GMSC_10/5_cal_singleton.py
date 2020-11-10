def cal_number(infile,outfile):
    seq={}
    out=open(outfile, "w")
    with open (infile) as f1:
        for line in f1 :
            line = line.strip()
            linelist=line.split("\t")
            if linelist[1] not in seq.keys():
                seq[linelist[1]]=int(linelist[0])
            else:
                seq[linelist[1]]+=int(linelist[0])
        for key,value in seq.items():
                out.write(str(value)+"\t"+key+"\n")
    out.close()
if __name__ == '__main__': 
    import sys
    import os
    infile="/home1/duanyq/GMSC_10/allnumber.txt"
    outfile="/home1/duanyq/GMSC_10/allnumber_dedup.txt"
    cal_number(infile,outfile)
