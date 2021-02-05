import sys
f = open(sys.argv[1],"r")
p = open(sys.argv[2],"w")
k =[]
j = 0
z = 0
for line in f.readlines():
    line = line.rstrip("\n").split("\t")
    k.append(line)
for sira in k:
    sira[0] = int(sira[0])
    sira[1] = int(sira[1])
k.sort()
p.write("Message ")
p.write(str(z+1))
p.write("\n")
for sira in k:
    sira[0] = str(sira[0])
    sira[1] = str(sira[1])
for i in range(len(k)):
    while 1:
        if k[i][0] == k [j][0]:
           p.write("\t".join(k[i]))
           p.write("\n")
           break
        else:
            j = i+1
            z = z+1
            p.write("Message ")
            p.write(str(z+1))
            p.write("\n")
            continue
f.close()
p.close()
