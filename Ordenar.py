n = []
n1 = []
want = "y"
i = 0
while want == "y":
    n.append(int(input("Write a number : ")))
    want = input("You want write more numbers ? ")
print("Original Sequence: ")
print(n)
OrigVectorSize = len(n)
while len(n1) != OrigVectorSize:
    while i < len(n):
        cont = 0
        for ii in range(0, len(n)):
            if n[i] <= n[ii]:
                cont = cont + 1
        if cont == len(n):
            n1.append(n[i])
            n.remove(n[i])
            i = 0
        else:
            i = i + 1
print("New Sequence: ")
print(n1)