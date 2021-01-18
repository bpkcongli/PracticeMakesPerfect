"""
    Apple and Orange
    Difficulty: ✰

    Di sekitar rumah Sam, terdapat sebuah pohon apel dan sebuah pohon jeruk
    yang menghasilkan banyak apel dan jeruk. Berbekal informasi yang diberikan
    melalui diagram di bawah ini, tentukan jumlah apel dan jeruk yang mendarat
    di area rumah Sam.

            Pohon Apel               Rumah Sam             Pohon Jeruk
             _  ___  _              ____________             _  ___  _
           _/ _/   \_ \            /            \           / _/   \_ \_
           \_/       \ \          /              \         / /       \_/
             \_     _/_/         /________________\        \_\_     _/
               \| |/     Apel      |     __     |  Jeruk_      \| |/
                | |      _|_       | *  |  |  * |      / \      | |
                | |      \_/       |    |  |    |      \_/      | |
        ---------*--------------*-------------------*------------*--------
                 a ------->     <------------------->   <------- b
                      d         s                   t       d

    - Area yang dibatasi dengan titik s dan titik t adalah area pekarangan
      rumah Sam. Pohon apel ada di kiri area rumah dan pohon jeruk ada di kanan
      area rumah.
    - Diasumsikan pohon terletak di titik tertentu, di mana pohon apel ada di
      titik a, dan pohon jeruk ada di titik b.
    - Ketika buah jatuh dari pohon, buah akan mendarat dalam satuan jarak d
      dari pohon asalnya di sepanjang sumbu X. Nilai negatif berarti buah
      mendarat di sebelah kiri dari pohon, sedangkan nilai positif berarti buah
      mendarat di sebelah kanan dari pohon.

    Diberikan nilai dari d untuk m buah apel dan n buah jeruk, tentukan berapa
    banyak apel dan jeruk yang jatuh di area rumah Sam.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan berapa banyak apel dan jeruk
    yang jatuh di area rumah Sam dengan mempertimbangkan parameter berikut ini.
    - s: integer, titik awal yang menunjukkan area rumah Sam
    - t: integer, titik akhir yang menunjukkan area rumah Sam
    - a: integer, titik yang menunjukkan lokasi pohon apel
    - b: integer, titik yang menunjukkan lokasi pohon jeruk
    - apples: array of integers, nilai d untuk masing-masing apel yang jatuh
    - oranges: array of integers, nilai d untuk masing-masing jeruk yang jatuh

    Format Input:
    Input pertama adalah dua buah integer yang dipisahkan dengan spasi, masing-
    masing merupakan nilai untuk s dan t.
    Input kedua adalah dua buah integer yang dipisahkan dengan spasi, masing-
    masing merupakan nilai untuk a dan b.
    Input ketiga adalah m buah integer yang dipisahkan dengan spasi, merupakan
    nilai d, jarak titik jatuh apel dengan pohonnya (titik a).
    Input keempat adalah n buah integer yang dipisahkan dengan spasi, merupakan
    nilai d, jarak titik jatuh jeruk dengan pohonnya (titik b).

    Format Output:
    Output merupakan dua buah integer yang dipisahkan dengan spasi, masing-
    masing merupakan jumlah apel dan jeruk yang jatuh di dalam area rumah Sam.

    Contoh Input:
    7 11
    5 15
    -2 2 1
    5 -6

    Contoh Output:
    1 1

    Penjelasan:
    Dari input di atas, maka:
    s = 7
    t = 11
    a = 5
    b = 15

    Apel pertama jatuh di titik 5 - 2 = 3. Apel kedua jatuh di titik 5 + 2 = 7.
    Apel ketiga jatuh di titik 5 + 1 = 6. Jeruk pertama jatuh di titik 15 + 5
    = 20. Jeruk kedua jatuh di titik 15 - 6 = 9.

    Hanya ada satu apel (yaitu apel kedua) yang jatuh di dalam area rumah Sam
    (diantara titik 7 dan 11), dan hanya ada satu jeruk (yaitu jeruk kedua)
    yang jatuh di dalam area rumah Sam (diantara titik 7 dan 11). Sehingga
    outputnya menjadi 1 1 (1 apel dan 1 jeruk).
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples_oranges = []
    
    for tree_point, d_fruits in {a: apples, b: oranges}.items():
        total_fruits = 0
        for d_fruit in d_fruits:
            falling_point = d_fruit + tree_point
            if falling_point >= s and falling_point <= t:
                total_fruits += 1
        total_apples_oranges.append(total_fruits)

    return '{0} {1}'.format(*total_apples_oranges)

[s, t], [a, b], apples, oranges = [[int(i) for i in input().split()] for j in range(4)]

print(countApplesAndOranges(s, t, a, b, apples, oranges))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 18/01/2021
"""
