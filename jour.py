fp=open("dblp50000.xml",'r')
fp1=open("BOOKtitle.csv",'w')
while True:
    line=fp.readline()
    if not line:
        break
    if "<booktitle>" in line:
        #print "hello"
        line1=line.split('>')
        #print line1[1]
        line2=line1[1].split('<')
        #print line2[0]
        fp1.write(str(line2[0])+"\n")