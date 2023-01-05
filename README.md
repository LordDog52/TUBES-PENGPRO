# TUBES-PENGPRO CATUR HULA-HULA
Deskripsi file teks:
Diberikan beberapa contoh file teks berisi data posisi permainan catur (papan ukuran 8x8). Buah catur hitam menggunakan huruf kecil, buah catur putih menggunakan huruf kapital, angka menyatakan petak kosong, dan ‘/’ adalah batas setiap baris pada papan catur.
Setiap buah-buah catur itu memiliki nilai dengan rincian sebagai berikut:
k/K = king bernilai 200
q/Q = queen bernilai 9
r/R = rook bernilai 5
b/B = bishop bernilai 3
n/N = knight bernilai 3
p/P = pawn bernilai 1

Contoh File Teks
File teks 1: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
File teks 2: 4k3/8/8/8/8/8/4P3/2K5

Contoh pembacaan file:
4k3/8/8/8/8/8/4P3/4K3 artinya pada baris pertama king hitam berada di petak ke 5 (4 petak kosong di sebelah kiri, dan 3 petak kosong di sebelah kanan). Baris kedua hingga keenam, 8 petak kosong semua. Baris ketujuh, hanya ada pawn putih di petak kelima, sedangkan di baris kedelapan, king putih ada dipetak ketiga.

Tugas:
a. Buatlah sebuah sebuah list bernama posisi berdasarkan pembacaan file teks itu.
b. Buatlah fungsi nilai_buah untuk mengembalikan nilai buah catur salah satu pemain. Fungsi memiliki dua parameter, yaitu posisi dengan tipe list dan pemain dengan tipe string.
c. Buatlah fungsi jumlah_petak_kosong yang digunakan untuk menghitung jumlah petak kosong pada papan catur. Fungsi memiliki satu parameter, yaitu posisi dengan tipe list.
d. Buatlah main program yang digunakan untuk menampilkan list dan memanggil fungsi yang dibuat.
