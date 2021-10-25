"""
    Circular Array Rotation
    Difficulty: ✰

    John Watson mengetahui sebuah operasi yang disebut dengan Circular Array
    Rotation. Operasi ini akan memindahkan elemen terakhir pada array ke posisi
    pertama pada array dan menggeser semua elemen yang tersisa ke kanan.
    Untuk menguji kemampuan Sherlock, Watson memberi Sherlock sebuah array
    yang berisi integer. Sherlock akan melakukan operasi rotasi beberapa kali
    dan setelah itu ia akan menentukan nilai elemen pada array pada posisi yang
    diminta oleh Watson.

    Diberikan sebuah array of integers, lakukan sejumlah operasi rotasi, lalu
    kemudian kembalikan nilai elemen dari array pada indeks yang diminta.

    Tugas:
    Buatlah sebuah fungsi yang akan melakukan Circular Array Rotation. Fungsi
    memiliki parameter sebagai berikut.
        - a: array of integers, array yang akan dilakukan operasi rotasi
        - k: integer, jumlah rotasi yang akan dilakukan
        - queries: array of integers, indeks pada array yang nilainya akan
          dikembalikan

    Format Input:
    Input pertama ialah sekumpulan integer yang dipisahkan dengan spasi, yang
    merupakan elemen dari array yang akan dilakukan operasi rotasi.
    Input kedua ialah integer, yaitu berapa kali operasi rotasi terhadap array
    akan dilakukan.
    Input ketiga ialah sekumpulan integer yang dipisahkan dengan spasi, yang
    merupakan indeks pada array yang nilainya akan dikembalikan.

    Format Output:
    Output ialah sekumpulan integer yang merupakan nilai dari elemen pada array
    berdasarkan indeks yang diminta.

    Contoh Input:
    3 4 5 6 7
    2
    1 2

    Contoh Output:
    7 3

    Penjelasan:
    Diketahui a = [3, 4, 5, 6, 7], k = 2, dan queries = [1, 2]

    Rotasi 1: [3, 4, 5, 6, 7] -> [7, 3, 4, 5, 6]
    Rotasi 2: [7, 3, 4, 5, 6] -> [6, 7, 3, 4, 5]

    Setelah dilakukan rotasi, diketahui nilai dari indeks ke-1 dan ke-2 dari
    array yang telah dirotasi ialah 7 dan 3.
"""

def circularArrayRotation(a, k, queries):
    k = k % len(a)    
    a = a[(k*-1):] + a[:(k*-1)]
    result = []
        
    for query in queries:
        result.append(a[query])
        
    return result

a = [int(i) for i in input().split()]
k = int(input())
queries = [int(i) for i in input().split()]

result = circularArrayRotation(a, k, queries)
print(' '.join(list(map(str, result))))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 21/01/2021
"""
