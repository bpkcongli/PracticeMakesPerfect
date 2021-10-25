"""
    Seorang pendaki gemar membuat catatan tentang pendakiannya. Selama
    pendakian terakhirnya, ia mencatat setiap langkah yang ia buat, seperti
    langkah menanjak (U) ataupun langkah menurun (D). Pendakian selalu dimulai
    dan diakhiri di ketinggian yang sama dengan permukaan laut.

    Pendaki dapat mendaki gunung: yang digambarkan sebagai urutan langkah
    yang berurutan di atas ketinggian permukaan laut, dimulai dengan naik dari
    ketinggian permukaan laut hingga turun kembali ke ketinggian permukaan laut.
    Pendaki juga dapat menuruni lembah: yang digambarkan sebagai urutan langkah
    yang berurutan di bawah ketinggian permukaan laut, dimulai dengan turun dari
    ketinggian permukaan laut hingga naik kembali ke ketinggian permukaan laut.

    Berdasarkan catatan dari si pendaki, tentukan berapa jumlah gunung dan
    lembah yang dilalui oleh si pendaki.

    Tugas:
    Buatlah sebuah fungsi yang akan mengembalikan dua buah integer, yang masing
    masing merepresentasikan jumlah gunung dan lembah yang dilalui oleh pendaki.
    Fungsi menerima parameter berupa string yang merupakan catatan si pendaki
    yang menggambarkan langkah yang ia buat selama melakukan pendakian.

    Format Input:
    Input berupa string yang merupakan catatan si pendaki yang menggambarkan
    langkah yang ia buat selama melakukan pendakian.

    Format Output:
    Output berupa dua buah integer yang dipisahkan dengan spasi, berurutan ialah
    m, yaitu jumlah gunung yang dilalui oleh pendaki selama pendakian, dan v,
    yaitu jumlah lembah yang dilalui oleh pendaki selama pendakian.

    Contoh Input:
    UDDDUDUU

    Contoh Output:
    1 1

    Penjelasan:
    Catatan pendaki bisa digambarkan sebagai berikut.
    
       _/\      _
          \    /
           \/\/

    Dengan _ adalah permukaan laut, / adalah langkah menanjak, dan \ adalah
    langkah menurun. Dari gambar di atas, bisa disimpulkan pendaki melewati
    1 gunung dan 1 lembah selama pendakian.
"""

def countingValleys(steps):
    sea_levels = 0
    total_mountains = total_valleys = 0
    
    for step in steps:
        on_valley = True if sea_levels < 0 else False
        on_mountain = True if sea_levels > 0 else False
        if step == 'U': sea_levels += 1
        else: sea_levels -= 1
        if on_valley and sea_levels == 0: total_valleys += 1
        if on_mountain and sea_levels == 0: total_mountains += 1
        
    return '{0} {1}'.format(total_mountains, total_valleys)

print(countingValleys(input()))

"""
    Challenge ini diadaptasi dari HackerRank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 17/01/2021
"""
