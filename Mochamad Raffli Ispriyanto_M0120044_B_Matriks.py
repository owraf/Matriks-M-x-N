ulang = True
while ulang:
    # menu operasi
    print()
    print('---------------------------------')
    print('SELAMAT DATANG DI PROGRAM MATRIKS')
    print('---------------------------------')
    print()
    print('>>>>>> SILAHKAN PILIH MENU <<<<<<')
    print()
    print('---------------------------------')
    print('1. penjumlahan matriks')
    print('2. pengurangan matriks')
    print('3. perkalian matriks')
    print('4. selesai')
    print('---------------------------------')

    choice = int(input('Masukan pilihan (1/2/3/4) : '))
    while choice > 4 or choice < 1:
        print('pilihan salah, masukkan ulang')
        choice = int(input('Masukan pilihan(1/2/3/4) : '))
        
    if choice == 1 :
        R=int(input('Jumlah baris : '))
        S=int(input('Jumlah kolom : '))
        x = []
        print('matriks1 : ')
        for i in range(R):
            a = []
            for j in range(S):
                a.append(int(input()))
            x.append(a)
        for i in range(R):
            for j in range(S):
                print(x[i][j],end=' ')
            print()
        print(' ')
        T=int(input('Jumlah baris : '))
        U=int(input('Jumlah kolom : '))
        y = []
        print('matriks2 : ')
        for c in range(T):
            b = []
            for d in range(U):
                b.append(int(input()))
            y.append(b)
        for c in range(T):
            for d in range(U):
                print(y[c][d],end=' ')
            print()
        print(' ')
        for m in range(0,len(x)):
            for n in range(0,len(x[0])):
                print(x[m][n]+y[m][n],end=' ')
            print()

    elif choice == 2 :
        R=int(input("Jumlah baris : "))
        C=int(input("Jumlah kolom : "))
        x = []
        print("matriks1 :")
        for i in range(R):
            a = []
            for j in range(C):
                a.append(int(input()))
            x.append(a)

        for i in range(R):
            for j in range(C):
                print(x[i][j],end = " ")
            print()
        print(' ')

        A=int(input("Jumlah baris : "))
        B=int(input("Jumlah kolom : "))
        y = []
        print("matriks2:")
        for d in range(A):
            b = []
            for e in range(B):
                b.append(int(input()))
            y.append(b)
        #For printing the matrix
        for d in range(A):
            for e in range(B):
                print(y[d][e],end = " ")
            print()
        print(' ')

        for m in range(0,len(x)):
                for n in range(0,len(x[0])):
                        print(x[m][n] - y[m][n], end = " ")
                print()
    
    elif choice == 3 :
        a=int(input("jumlah baris : "))
        b=int(input("jumlah kolom : "))
        matriks1 = []
        print("matriks1 : ")

        for i in range (a):
            p=[]
            for j in range (b):
                p.append(int(input()))
            matriks1.append(p)

        print("matriks1")
        for i in range (a):
            for j in range (b):
                print(matriks1[i][j], end="")
            print()

        matriks2 = []
        print("matriks2 : ")

        for i in range (a):
            q=[]
            for j in range (b):
                q.append(int(input()))
            matriks2.append(q)

        print("matriks2")
        for i in range (a):
            for j in range (b):
                print(matriks2[i][j], end="")
            print()

        matriks3 = []
        print("matriks3 : ")
        for i in range (a):
            r=[]
            for j in range (b):
                r.append(int(input()))
            matriks3.append(r)

        print("matriks3")
        for i in range (a):
            for j in range (b):
                print(matriks3[i][j], end="")
            print()
        print("Hasil penjumlahan matriks")
        for i in range(0,len(matriks1)):
            for j in range(0,len(matriks1[0])):
                print(matriks1[i][j]+matriks2[i][j], end="")
            print()
        print("Hasil perkalian matriks")
        for i in range(0,len(matriks1)):
            for j in range(0,len(matriks2)):
                for k in range(0,len(matriks2)):
                    matriks3[i][j]+=(matriks1[i][k]*matriks2[k][j])
                print(matriks3[i][j], end="")
            print()
        
    elif choice == 4:
        ulang = False
    print('')
    print('operasi matriks telah selesai')