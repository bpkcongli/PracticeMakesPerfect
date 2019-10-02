# PmP (Practices makes Perfect) Part 1:
# Mengurutkan Karakter pada String tanpa Menggunakan Built-in Method pada Python
# Difficulty : Easy

# Overview:
# Buatlah sebuah function yang bertujuan untuk mengurutkan karakter pada string.
# Function menerima string sebagai argument, lalu string diproses sedemikian rupa
# sehingga setiap karakter pada string terurut dengan urutan dimulai dari:
# 1. Special Character (Simbol dan Tanda Baca)
# 2. Number
# 3. Alphabet
# 4. Tanda spasi harus diabaikan
# Function akan menghasilkan return value berupa string yang karakternya sudah diurutkan.

# Objective:
# 1. Menggunakan Function Argument dan Return Value
# 2. Menggunakan Algoritma Sorting: Selection Sort

# Expected Result:
# Input: bohemian
# Output: abehimno
#
# Input: alpha123
# Output: 123aahlp
#
# Input: $t4r qu33n
# Output: $334nqrtu

# Source Code:
# String yang akan diurutkan
my_str = '@lpha123 .'

# Definisi fungsi sort() dengan strinput sebagai parameter
def sort(strinput):
    # Mengubah string yang akan diurutkan menjadi list
    strinput = list(strinput)
    # Selection Sort Algorithm akan mengurutkan karakter berdasarkan nilai ASCII
    # Nilai ASCII paling kecil dimulai dari special character, simbol, angka, dan huruf
    for x in range(len(strinput)):
        # Diasumsikan indeks pertama (dari unsorted list) sebagai karakter dengan nilai ASCII paling kecil
        min = x
        # Membandingkan nilai ASCII indeks pertama dengan indeks yang lain
        for y in range(x+1, len(strinput)):
            # Jika ada indeks lain yang nilai ASCII-nya lebih kecil dari indeks pertama
            if ord(strinput[min]) > ord(strinput[y]):
                # Update nilai dari variable min
                # Looping dilakukan terus-menerus sampai indeks terakhir untuk menemukan indeks dengan nilai ASCII paling kecil
                min = y
        # Jika sudah ditemukan, tukar posisi indeks pertama (dari unsorted list) dengan indeks yang nilai ASCII-nya paling kecil
        # Ini berarti indeks pertama diisi dengan karakter dengan nilai ASCII terkecil (kita sebut dengan sorted list)
        strinput[x], strinput[min] = strinput[min], strinput[x]
        # Unsorted list sekarang dimulai dari indeks ke-1

    # Definisi variable untuk menyimpan hasil
    result = ''
    # Filter apakah string yang sudah diurutkan memiliki spasi
    for x in strinput:
        if x != ' ':
            result += x

    # Mengembalikan nilai sebagai string
    return result

# Testing Code:
print('Sebelum diurutkan: ' + my_str)
print('Sesudah diurutkan: ' + sort(my_str))
