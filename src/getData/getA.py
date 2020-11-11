import socket
import dns.resolver
from time import sleep

file = open("../../data/top1A.txt", "r")
output = open("../../data/A-400K.txt", "w+")
i = 0



#print("Done with the file")
for line in iter(file.readline, b''):
    line = line.strip("\n")
    #print(line)
    try:
        query = dns.resolver.query(line, "A")
        #print(query[0])
        output.write(line + " " + str(query[0])+ "\n")
    except:
        continue
    #exit(0)

    i+=1
    if(i % 10000 ==0): print (str(i) + " records completed")
    if(i>400000): break
print("done")

