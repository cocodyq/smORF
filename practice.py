# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:20:33 2020

@author: ASUS
"""
def sortlist(L):
    L=L.sort()
    
def mergelist(outlist):
    mediumlist=[]
    resultfile="result_medium"
    global circle
    circle+=1
    no=1
    i=0
    while i < len(outlist)-1:
        mediumfile=resultfile+str(circle)+'_'+str(no)
        mediumlist.append(mediumfile)
        rm = open(mediumfile, "w")
        out_1=open(outlist[i],"r")
        out_2=open(outlist[i+1],"r")
    
        i+=2
        number=[]
        line1=out_1.readline()
        number.append(int(line1))
        line2=out_2.readline()
        number.append(int(line2))
        while(True):
            if number[0] <= number[1]:
                rm.write(str(number[0])+'\n')
                line1=out_1.readline()
                if len(line1)==0:
                    break
                number[0]=(int(line1)) 
            else:
                rm.write(str(number[1])+'\n')
                line2=out_2.readline()
                if len(line2)==0:
                    break
                number[1]=(int(line2))    
        if len(line1)==0:
            rm.write(line2)
            while(True):
                line2=out_2.readline()
                rm.write(line2)
                if len(line2)==0:
                    break  
        if len(line2)==0:
            rm.write(line1)
            while(True):
                line1=out_1.readline()
                rm.write(line1)
                if len(line1)==0:
                    break
        no+=1
        out_1.close()
        out_2.close()
        rm.close()
    mediumfile=resultfile+str(circle)+'_'+str(no)
    if i<len(outlist):
        mediumlist.append(mediumfile)
        shutil.copyfile(outlist[i], mediumfile)
    out_1.close()
    out_2.close()
    rm.close()
    if len(mediumlist)!=1:
        mediumlist=mergelist(mediumlist)
    return mediumlist
        
if __name__ == '__main__':
    import os
    import sys
    import shutil

    threshold=5
    n = 0
    nth = 1
    L = []
    outList = []
    circle=0
    #输入文件，分割文件
    with open('practice.txt', "rt") as all:
        for line in all:
            if (n == 0):
                outfile = 'practice_out' + str(nth)
                outList.append(outfile)
                print ('sorting ' + outfile)
                try:
                    outp = open(outfile, "w")#打开分割文件
                except:
                    print ("unable to write file " + outfile)
            L.append(int(line))
            n += 1#计数
            if n >= threshold:
                sortlist(L)
                for x in L:
                    outp.write(str(x)+'\n')
                n=0
                L=[]
                nth += 1
                outp.close()
    if n > 0:
        sortlist(L)
        for x in L:
            outp.write(str(x)+'\n')
        outp.close() 
    result=mergelist(outList)
    print(result)
    


        
    