"""
    Non Divisible Subset
    Difficulty: ✰✰

    Diketahui S, sebuah array yang berisikan integer, tentukan panjang maksimal
    dari S', sebuah array yang merupakan himpunan bagian dari S. Himpunan bagian
    harus memenuhi syarat, yaitu jumlah dua angka dari setiap angka pada
    himpunan bagian tidak habis dibagi dengan k.

    Contoh:
    S = [19, 10, 12, 10, 24, 25, 22]
    k = 4

    Adapun himpunan bagian dari S yang memenuhi syarat, yaitu jumlah dua angka
    tidak habis dibagi dengan 4, diantaranya:
    [12, 25, 10], [12, 25, 22], [24, 25, 10], [24, 25, 22], [12, 19, 10],
    [12, 19, 22], [24, 19, 10], dan [24, 19, 22]

    Sehingga, bisa disimpulkan panjang maksimal dari S' adalah 3 elemen. 

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan integer yang merupakan panjang
    maksimal dari S' yang sudah memenuhi syarat. Fungsi akan menerima parameter
    sebagai berikut.
        - S, array yang berisi integer
        - k, sebuah integer

    Format Input:
    Input pertama yaitu k.
    Input kedua yaitu n integer yang dipisahkan dengan spasi, merupakan elemen
    dari S.

    Format Output:
    Output adalah sebuah integer yang merupakan panjang maksimal dari S',
    himpunan bagian yang memenuhi syarat yang sudah disebutkan.

    Contoh Input:
    3
    1 2 4 7

    Contoh Output:
    3

    Penjelasan:
    Diketahui, S = [1, 2, 4, 7], dan k = 3
    Jumlah dua angka dari setiap angka pada array S, dijabarkan seperti ini.

        1 + 2 = 3
        1 + 4 = 5
        1 + 7 = 8
        2 + 4 = 6
        2 + 7 = 9
        4 + 7 = 11

    Terlihat bahwa S' yang memenuhi syarat yaitu [1, 4, 7]. Sehingga output = 3.

    Tips:
    Coming soon...
"""

def nonDivisibleSubset(k, s):
    remainder = sorted([e%k for e in s])
    max_len_subset = 1 if remainder.count(0) > 0 else 0
    
    i = 1
    while i <= k//2:
        if i == k-i:
            max_len_subset += 1
        else:
            max_len_subset += remainder.count(i) if remainder.count(i) >= remainder.count(k-i) else remainder.count(k-i)
        i += 1
        
    return max_len_subset

k = int(input())
s = list(map(int, input().split()))

print(nonDivisibleSubset(k, s))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 26/01/2021
"""
