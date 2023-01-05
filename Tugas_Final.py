#papan catur kosong 8x8 dalam bentuk list
posisi = [[' ' for i in range(8)] for i in range(8)]

#membuka file teks 
teks = open(input('contoh file teks : teks3.txt\n\nInput file teks : '),"r")

#Mengubah isi file teks menjadi list 
list_teks = teks.read().split("/")

#mengubah isi list menjadi int
def int_list(list_teks):
    for i in list_teks:
        try:
            list_teks[list_teks.index(i)] = int(i)
        except ValueError:
            pass
    return list_teks
list_teks = int_list(list_teks)

#mengubah format list_teks dari seperti ini [2n5] menjadi [' ', ' ', 'n', ' ', ' ', ' ', ' ', ' '] dan memasukannya ke list posisi    
for i in list_teks: 
    if type(i) != int: 
        if len(i) <= 8: 
            list_kosong = [] 
            posisi[list_teks.index(i)] = int_list(list(i))#menggunakan fungsi user
            for j in posisi[list_teks.index(i)]: #perulangan untuk mengubah nomor dalam list_teks menjadi petak kosong dan dimasukan ke list kosong
                if type(j) == int:
                    list_kosong.extend(' '*j)
                if type(j) != int: #perulangan untuk menambahkan yang bukan nomor ke list kosong
                    list_kosong.append(j)
            posisi[list_teks.index(i)] = list_kosong #mengubah isi list posisi menggunaka list kosong yang telah diisi

#mengubah posisi dengan list apabila formatnya sudah sesuai

#menutup akses file
teks.close()

#daftar nilai buah catur
nilai = {'k':200,'K':200,'q':9,'Q':9,'r':5,'R':5,'b':3,'B':3,'n':3,'N':3,'p':1,'P':1}

#fungsi nilai_buah catur
def nilai_buah(posisi,pemain):
    #Kode untuk menghitung nilai buah catur dan menampilkannya untuk pemain putih
    if pemain == 'Hitam' or pemain == 'hitam':
        string_posisi = [x for x in posisi for x in x] # Mengubah list dalam list posisi menjadi 1 list
        buah_catur = {#dictionary untuk mencatat jumlah masing masing buah catur
          'k': 0,
          'q': 0,
          'r': 0,
          'b': 0,
          'n': 0,
          'p': 0
        }
        total_buah_catur = 0 #inisialisasi untuk total buah catur
        for i in string_posisi: #perulangan untuk menghitung buah catur
          if i in ['k', 'q', 'r', 'b',  'n', 'p']:
            buah_catur[i] += 1
            total_buah_catur += 1
        print(f'\nTotal buah catur pemain hitam: {total_buah_catur}')#menampilkan nilai buah catur
        print(' ')
        print(f"""\
        King -> {buah_catur['k']} = {nilai['k'] * buah_catur['k']}
        Queen -> {buah_catur['q']} = {nilai['q'] * buah_catur['q']}
        Rook -> {buah_catur['r']} = {nilai['r'] * buah_catur['r']}
        Bishop -> {buah_catur['b']} = {nilai['b'] * buah_catur['b']}
        Knight -> {buah_catur['n']} = {nilai['n'] * buah_catur['n']}
        Pawn -> {buah_catur['p']} = {nilai['p'] * buah_catur['p']}\
        """)
        print(' ')
        hasil = (nilai['k'] * buah_catur['k'])+(nilai['q'] * buah_catur['q'])+(nilai['r'] * buah_catur['r'])+(nilai['b'] * buah_catur['b'])+(nilai['n'] * buah_catur['n'])+(nilai['p'] * buah_catur['p'])
        return 'Nilai total semua buah catur' + ' ' + '=' + ' ' + str(hasil)
    #Kode untuk menghitung nilai buah catur dan menampilkannya untuk pemain Hitam    
    elif pemain == 'Putih' or pemain == 'putih':
        string_posisi = [x for x in posisi for x in x]
        buah_catur = {
          'K': 0,
          'Q': 0,
          'R': 0,
          'B': 0,
          'N': 0,
          'P': 0
        }
        total_buah_catur = 0
        for i in string_posisi:
          if i in ['K', 'Q', 'R', 'B',  'N', 'P']:
            buah_catur[i] += 1
            total_buah_catur += 1
        print(f'\nTotal Buah catur pemain putih: {total_buah_catur}')
        print(' ')
        print(f"""\
        King -> {buah_catur['K']} = {nilai['K'] * buah_catur['K']}
        Queen -> {buah_catur['Q']} = {nilai['Q'] * buah_catur['Q']}
        Rook -> {buah_catur['R']} = {nilai['R'] * buah_catur['R']}
        Bishop -> {buah_catur['B']} = {nilai['B'] * buah_catur['B']}
        Knight -> {buah_catur['N']} = {nilai['N'] * buah_catur['N']}
        Pawn -> {buah_catur['P']} = {nilai['P'] * buah_catur['P']}\
        """)
        print(' ')
        hasil = (nilai['K'] * buah_catur['K'])+(nilai['Q'] * buah_catur['Q'])+(nilai['R'] * buah_catur['R'])+(nilai['B'] * buah_catur['B'])+(nilai['N'] * buah_catur['N'])+(nilai['P'] * buah_catur['P'])
        return 'Nilai total semua buah catur = ' + str(hasil)
    
#Fungsi untuk menghitung petak kosong
def jumlah_petak_kosong(posisi):
    string_posisi = [x for x in posisi for x in x]
    jumlah_petak_kosong = 0
    for i in string_posisi:
        if i == ' ':
            jumlah_petak_kosong += 1
    return 'Jumlah Petak kosong dalam papan catur = ' + str(jumlah_petak_kosong)

#main program untuk menampilkan list posisi            
print(f'\nList Posisi Pada papan catur\n')
baris = 0
while baris <= 7:
    i = posisi[baris]
    baris += 1
    print('Baris ke ',baris,i)
print('')

#main program untuk menampilkan fungsi nilai_buah
print(f"Input pemain untuk menghitung nilai buah catur (Putih/hitam)\n")
pemain = input('pemain = ')
print(nilai_buah(posisi,pemain))

#main program untuk menampilkan petak kosong
print(f'\n{jumlah_petak_kosong(posisi)}')
#main program untuk mengakhiri program
akhir = input('\nProgram Telah selesai')
    


