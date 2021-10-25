"""
    The Grid Search
    Difficulty: ✰✰

    Diberikan sebuah array yang berisikan string, dimana setiap string merupakan
    kumpulan angka, temukan apakah pola angka tertentu (kita sebut dengan pattern)
    muncul di dalam array tersebut (kita sebut dengan grid). Sebagai contoh,
    perhatikan grid berikut ini.

    1 2 3 4 5 6 7 8 9 0
    0 9 8 7 6 5 4 3 2 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    2 2 2 2 2 2 2 2 2 2

    Lalu diberikan pattern seperti berikut.

    8 7 6 5 4 3
    1 1 1 1 1 1
    1 1 1 1 1 1

    Pattern di atas dimulai dari baris kedua dan kolom ketiga pada grid dan
    berlanjut hingga dua baris sesudahnya. Sehingga pattern tersebut dapat
    dikatakan ada di dalam grid. Return value harus 'YES' atau 'NO', tergantung
    pada apakah pattern dapat ditemukan atau tidak di dalam grid. Dalam kasus
    di atas, return 'YES'.
    
    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan 'YES' jika pattern muncul di
    dalam grid, dan sebaliknya, kembalikan 'NO' jika pattern tidak ditemukan.
    Fungsi akan memiliki parameter sebagai berikut.
    - G, array of strings, merepresentasikan grid
    - P, array of strings, merepresentasikan pattern

    Format Input:
    Input di baris pertama adalah t, sebuah integer yang merupakan jumlah kasus
    yang akan diuji. Setiap kasus yang diuji akan memiliki input sebagai berikut:
    - Input pertama adalah R dan C, yaitu dua buah integer yang dipisahkan dengan
      spasi, merupakan jumlah baris dan kolom dari grid G.
    - Input selanjutnya adalah R baris, masing-masing baris berisi string yang
      terdiri dari angka sebanyak C digit, merupakan elemen dari grid G.
    - Input ketiga adalah r dan c, yaitu dua buah integer yang dipisahkan dengan
      spasi, merupakan jumlah baris dan kolom dari pattern P.
    - Input selanjutnya adalah r baris, masing-masing baris berisi string yang
      terdiri dari angka sebanyak c digit, merupakan elemen dari pattern P.

    Format Output:
    Output yaitu string 'YES', jika pattern P dapat ditemukan di dalam grid G,
    atau 'NO', jika pattern P tidak dapat ditemukan di dalam grid G. Satu output
    untuk satu kasus yang diuji.

    Contoh Input:
    2
    6 6
    903731
    120128
    812831
    002100
    037812
    905611
    3 2
    12
    83
    10
    5 5
    09090
    90909
    09090
    90909
    09090
    2 2
    90
    90

    Contoh Output:
    YES
    NO

    Penjelasan:
    Pada kasus pertama, pattern dapat ditemukan di dalam grid, mulai dari baris
    kedua dan kolom keempat, berlanjut hingga dua baris sesudahnya. Kembalikan 'YES'
    Pada kasus kedua, pattern tidak dapat ditemukan di dalam grid. Kembalikan 'NO'
"""

def gridSearch(G, P):
    status = False
    first_row_P = P[0]
    possible_index = [i for i in range(len(G)) if G[i].find(first_row_P) != -1 and i <= len(G)-len(P)]

    if len(possible_index) > 0:

        for index in possible_index:
            start = getIndexes(G[index], first_row_P)
            for i in range(1, len(P)):
                if len(start.intersection(getIndexes(G[index+i], P[i]))) == 0: break
            else:
                status = True
                break

    return 'YES' if status else 'NO'

def getIndexes(st, sub):
    indexes = set()
    bound = 0

    while True:
        res = st[bound:].find(sub)
        if res == -1: break
        else:
            indexes.add(res+bound)
            bound = res+bound+1

    return indexes

t = int(input())
result = []

for _ in range(t):
    R, C = list(map(int, input().split()))
    G = []

    for __ in range(R):
        G.append(input())

    r, c = list(map(int, input().split()))
    P = []

    for __ in range(r):
        P.append(input())

    result.append(gridSearch(G, P))

print('\n'.join(result))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 08/02/2021
"""
