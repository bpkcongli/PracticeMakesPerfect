"""
    Day of the Programmer
    Difficulty: ✰

    Marie menemukan sebuah mesin waktu dan ia ingin mencobanya dengan bepergian
    melintasi waktu untuk mengunjungi Rusia pada Day of the Programmer
    (yang jatuh pada hari ke-256 setiap tahunnya) sepanjang tahun 1700 hingga
    tahun 2700.

    Dari tahun 1700 hingga tahun 1917, kalender resmi Rusia adalah kalender
    Julian, dan sejak 1919 mereka menggunakan sistem kalender Gregorian.
    Peralihan dari sistem kalender Julian ke Gregorian terjadi pada tahun 1918,
    ketika tanggal setelah 31 Januari adalah menjadi tanggal 14 Februari.
    Artinya, pada 1918, 14 Februari adalah hari ke-32 pada tahun tersebut di
    Rusia.

    Dalam kedua sistem kalender tersebut, bulan Februari memiliki jumlah hari
    yang bervariasi, akan menjadi 29 hari selama satu tahun kabisat, dan
    28 hari selama satu tahun biasa. Dalam kalender Julian, tahun kabisat
    selalu habis dibagi dengan 4. Sedangkan dalam kalender Gregorian, tahun
    bisa dikatakan tahun kabisat, jika memenuhi syarat berikut.

        - Habis dibagi dengan 400
        - Habis dibagi dengan 4 dan tidak habis dibagi dengan 100

    Asumsikan tahun dalam y, temukan tanggal dari hari ke-256 tahun tersebut
    menurut kalender resmi Rusia yang berlaku saat itu. Kemudian cetak dalam
    format dd.mm.yyyy, di mana dd adalah hari, mm adalah bulan, dan yyyy adalah
    tahun.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan string yang merepresentasikan
    tanggal dari hari ke-256 dari input tahun yang diberikan.    

    Format Input:
    Sebuah integer yang merepresentasikan tahun.

    Format Output:
    Tampilkan sebuah string yang merupakan Day of the Programmer dalam format
    dd.mm.yyyy, dimana dd adalah hari, mm adalah bulan, dan yyyy adalah tahun.

    Contoh Input:
    2017

    Contoh Output:
    13.09.2017

    Penjelasan:
    Pada tahun 2017, Januari terdiri dari 31 hari, Februari 28 hari (karena
    bukan tahun kabisat), Maret 31 hari, April 30 hari, Mei 31 hari, Juni 30
    hari, Juli 31 hari, dan Agustus 31 hari. Sehingga jika dijumlahkan seluruh
    hari dari Januari-Agustus adalah 243 hari. Days of the Programmer jatuh
    pada hari ke-256, butuh 13 hari lagi menuju ke hari itu, sehingga bisa
    kita temukan Days of the Programmer tahun 2017 jatuh pada 13 September. 
    
"""

def dayOfProgrammer(year):
    isGregorian = True if year > 1918 else False
    isLeap = False
    
    if year == 1918:
        return '26.09.1918'
    
    if isGregorian:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): isLeap = True
    else:
        if year % 4 == 0: isLeap = True
    
    return '12.09.{0}'.format(year) if isLeap else '13.09.{0}'.format(year)

print(dayOfProgrammer(int(input())))

"""
    Challenge ini diadaptasi dari HackerRank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 13/01/2021
"""
