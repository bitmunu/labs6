fin = open("input.txt", "r")
s = fin.readline()
a = list(map(int, s.split()))
fin.close()

multi = 1
for i in a:
    multi = multi * i

fout = open("output.txt", "w")
fout.write(repr(multi))
fout.close()
print("SUCCESS")