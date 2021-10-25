"""
    Encryption
    Difficulty: ✰✰

    Bayangkan kamu adalah seorang agen mata-mata. Kamu akan mengirim sebuah
    pesan teks rahasia yang ditujukan kepada seorang klien. Pesan teks tersebut
    harus dienkripsi dengan menggunakan metode enkripsi, yang langkah-langkahnya
    seperti berikut ini.
        - Pertama, hapus spasi dari teks yang akan diproses.
        - Asumsikan L adalah jumlah karakter dari teks yang sudah dihapus spasinya.
        - Karakter tersebut akan ditulis ke dalam sebuah grid, yang jumlah baris
          dan kolomnya mengikuti ketentuan berikut.

              ⌊ √L ⌋ <= rows <= columns <= ⌈ √L ⌉, dimana:
              
              - L adalah panjang karakter dari string
              - rows adalah jumlah baris pada grid
              - columns adalah jumlah kolom pada grid
              - ⌊ x ⌋ adalah floor function, yaitu pembulatan angka ke bawah
              - ⌈ x ⌉ adalah ceil function, yaitu pembulatan angka ke atas
                Pastikan rows * columns >= L
              
    Contoh:
    s = 'allied soldiers will try to take control the bridge in remagen'

    Setelah menghapus spasi pada teks, panjang karakter dari teks adalah L = 52.
    Ukuran grid berdasarkan ketentuan yaitu:
    Jumlah baris: √52 = 7.21110255092, dibulatkan ke bawah menjadi 7
    Jumlah kolom: √52 = 7.21110255092, dibulatkan ke atas menjadi 8
    Karena 7 * 8 >= 52, ukuran grid berdasarkan ketentuan adalah 7x8.

    Tuliskan pesan teks di atas ke dalam grid, sehingga menjadi seperti ini.
    alliedso
    ldierswi
    lltrytot
    akecontr
    olthebri
    dgeinrem
    agen
    
    Bentuk teks yang terenkripsi diperoleh dengan menampilkan karakter pada setiap
    kolom, yang dipisahkan dengan spasi antar kolomnya. Sehingga bentuk teks yang
    sudah dienkripsi akan menjadi:

        allaoda ldlklgg litetee ierchin eryoen dstnbr swotre oitrim
    
    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan teks yang sudah terenkripsi.
    Fungsi akan menerima parameter sebagai berikut.
        - s, sebuah string, teks yang akan dienkripsi

    Format Input:
    Input yaitu string yang merupakan teks yang akan dienkripsi.

    Format Output:
    Output yaitu string berisi teks yang sudah dalam format terenkripsi.

    Contoh Input:
    the president will enter the meeting room in one hour

    Contoh Output:
    tiltiiu hdlhnnr eeeego pnnmrn rtteoe eweeoh sirtmo

    Penjelasan:
    Setelah spasi dihapus, informasi yang kita dapatkan ialah:
    L = 44
    Jumlah baris: √44 = 6.6332495807, dibulatkan ke bawah menjadi 6
    Jumlah kolom: √44 = 6.6332495807, dibulatkan ke atas menjadi 7
    Karena 6 * 7 < 44, genapkan jumlah baris menjadi 7. Ukuran grid menjadi 7x7.

    Ubah ke dalam bentuk grid.
    thepres
    identwi
    llenter
    themeet
    ingroom
    inoneho
    ur

    Sehingga bentuk teks terenkripsi akan menjadi seperti pada output.
"""

import math

def encryption(s):
    s = s.replace(' ', '')
    rows = math.floor(math.sqrt(len(s)))
    columns = math.ceil(math.sqrt(len(s)))
    rows += 1 if rows * columns < len(s) else 0
    whitespace = rows*columns - len(s)
    grids = []
    s_index = 0
    encrypted_s = ''

    for row in range(rows):
        grid_column = []
        total_char_in_column = 0
        while total_char_in_column < columns and s_index < len(s):
            grid_column.append(s[s_index])
            s_index += 1
            total_char_in_column += 1
        else:
            if row + 1 == rows:
                grid_column += ['' for i in range(whitespace)]
            grids.append(grid_column)

    for column in range(columns):
        for row in range(rows):
            encrypted_s += grids[row][column]
        encrypted_s += ' ' if column + 1 != columns else ''

    return encrypted_s

s = input()

print(encryption(s))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 31/01/2021
"""
