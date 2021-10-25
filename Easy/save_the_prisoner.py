"""
    Save the Prisoner!
    Difficulty: ✰

    Sebuah penjara memiliki sejumlah narapidana dan sejumlah permen untuk
    diberikan kepada mereka. Kepala penjara memutuskan cara paling adil untuk
    membagi permen ialah dengan mendudukkan para narapidana di sekitar meja
    bundar di kursi yang sudah diberi nomor urut. Satu permen akan diberikan
    kepada setiap narapidana secara berurutan sesuai dengan nomor urut pada
    kursi sampai semua permen habis dibagikan.

    Kepala penjara rupanya sedang bercanda. Permen terakhir terlihat seperti
    permen lainnya, tetapi rasanya tidak enak. Tentukan nomor kursi yang
    ditempati oleh narapidana yang akan menerima permen tersebut.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan integer yang merepresentasikan
    nomor pada kursi dimana narapidana yang duduk di kursi tersebut akan
    mendapatkan permen yang terakhir. Fungsi memiliki parameter sebagai berikut:
        - n: integer, jumlah narapidana
        - m: integer, jumlah permen yang akan dibagikan
        - s: integer, distribusi permen dimulai dari nomor kursi ini.

    Format Input:
    Input pertama, t, sebuah integer yang merupakan jumlah kasus yang diuji.
    Input selanjutnya, t baris, setiap barisnya terdiri dari kumpulan integer
    yang dipisahkan dengan spasi. Masing-masing integer merepresentasikan nilai
    secara berurutan untuk n, m, dan s.

    Format Output:
    Output adalah n integer yang dipisahkan dengan spasi, masing-masing
    merupakan nomor kursi 'permen terakhir' untuk setiap kasus yang diuji.

    Contoh Input:
    2
    7 9 3
    3 7 3
    
    Contoh Output:
    4 3

    Penjelasan:
    Kasus pertama, terdapat n = 7 narapidana, m = 9 permen, dan pembagian
    permen dimulai dari kursi nomor s = 3. Pembagian permen kepada narapidana
    akan menjadi seperti ini.

    Permen |  9  8  7  6  5  4  3  2  1
    Kursi  |  3  4  5  6  7  1  2  3  4
    
    Kasus kedua, terdapat n = 3 narapidana, m = 7 permen, dan pembagian
    permen dimulai dari kursi nomor s = 3. Pembagian permen kepada narapidana
    akan menjadi seperti ini.

    Permen |  7  6  5  4  3  2  1
    Kursi  |  3  1  2  3  1  2  3

    Sehingga, pada kasus pertama narapidana yang duduk di kursi nomor 4, dan
    pada kasus kedua narapidana yang duduk di kursi nomor 3 akan mendapatkan
    permen yang tidak enak.
"""

def saveThePrisoner(n, m, s):
    res = s + (m-1) % n    
    return res-n if res > n else res

result = []

for i in range(int(input())):
    n, m, s = list(map(int, input().split()))
    result.append(saveThePrisoner(n, m, s))

print(' '.join(list(map(str, result))))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 21/01/2021
"""
