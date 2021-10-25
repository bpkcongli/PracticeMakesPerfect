"""
    Circus Show
    Difficulty: ✰

    Bayangkan kamu sedang membuat koreografi pertunjukan sirkus dengan berbagai
    binatang. Dalam satu babak pertunjukan, kamu memiliki dua ekor kangguru
    yang akan melompat ke arah yang sama.

    Asumsikan lintasan yang dilewati kangguru saat melompat adalah sebuah garis
    bilangan, kangguru akan melompat ke arah kanan (ke arah positif). Kangguru
    pertama mulai pada titik x1 dan bergerak dengan kecepatan v1 meter per
    lompatan. Kangguru kedua mulai pada titik x2 dan bergerak dengan kecepatan
    v2 meter per lompatan. Kamu harus mencari tahu apakah kedua kangguru dapat
    tiba di titik yang sama dan pada waktu yang sama.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan 'YES' jika kedua kangguru
    dapat tiba di titik yang sama dan pada waktu yang sama. Jika tidak,
    kembalikan 'NO'. Fungsi akan menerima parameter sebagai berikut:
        - x1: integer, titik awal kangguru pertama mulai melompat
        - x2: integer, titik awal kangguru kedua mulai melompat
        - v1: integer, kecepatan lompat kangguru pertama (dalam meter)
        - v2: integer, kecepatan lompat kangguru kedua (dalam meter)

    Format Input:
    Input ialah empat integer yang dipisahkan dengan spasi yang menunjukkan
    nilai masing-masing untuk x1, v1, x2, dan v2.

    Format Output:
    Tampilkan 'YES' jika kangguru tiba di titik yang sama saat waktu yang sama,
    jika tidak, tampilkan 'NO'.

    Catatan:
    Tiba saat waktu yang sama, berarti kedua kangguru melakukan jumlah lompatan
    yang sama.

    Contoh Input:
    0 3 4 2

    Contoh Output:
    YES

    Penjelasan:
    Lompatan kangguru bisa dilihat melalui diagram berikut.

                                       Jump 1    Jump 2    Jump 3    Jump 4
                         Kangguru 2 *---------*---------*---------*---------*
                                    x2

                     Jump 1         Jump 2         Jump 3         Jump 4
     Kangguru 1 *--------------*--------------*--------------*--------------*
                x1

        <--*----*----*----*----*----*----*----*----*----*----*----*----*----*-->
          -1    0    1    2    3    4    5    6    7    8    9   10   11   12

     Terlihat bahwa kedua kangguru dapat tiba di titik yang sama (nomor 12 pada
     diagram) setelah melakukan lompatan sebanyak empat kali.
"""

def kangaroo(x1, v1, x2, v2):
    x = x1
    y = x2
    dif = y-x if x<y else x-y
    status = False

    while x!=y:
        x += v1
        y += v2
        dif_after_jump = y-x if x<y else x-y
        if dif_after_jump >= dif: break
        else: dif = dif_after_jump
    else:
        status = True

    return 'YES' if status else 'NO'

x1, v1, x2, v2 = [int(i) for i in input().split()]
print(kangaroo(x1, v1, x2, v2))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 20/01/2021
"""
