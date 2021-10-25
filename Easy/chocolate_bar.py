"""
    Chocolate Bar
    Difficulty: ✰

    Lily dan Ron memiliki sebatang coklat, mereka sedang menentukan
    bagaimana cara membaginya. Setiap kotak pada coklat memiliki bilangan
    integer di atas nya.

        A bar of chocolate
        +-----+-----+-----+-----+-----+-----+
        |     |     |     |     |     |     |
        |  2  |  3  |  1  |  1  |  4  |  3  |
        |     |     |     |     |     |     |
        +-----+-----+-----+-----+-----+-----+

    Lily memutuskan untuk membagi setiap kotak pada sebatang coklat sehingga:
    - Banyak kotak sesuai dengan bulan kelahiran Ron, dan
    - Jumlah bilangan integer di setiap kotak sama dengan tanggal kelahiran Ron

    Asumsikan sebatang coklat dengan bilangan integer di setiap kotaknya
    sebagai array of integer, s = [2, 3, 1, 1, 4, 3]. Lily ingin menemukan
    potongan coklat yang jumlah kotaknya sesuai dengan bulan kelahiran Ron,
    m = 2, dan jumlah integer di setiap kotaknya sama dengan tanggal kelahiran
    Ron, d = 5. Pada kasus ini, terdapat dua potong coklat yang sesuai dengan
    kriteria yaitu: [2, 3] dan [1, 4]

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan bilangan integer yang
    merepresentasikan berapakah cara yang dapat dilakukan Lily untuk membagi
    coklatnya kepada Ron dengan kriteria/parameter sebagai berikut:
    s = array of integers, angka di setiap kotak pada sebatang coklat
    d = sebuah integer, merepresentasikan tanggal lahir Ron
    m = sebuah integer, merepresentasikan bulan lahir Ron

    Format Input:
    Input pertama merupakan n integer yang dipisahkan dengan spasi, merupakan
    angka di setiap kotak pada sebatang coklat.
    Input kedua merupakan dua buah integer yang dipisahkan dengan spasi,
    merupakan tanggal dan bulan lahir Ron.

    Format Output:
    Tampilkan sebuah integer yang merupakan jumlah cara bagaimana Lily
    membagi coklatnya kepada Ron.

    Contoh Input:
    1 2 1 3 2
    3 2

    Contoh Output:
    2

    Penjelasan:

        +-----+-----+-----+-----+-----+
        |     |     |     |     |     |
        |  1  |  2  |  1  |  3  |  2  |
        |     |     |     |     |     |
        +-----+-----+-----+-----+-----+

    Lily ingin memberikan Ron potongan coklat dengan jumlah kotak = 2, dan
    jumlah integer di setiap kotaknya = 3, sehingga ada dua kemungkinan
    potongan coklat yang dapat diberikan kepada Ron, yaitu: [1, 2] dan [2, 1]
"""

def birthday():
    s = list(map(int, input().strip().split(" ")))
    d, m = list(map(int, input().strip().split(" ")))
    pieces = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d: pieces += 1
    return pieces

print(birthday())

"""
    Challenge ini diadaptasi dari HackerRank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 12/01/2021
"""
