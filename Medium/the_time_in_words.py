"""
    The Time in Words
    Difficulty: ✰✰

    Diberikan waktu dalam bentuk angka, konversikan ke dalam frasa seperti ini.

        5:00 - five o' clock
        5:01 - one minute past five
        5:10 - ten minutes past five
        5:15 - quarter past five
        5:30 - half past five
        5:40 - twenty minutes to six
        5:45 - quarter to six
        5:59 - one minute to six
        5:28 - twenty eight minutes past five

    Saat menit = 0, gunakan o' clock. Untuk 1 <= menit <= 30, gunakan past, dan
    untuk 30 < menit, gunakan to.
    
    Tugas:
    Buatlah sebuah fungsi akan mengembalikan string, yang merupakan bentuk waktu
    dalam kata/frasa. Fungsi akan menerima parameter berikut ini.
        - h, integer, merupakan jam dalam satuan waktu
        - m, integer, merupakan menit dalam satuan waktu

    Format Input:
    Input pertama adalah h, yang merupakan jam dalam satuan waktu.
    Input kedua adalah m, yang merupakan menit dalam satuan waktu

    Format Output:
    Output adalah sebuah string, yang merupakan bentuk waktu dalam kata/frasa.

    Contoh Input:
    12
    13

    Contoh Output:
    thirteen minutes past twelve

    Catatan:
    Format waktu yang digunakan adalah format 12 jam (AM/PM). Sehingga, jika
    12:59, sama dengan one minute to one.
"""

def timeInWords(h, m):
    timeWord = ''
    h = h+1 if m > 30 else h
    h = 1 if h > 12 else h
    
    if m == 0: timeWord += '{0} o\' clock'.format(numberInWords(h))
    elif m == 1: timeWord += 'one minute past {0}'.format(numberInWords(h))
    elif m == 15: timeWord += 'quarter past {0}'.format(numberInWords(h))
    elif m == 30: timeWord += 'half past {0}'.format(numberInWords(h))
    elif m == 45: timeWord += 'quarter to {0}'.format(numberInWords(h))
    elif m == 59: timeWord += 'one minute to {0}'.format(numberInWords(h))
    else:
        status = 'past' if m < 30 else 'to'
        minuteWord = numberInWords(60-m) if m > 30 else numberInWords(m)
        hourWord = numberInWords(h) if m < 30 else numberInWords(h)
        timeWord += '{0} minutes {1} {2}'.format(minuteWord, status, hourWord)
        
    return timeWord

def numberInWords(num):
    numbers_dict = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty'
    }
    
    if num <= 20: return numbers_dict[num]
    else:
        satuan = num % 10
        puluhan = num - satuan
        return '{0} {1}'.format(numbers_dict[puluhan], numbers_dict[satuan])

h = int(input())
m = int(input())

print(timeInWords(h, m))

"""
    Challenge ini diadaptasi dari Hackerrank
    Alih bahasa oleh bpkcongli
    Solusi logika oleh bpkcongli
    Created with ♥ by bpkcongli on 31/01/2021
"""
