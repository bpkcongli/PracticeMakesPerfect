"""
    Picking Numbers
    Difficulty: ✰

    Diberikan sebuah array of integers, tentukan panjang maksimum dari
    sub-array, dimana sub-array harus memenuhi kriteria, yaitu selisih absolut
    antara dua elemennya harus kurang dari sama dengan 1.

    Contoh:

        a = [1, 1, 2, 2, 4, 4, 5, 5, 5]

    Dari array di atas, terdapat dua sub-array yang selisih absolut antara dua
    elemennya kurang dari sama dengan 1, yaitu [1, 1, 2, 2] dan [4, 4, 5, 5, 5].
    Dari dua sub-array tadi, panjang maksimum dari sub-array adalah 5 elemen.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan panjang maksimum dari
    sub-array, dimana sub-array memiliki selisih absolut antara dua
    elemennya, yaitu kurang dari sama dengan 1. Fungsi memiliki parameter,
    yaitu: a, array of integers.

    Format Input:
    Input ialah kumpulan integer yang dipisahkan dengan spasi, merupakan
    elemen dari array a.

    Format Output:
    Sebuah integer yang merupakan panjang maksimum dari sub-array yang memenuhi
    kriteria yang sudah disebutkan.

    Contoh Input:
    4 6 5 3 3 1

    Contoh Output:
    3

    Penjelasan:
    Sub-array yang sesuai dengan kriteria, berdasarkan input array yang sudah
    diberikan ialah: [4, 5], [4, 3, 3], dan [6, 5]. Dari sub-array tersebut
    diketahui panjang maksimumnya adalah 3 elemen.
"""

def pickingNumbers(a):
    longest = 0
    
    for num in a:
        x = num-1
        y = num+1
        num_total = a.count(num)
        x_total = a.count(x)
        y_total = a.count(y)
        longest_substring = y_total+num_total if x_total <= y_total else x_total+num_total
        longest = longest_substring if longest_substring > longest else longest

    return longest

a = [int(i) for i in input().split()]
print(pickingNumbers(a))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 19/01/2021
"""
