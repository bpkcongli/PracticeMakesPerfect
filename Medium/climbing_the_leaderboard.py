"""
    Climbing the Leaderboard
    Difficulty: ✰✰

    Kamu sedang memainkan sebuah permainan arkade. Setiap skor yang berhasil
    kamu cetak akan masuk ke papan peringkat (leaderboard). Leaderboard
    menggunakan sistem Dense Ranking, aturan penentuan peringkatnya sebagai
    berikut.

        - Pemain yang mencetak skor tertinggi berada di peringkat 1 pada
          leaderboard.
        - Pemain yang memiliki skor yang sama dengan pemain lainnya, akan
          mendapatkan peringkat yang sama, dan pemain setelahnya mendapatkan
          nomor peringkat berikutnya.

    Contoh:
    ranked = [100, 90, 90, 80]
    player = [70, 80, 105]

    - ranked -> skor pemain yang sudah ada pada leaderboard.
    - player -> skor kamu setelah game ke-1, ke-2, ..., hingga game ke-n.

    Sehingga, pemain yang sudah ada pada leaderboard akan mendapatkan peringkat
    1, 2, 2, dan 3 secara berurutan. Peringkat kamu setelah game ke-1 hingga
    game ke-3 ialah peringkat ke-4, ke-3, dan ke-1, secara berurutan.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan array of integer, yaitu
    peringkat kamu setelah baru saja mencetak skor di masing-masing game.
    Fungsi akan menerima parameter sebagai berikut.
        - ranked, array of integer, skor pada leaderboard, yang sudah dicetak
          pemain lain.
        - player, array of integer, skor kamu di masing-masing game.

    Format Input:
    Input pertama yaitu n integer yang dipisahkan dengan spasi, yaitu ranked,
    skor pada leaderboard, yang sudah dicetak pemain lain.
    Input kedua yaitu n integer yang dipisahkan dengan spasi, yaitu player,
    skor kamu di masing-masing game.

    Format Output:
    Output adalah n integer yang dipisahkan dengan spasi, yaitu peringkat kamu
    setelah mencetak skor di masing-masing game.

    Contoh Input:
    105 90 90 85 70 65 65 60
    30 50 55 85 120

    Contoh Output:
    7 7 7 3 1

    Penjelasan:
    
    Berikut leaderboard sebelum kamu memainkan game pertama.
    +---------+----------+
    |  Ranks  |  Scores  |
    +---------+----------+
    |    1    |    105   |
    |    2    |     90   |
    |    2    |     90   |
    |    3    |     85   |
    |    4    |     70   |
    |    5    |     65   |
    |    5    |     65   |
    |    6    |     60   |
    +---------+----------+

      Setelah game ke-1        Setelah game ke-2        Setelah game ke-3
    +---------+----------+   +---------+----------+   +---------+----------+
    |  Ranks  |  Scores  |   |  Ranks  |  Scores  |   |  Ranks  |  Scores  |
    +---------+----------+   +---------+----------+   +---------+----------+
    |    1    |    105   |   |    1    |    105   |   |    1    |    105   |
    |    2    |     90   |   |    2    |     90   |   |    2    |     90   |
    |    2    |     90   |   |    2    |     90   |   |    2    |     90   |
    |    3    |     85   |   |    3    |     85   |   |    3    |     85   |
    |    4    |     70   |   |    4    |     70   |   |    4    |     70   |
    |    5    |     65   |   |    5    |     65   |   |    5    |     65   |
    |    5    |     65   |   |    5    |     65   |   |    5    |     65   |
    |    6    |     60   |   |    6    |     60   |   |    6    |     60   |
    |   *7*   |     30   |   |   *7*   |     50   |   |   *7*   |     55   |
    +---------+----------+   +---------+----------+   +---------+----------+

      Setelah game ke-4        Setelah game ke-5
    +---------+----------+   +---------+----------+
    |  Ranks  |  Scores  |   |  Ranks  |  Scores  |
    +---------+----------+   +---------+----------+
    |    1    |    105   |   |   *1*   |    120   |
    |    2    |     90   |   |    2    |    105   |
    |    2    |     90   |   |    3    |     90   |
    |   *3*   |     85   |   |    3    |     90   |
    |    3    |     85   |   |    4    |     85   |
    |    4    |     70   |   |    5    |     70   |
    |    5    |     65   |   |    6    |     65   |
    |    5    |     65   |   |    6    |     65   |
    |    6    |     60   |   |    7    |     60   |
    +---------+----------+   +---------+----------+
"""

def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    i = len(ranked)-1
    ranks = []

    for score in player:
        while i>=0:
            if score < ranked[i]:
                ranks.append(i+2)
                break
            i -= 1
        else:
            ranks.append(1)

    return ranks

ranked = list(map(int, input().split()))
player = list(map(int, input().split()))

print(' '.join(list(map(str, climbingLeaderboard(ranked, player)))))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 25/01/2021
"""
