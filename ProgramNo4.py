def angkaganjil(n):
    print(f"Masukkan angka ganjil sampai {n}:")
    for i in range(1, n + 1, 2):  
        print(i, end=" ")
    print()  


n = int(input("Masukkan nilai n: "))

angkaganjil(n)
