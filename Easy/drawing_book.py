"""
    Drawing Book
    Difficulty: ✰

    Seorang guru meminta siswanya untuk membuka halaman pada sebuah buku.
    Seorang siswa dapat mulai membalik halaman dari depan maupun dari belakang
    buku. Mereka selalu membalik halaman satu per satu. Ketika mereka mulai
    membuka buku, halaman selalu dimulai dari sisi sebelah kanan:

        Buku
        +-------\ /-------+        +-------\ /-------+
        |        |        |        |        |        |
        |        |        |        |        |        |
        |        |    1   |  >>>>  |   2    |    3   |
        |        |        |        |        |        |
        |        |        |        |        |        |
        +-------/ \-------+        +-------/ \-------+

    Ketika mereka membalik halaman ke-1, mereka akan melihat halaman ke-2 dan
    ke-3, ketika mereka membalik halaman lagi, mereka akan melihat halaman ke-4
    dan ke-5, dan begitu seterusnya. Setiap halaman kecuali halaman terakhir,
    akan selalu dicetak pada kedua sisi.

    Jika jumlah halaman pada sebuah buku dinyatakan dalam n, dan halaman pada
    buku yang siswa ingin buka dinyatakan dalam p, tentukan jumlah minimum
    berapa kali siswa membalik halaman menuju ke halaman yang ingin dibuka.
    Dengan catatan, siswa dapat membalik halaman mulai dari depan atau dari
    belakang buku.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan sebuah integer yang merupakan
    jumlah minimum berapa kali siswa membalik halaman menuju ke halaman yang
    ingin dibuka, dengan parameter yaitu:
        - n, sebuah integer, merupakan jumlah keseluruhan halaman pada buku
        - p, sebuah integer, nomor halaman yang ingin dibuka

    Format Input:
    Input pertama ialah integer n, yaitu jumlah keseluruhan halaman pada buku.
    Input kedua ialah integer p, yaitu nomor halaman yang ingin dibuka.

    Format Output:
    Sebuah integer yang merupakan jumlah minimum berapa kali siswa membalik
    halaman menuju ke halaman yang ingin dibuka.

    Contoh Input:
    6
    2

    Contoh Output:
    1

    Penjelasan:
    Jika siswa membuka halaman dari depan buku, mereka hanya butuh sekali
    membalik halaman menuju halaman ke-2.

                +-------\ /-------+        +-------\ /-------+
                |        |        |        |        |        |
                |        |        |        |        |        |
                |        |    1   |  >>>>  |   2    |    3   |
                |        |        |        |        |        |
                |        |        |        |        |        |
                +-------/ \-------+        +-------/ \-------+

    Jika siswa membuka halaman buku dari belakang buku, mereka butuh dua kali
    membalik halaman menuju halaman ke-2.

    +-------\ /-------+        +-------\ /-------+        +-------\ /-------+
    |        |        |        |        |        |        |        |        |
    |        |        |        |        |        |        |        |        |
    |   6    |        |  >>>>  |   4    |    5   |  >>>>  |   2    |    3   |
    |        |        |        |        |        |        |        |        |
    |        |        |        |        |        |        |        |        |
    +-------/ \-------+        +-------/ \-------+        +-------/ \-------+

    Sehingga jumlah minimum siswa membalik halaman adalah sebanyak 1 kali.
"""

def pageCount(n, p):
    current_page = 1
    turns = []
    current_turn = 0

    while current_page<p:
        current_page += 2
        current_turn += 1
    else:
        turns.append(current_turn)
        current_page = n if n % 2 == 0 else n-1
        current_turn = 0
        if current_page == p:
            turns.append(0)
        else:
            while current_page>p:
                current_page -= 2
                current_turn += 1
            else:
                turns.append(current_turn)

    return min(turns)

print(pageCount(int(input()), int(input())))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 17/01/2021
"""
