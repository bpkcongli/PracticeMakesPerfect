"""
    Append and Delete
    Difficulty: ✰✰

    Kamu memiliki dua buah string yang terdiri dari huruf kecil. Kamu dapat
    melakukan dua tipe operasi pada string yang pertama, yaitu:

        - Menambahkan huruf kecil ke posisi akhir dari string
        - Menghapus karakter terakhir dari string. Melakukan operasi ini pada
          string kosong akan menghasilkan string kosong juga.

    Diketahui integer k, dan dua buah string, s dan t. Tentukan apakah kamu
    dapat mengkonversi string s ke string t dengan melakukan k operasi yang
    sudah disebutkan di atas. Jika iya, cetak Yes. Jika tidak, cetak No.

    Contoh:

        s = 'man'
        t = 'main'
        k = 3

        Untuk mengkonversikan string s ke string t, pertama-tama hapus karakter
        'n' dari string s, dengan ini ada satu operasi yang dilakukan. Setelah
        itu, tambahkan karakter 'i' dan 'n' sehingga sekarang string s sama
        dengan string t. Total ada tiga operasi yang dilakukan. Kembalikan Yes.

        Jumlah operasi yang mungkin untuk dikembalikan Yes:
        5: Hapus 'n' dan 'a'. Tambahkan 'a', 'i', dan 'n'.
        7: Hapus seluruh karakter. Tambahkan 'm', 'a', 'i', dan 'n'.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan 'Yes' atau 'No'. Fungsi ini
    memiliki parameter sebagai berikut:
        - s, string yang akan dilakukan operasi
        - t, target string, s akan berpatokan dengan t
        - k, jumlah operasi yang harus dilakukan

    Format Input:
    Input pertama adalah s.
    Input kedua adalah t.
    Input ketiga adalah k.

    Format Output:
    Output adalah sebuah string, 'Yes' jika string s bisa dikonversi ke string
    t dengan melakukan persis sebanyak k operasi, dan 'No' jika sebaliknya.

    Contoh Input:
    black
    white
    10

    Contoh Output:
    Yes

    Penjelasan:
    Coming Soon
"""

def appendAndDelete(s, t, k):
    status = False
    
    while k>=0:
        if len(s) == 0:
            if len(t) <= k: status = True
            break
        if s == t[:len(s)]:
            remain_operation = len(t.split(s)[1])
            if remain_operation == 0:
                status = True if k > 2*len(t) or (k <= 2*len(t) and k%2 == 0) else False
            else:
                status = True if k >= remain_operation and (k-remain_operation)%2 == 0 or k>len(s)+len(t) else False
            break
        else:
            s = s[:-1]
        k -= 1
        
    return 'Yes' if status else 'No'

s = input()
t = input()
k = int(input())

print(appendAndDelete(s, t, k))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 22/01/2021
"""
