"""
    Breaking the Records
    Difficulty: ✰

    Maria bermain basket di kampus nya dan ia ingin menjadi profesional.
    Setiap musim dia menyimpan rekor pertandingannya. Dia membuat tabel
    yang berisi berapa kali dia memecahkan rekor musimnya untuk poin
    terbanyak dan poin paling sedikit dalam sebuah pertandingan. Anggaplah
    poin yang dicetak pada pertandingan pertama menetapkan rekornya untuk
    musim ini dan dia mulai menghitung berapa kali ia memecahkan rekor
    dari pertandingan pertama.

    Asumsikan poin yang ia peroleh dalam semusim ditampilkan dalam sebuah
    array. Poin memiliki urutan yang sama dengan pertandingan yang
    dimainkan. Misal:

        scores = [12, 24, 10, 24]

    Yang berarti di pertandingan pertama ia memperoleh 12 poin, pertandingan
    kedua memperoleh 24 poin, dst.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan integer array yang berisi
    berapa kali ia memecahkan rekor poin. Index 0 untuk berapa kali
    memecahkan rekor poin terbanyak, dan index 1 untuk berapa kali memecahkan
    rekor poin paling sedikit.

    Format Input:
    Input pertama merupakan sebuah integer n, yang merepresentasikan berapa
    banyak pertandingan yang dimainkan.
    Input kedua merupakan n baris integer yang merupakan elemen dari array
    yang merepresentasikan poin yang diperoleh dari setiap pertandingan.

    Format Output:
    Tampilkan dua integer yang dipisahkan dengan spasi yang merupakan jumlah
    berapa kali Maria memecahkan rekor untuk poin terbanyak dan poin paling
    sedikit pada satu pertandingan dalam satu musim.

    Contoh Input:
    9
    10
    5
    20
    20
    4
    5
    2
    25
    1

    Contoh Output:
    2 4

    Penjelasan:
    Diagram di bawah menggambarkan berapa kali Maria memecahkan rekor poin
    terbanyak dan paling sedikit sepanjang satu musim:

        Game        0   1   2   3   4   5   6   7   8
        Score       10  5   20  20  4   5   2   25  1
        Highest     10  10  20  20  20  20  20  25  25
        Lowest      10  5   5   5   4   4   2   2   1

    Dia memecahkan rekor poin terbanyaknya dua kali (setelah pertandingan
    ke-2 dan ke-7) dan rekor poin paling sedikit empat kali (setelah
    pertandingan ke-1, ke-4, ke-6, dan ke-8). Perhatikan bahwa dia tidak
    memecahkan rekornya untuk poin terbanyak setelah pertandingan ke-3,
    karena poinnya selama pertandingan itu tidak lebih besar dari
    rekor poin terbaiknya.
"""

def breakingRecords():
    totalGames = int(input())
    scores = [int(input()) for i in range(totalGames)]
    lowest = highest = scores[0]
    bestRecord = worstRecord = 0
    
    for score in scores[1:]:
        if score < lowest:
            worstRecord += 1
            lowest = score
        elif score > highest:
            bestRecord += 1
            highest = score

    return ' '.join([str(bestRecord), str(worstRecord)])

print(breakingRecords())

"""
    Challenge ini diadaptasi dari HackerRank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 12/01/2021
"""
