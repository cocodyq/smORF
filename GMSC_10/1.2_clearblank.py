def clearBlankLine():
    file1 = open('/home1/duanyq/GMSC_10/submetag5.faa', 'r') 
    file2 = open('/home1/duanyq/GMSC_10/sub_metag5.faa', 'w')
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()
