import RadSort
with open('in.txt', 'r') as f:
    lines = [line.strip() for line in f]

result = list(map(int, lines))
res = list(map(int, RadSort.keker(result)))

with open('out.txt', 'w') as f:
    f.writelines(f"{item}\n" for item in res)
