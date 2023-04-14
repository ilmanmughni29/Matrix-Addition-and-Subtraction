# Program penjumlahan dan pengurangan matriks tanpa numpy

print("masukkan jumlah baris dan kolom matriks 1:\n", end="")
rowOne = int(input())
colOne = int(input())
print("masukkan jumlah baris dan kolom matriks 2:\n", end="")
rowTwo = int(input())
colTwo = int(input())

if rowOne==rowTwo and colOne==colTwo:
    matOne = []
    print("\nmasukkan", rowOne*colOne, "angka untuk matriks 1:\n", end="")
    for i in range(rowOne):
        matOne.append([])
        for j in range(colOne):
            num = int(input())
            matOne[i].append(num)

    matTwo = []
    print("\nmasukkan", rowTwo*colTwo, "angka untuk matriks 2:\n", end="")
    for i in range(rowTwo):
        matTwo.append([])
        for j in range(colTwo):
            num = int(input())
            matTwo[i].append(num)

    matThree = []
    for i in range(rowOne):
        matThree.append([])
        for j in range(colTwo):
            sub = matOne[i][j] - matTwo[i][j]
            matThree[i].append(sub)
            
    matFour = []
    for i in range(rowOne):
        matFour.append([])
        for j in range(colTwo):
            matFour[i].append(matOne[i][j]+matTwo[i][j])

    print("\nhasil pengurangan:")
    for i in range(rowOne):
        for j in range(colOne):
            print(matThree[i][j], end=" ")
        print()
        
    print("\nhasil penjumlahan:")
    for i in range(rowOne):
        for j in range(colOne):
            print(matFour[i][j], end=" ")
        print()
    
else:
    print("\nOrdo tidak sama!")
