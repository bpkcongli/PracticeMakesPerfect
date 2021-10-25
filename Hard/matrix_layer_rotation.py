"""
    Matrix Layer Rotation
    Difficulty: ✰✰✰

    Diberikan sebuah matriks dua dimensi dengan ukuran M x N dan sebuah integer
    yaitu r. Kamu harus memutar/merotasi matriks tersebut sebanyak r kali dan
    tampilkan hasilnya. Rotasi harus berlawanan arah jarum jam (anti-clockwise).

    Rotasi sebuah matriks berdimensi 4 x 5 akan dijelaskan melalui penjelasan
    berikut. Perhatikan bahwa dalam sekali rotasi, kamu harus menggeser elemen
    hanya sebanyak satu langkah.

    A11 <-- A12 <-- A13 <-- A14 <-- A15
     |                               ↑
     ↓                               |
    A21     A22 <-- A23 <-- A24     A25
     |       |               ↑       ↑
     ↓       ↓               |       |
    A31     A32 --> A33 --> A34     A35
     |                               ↑
     ↓                               |
    A41 --> A42 --> A43 --> A44 --> A45

    Nilai minimum dari M dan N adalah bilangan genap.
    
    Tugas:
    Buatlah sebuah fungsi yang akan melakukan rotasi pada matriks dengan arah
    berlawanan jarum jam dan tampilkan matriks hasil rotasinya. Fungsi memiliki
    parameter sebagai berikut.
    - matrix, array dua dimensi berisikan integer, matriks yang akan dilakukan
      proses rotasi
    - r, sebuah integer, jumlah rotasi yang akan dilakukan pada matriks

    Format Input:
    Input pertama adalah M, yaitu sebuah integer yang merupakan jumlah baris
    pada matriks.
    Input kedua adalah N, yaitu sebuah integer yang merupakan jumlah kolom pada
    matriks.
    Input ketiga adalah r, yaitu sebuah integer yang merupakan jumlah rotasi
    yang akan dilakukan pada matriks.
    Input terakhir adalah M baris yang berisi N integer yang dipisahkan dengan
    spasi, merupakan elemen dari matriks yang akan dirotasi.

    Format Output:
    Output yaitu M baris yang berisi N integer yang dipisahkan dengan spasi,
    merupakan hasil dari matriks dua dimensi yang sudah dirotasi.

    Contoh Input:
    5
    4
    4
    13 2 8 7
    13 12 10 16
    13 17 16 9
    19 11 9 4
    14 8 12 5

    Contoh Output:
    16 9 4 5
    7 11 17 12
    8 9 12 8
    2 16 10 14
    13 13 13 19

    Penjelasan:
    Matriks akan dirotasi sebanyak 4 kali.
    Before            First rotation    Second Rotation
    13  2  8  7        2  8  7 16        8  7 16  9
    13 12 10 16       13 10 16  9        2 16  9  4
    13 17 16  9  -->  13 12  9  4  -->  13 10 11  5  -->
    19 11  9  4       13 17 11  5       13 12 17 12
    14  8 12  5       19 14  8 12       13 19 14  8

    Third Rotation    Fourth Rotation
     7 16  9  4       16  9  4  5
     8  9 11  5        7 11 17 12
     2 16 17 12  -->   8  9 12  8
    13 10 12  8        2 16 10 14
    13 13 19 14       13 13 13 19
"""

def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    lines = getLines(matrix, m, n)

    for i in range(len(lines)):
        for j in range(r%len(lines[i])):
            lines[i] = step(lines[i])

    matrixAfterRotation = buildMatrix(lines, m, n)
    print('\n'.join(list(map(lambda x: ' '.join(list(map(str, x))), matrixAfterRotation))))

def reverseLine(arr):
    arr.reverse()
    return arr

def step(arr):
    return [arr[-1]]+arr[:-1]

def getLines(seq, m, n):
    lines = []

    r = c = 0
    while r < m//2 and c < n//2:
        line = []
        line += [seq[r+i][c] for i in range(m-1-r*2)]
        line += [seq[m-1-r][c+i] for i in range(n-1-c*2)]
        line += reverseLine([seq[c+i][n-1-c] for i in range(1, m-r*2)])
        line += reverseLine([seq[r][r+i] for i in range(1, n-c*2)])
        r += 1
        c += 1
        lines.append(line)

    return lines

def buildMatrix(seq, m, n):
    res = []
    Ru = 0
    
    while Ru < min(m, n) // 2:
        row_res = []
        for i in range(Ru+1):
            row_res += [seq[i][Ru-i]]
        for i in range(Ru+1):
            row_res += reverseLine(seq[Ru-i][len(seq[Ru-i])-(n-(2*Ru+1)):]) if i == 0 else [seq[Ru-i][len(seq[Ru-i])-(n-(2*(Ru-i)+1))-i]]
        Ru += 1
        res.append(row_res)

    Rd = 0
    
    while Rd < min(m, n) // 2:
        row_res = []
        for i in range(Rd+1):
            row_res += [seq[i][(m-1-(2*(Rd-(Rd-i))))+(n-1-(2*(Rd-(Rd-i))))+Rd-i]]
        for i in range(Rd+1):
            row_res += reverseLine(seq[Rd-i][(m-1-(2*Rd)):(m-1-(2*Rd))+(n-1-(2*Rd))]) if i == 0 else [seq[Rd-i][(m-1-(2*(Rd-i)))-(Rd-(Rd-i))]]
        Rd += 1
        res.insert(min(m, n) // 2, reverseLine(row_res))

    row_remaining = m - (Ru + Rd)
    Rr = row_remaining - 1
    
    while Rr >= 0:
        row_res = []
        for i in range(len(seq)):
            row_res.insert(i, seq[i][(m-(i*2))-(Rd-i)-Rr-1])
            target = seq[i][len(seq[i])-(n-1-(i*2))-(Ru-i)-(row_remaining-1-Rr)]
            row_res.append(target) if i == 0 else row_res.insert(-1-(i-1), target)
        res.insert(min(m, n) // 2 + row_remaining-(Rr+1), row_res)
        Rr -= 1

    return res

M = int(input())
N = int(input())
r = int(input())
matrix = [list(map(int, input().split())) for j in range(M)]

matrixRotation(matrix, r)

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 07/02/2021
"""
