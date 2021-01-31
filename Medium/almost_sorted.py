"""
    Almost Sorted
    Difficulty: ✰✰

    Diberikan sebuah array yang berisikan integer, tentukan apakah elemen pada
    array dapat diurutkan dari yang terkecil sampai ke yang terbesar, dengan
    melakukan satu kali operasi, diantara operasi-operasi berikut ini.

        - Menukar dua elemen pada array (operasi swap), atau
        - Membalik urutan segmen pada array (operasi reverse)

    Tentukan apakah ada satu, atau dua, atau tidak ada satupun operasi di atas
    yang dapat dilakukan untuk mengurutkan elemen pada array dari yang terkecil
    sampai ke yang terbesar.
    
    Tugas:
    Buatlah sebuah fungsi yang akan menerima parameter sebagai berikut.
        - arr, array yang berisikan integer

    Format Input:
    N integer yang dipisahkan dengan spasi, yang merupakan elemen pada arr.

    Format Output:
    Fungsi harus menampilkan output berdasarkan ketentuan berikut ini.
    1. Jika elemen pada array sudah dalam posisi urut dari yang terkecil sampai
       ke yang terbesar, tampilkan 'yes' pada baris pertama.
    2. Jika elemen pada array dapat diurutkan setelah melakukan satu kali operasi
       dari dua operasi yang diijinkan, tampilkan 'yes' pada baris pertama, dan
       setelah itu,
       a. Jika elemen pada array dapat diurutkan setelah melakukan operasi swap
          antara arr[l] dengan arr[r], tampilkan 'swap l r' pada baris kedua.
          l dan r adalah indeks yang menunjukkan elemen pada array yang akan
          ditukar, dengan asumsi indeks pada array dimulai dari 1 sampai n.
       b. Jika elemen pada array dapat diurutkan setelah melakukan operasi
          reverse pada segmen array [l...r], tampilkan 'reverse l r' pada baris
          kedua. l dan r adalah indeks yang menunjukkan elemen pertama dan
          elemen terakhir dari segmen array yang akan dibalik urutannya, dengan
          asumsi indeks pada array dimulai dari 1 sampai n.
       c. Jika elemen pada array dapat diurutkan, baik jika sudah melakukan satu
          kali operasi swap atau satu kali operasi reverse, pilih operasi swap.
    3. Jika elemen pada array tidak dapat diurutkan walaupun sudah melakukan
       satu kali operasi, baik operasi swap ataupun operasi reverse, tampilkan
       'no' pada baris pertama.

    Contoh Input:
    23 26 43 34 44 51 60

    Contoh Output:
    yes
    swap 3 4

    Penjelasan:
    Jika elemen ke-3 (indeks ke-2), yaitu 43 dan elemen ke-4 (indeks ke-3), yaitu
    34, ditukar posisinya, elemen pada array akan tersusun dari yang terkecil
    sampai ke yang terbesar.

    Contoh Input:
    26 21 21 21 21 22

    Contoh Output:
    no

    Penjelasan:
    Walaupun sudah dilakukan satu kali operasi swap, ataupun satu kali operasi
    reverse, elemen pada array tersebut tidak dapat diurutkan dari yang terkecil
    sampai ke yang terbesar.

    Contoh Input:
    24 62 45 32 25 63

    Contoh Output:
    yes
    reverse 2 5

    Penjelasan:
    Jika segmen array dari elemen ke-2 (indeks ke-1) sampai elemen ke-5 (indeks
    ke-4), yaitu [62, 45, 32, 25] dibalik urutannya, elemen pada array akan
    tersusun dari yang terkecil sampai ke yang terbesar.

    Contoh Input:
    24 62 45 45 25 63

    Contoh Output:
    yes
    swap 2 5

    Penjelasan:
    Array tersebut dapat diurutkan setelah dilakukan satu kali operasi, baik
    operasi swap yaitu menukar elemen ke-2 (indeks ke-1), yaitu 62 dengan elemen
    ke-5 (indeks ke-4), yaitu 25, ataupun dengan operasi reverse yaitu membalik
    urutan segmen array dari elemen ke-2 (indeks ke-1) sampai elemen ke-5 (indeks
    ke-4), yaitu [62, 45, 45, 25]. Karena ada dua operasi yang dapat dilakukan
    untuk mengurutkan elemen pada array, pilih operasi swap.
"""

def almostSorted(arr):
    iio = [arr[i-1] <= arr[i] for i in range(1, len(arr))]
    tnio = iio.count(False)

    if tnio == 0:
        print('yes')
        return
    
    finio = iio.index(False)
    ninio = finio+1 + iio[finio+1:].index(False) if tnio > 1 else -1
    ivafv = [arr[i] >= arr[finio] for i in range(finio+1, len(arr))]
    fiovafv = finio + ivafv.index(True) if ivafv.count(True) else len(arr)-1

    if tnio == 1 and ((finio > 0 and arr[finio+1] >= arr[fiovafv] and arr[finio-1] <= arr[fiovafv]) or (finio == 0 and arr[finio] >= arr[fiovafv] and arr[finio+1] >= arr[fiovafv])):
        print('yes')
        print('swap {0} {1}'.format(finio+1, fiovafv+1))
    elif tnio == 2 and (arr[finio] >= arr[ninio] and arr[finio-1] <= arr[ninio+1]):
        print('yes')
        print('swap {0} {1}'.format(finio+1, ninio+2))
    elif tnio > 2 and iio[finio:finio + tnio] == [False for i in range(tnio)] and arr[finio+tnio] >= arr[finio-1]:
        print('yes')
        print('reverse {0} {1}'.format(finio+1, finio+1+tnio))
    else:
        print('no')

arr = list(map(int, input().split()))

almostSorted(arr)

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 31/01/2021
"""
