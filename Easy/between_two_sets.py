"""
    Between Two Sets
    Difficulty: ✰

    Diberikan dua buah array of integers, yaitu A dan B. Tentukan semua
    bilangan bulat, dalam hal ini disebut dengan X, yang memenuhi dua kondisi
    berikut.

        - Elemen dari array pertama adalah semua faktor dari bilangan bulat X
        - Bilangan bulat X adalah faktor dari semua elemen dari array kedua

    Bilangan bulat X ini disebut berada di antara dua array. Tentukan berapa
    banyak bilangan bulat X yang memenuhi kondisi yang disebutkan di atas.

    Tugas:
    Buatlah sebuah fungsi yang mengembalikan sebuah integer yang merupakan
    jumlah dari bilangan bulat X, bilangan yang memenuhi kondisi yang sudah
    disebutkan.

    Format Input:
    Input pertama ialah integer-integer yang dipisahkan dengan spasi, yang
    merupakan elemen dari array pertama, yaitu A.
    Input kedua ialah integer-integer yang dipisahkan dengan spasi, yang
    merupakan elemen dari array kedua, yaitu B.

    Format Output:
    Output merupakan sebuah integer, yaitu X, jumlah bilangan yang memenuhi
    kondisi yang sudah disebutkan.

    Contoh Input:
    2 4
    16 32 96

    Contoh Output:
    3

    Penjelasan:
    A = [2, 4]
    B = [16, 32, 96]
    Faktor dari semua elemen array B: [1, 2, 4, 8, 16]
    Dari bilangan-bilangan di atas, yang memiliki faktor 2 dan 4 hanya:
    [4, 8, 16]
    Sehingga jumlah bilangan bulat X yang memenuhi kondisi adalah 3.
"""

def getTotalX(a, b):
    all_factors = []
    total_x = 0

    for i in b:
        all_factors += getFactors(i)

    all_factors = list(set(filter(lambda x: all_factors.count(x) == len(b), all_factors)))

    for j in all_factors:
        check = [j % k for k in a]
        if check.count(0)==len(a):
            total_x += 1
            
    return total_x

def getFactors(num):
    lower_bound = 1
    upper_bound = num
    factors = []

    while lower_bound<upper_bound:
        if num % lower_bound == 0:
            factors.append(lower_bound)
            upper_bound = num / lower_bound
            factors.append(int(upper_bound))
        lower_bound += 1

    return sorted(list(set(factors)))

"""
    Challenge ini diadaptasi dari HackerRank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 17/01/2021
"""
