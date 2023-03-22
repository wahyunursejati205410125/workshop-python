*pertemuan 02*
Selain whilepernyataan yang baru saja diperkenalkan, Python menggunakan pernyataan kontrol aliran biasa yang dikenal dari bahasa lain, dengan beberapa perubahan.

IF PERNYATAAN

Sebuah if… elif… elif… urutan adalah pengganti switchatau casepernyataan yang ditemukan dalam bahasa lain.
Jika Anda membandingkan nilai yang sama dengan beberapa konstanta, atau memeriksa tipe atau atribut tertentu, Anda mungkin juga menganggap matchpernyataan itu berguna.

FOR PERNYATAAN

Daripada selalu mengulangi perkembangan aritmatika angka (seperti di Pascal), atau memberi pengguna kemampuan untuk menentukan langkah iterasi dan menghentikan kondisi (sebagai C), pernyataan Python mengulangi item dari urutan apa pun (daftar atau fora string), dalam urutan yang muncul dalam urutan. Misalnya (tidak ada permainan kata-kata)

FUNGSI RANGE()

Dalam banyak hal objek yang dikembalikan oleh range()berperilaku seolah-olah itu adalah daftar, tetapi sebenarnya bukan. Ini adalah objek yang mengembalikan item berturut-turut dari urutan yang diinginkan saat Anda mengulanginya, tetapi tidak benar-benar membuat daftar, sehingga menghemat ruang.

DEF

Kata kunci def memperkenalkan definisi fungsi, harus diikuti dengan nama fungsi dan daftar parameter formal dalam kurung. Pernyataan-pernyataan yang membentuk badan fungsi dimulai dari baris berikutnya, dan harus diindentasi. Pernyataan pertama dari badan fungsi secara opsional dapat berupa string literal. string literal adalah string dokumentasi fungsi, atau docstring.
Parameter khusus : - Argumen Posisi-atau-Kata Kunci - Parameter Hanya Posisi - Argumen Hanya Kata Kunci - Contoh Fungsi - Rekap Daftar Argumen sewenang-wenang : opsi yang paling jarang digunakan adalah menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen yang berubah-ubah. Argumen-argumen ini akan dibungkus dalam sebuah tupel. Sebelum jumlah variabel argumen, nol atau lebih argumen normal dapat terjadi Fungsi anonim kecil dapat dibuat dengan kata kunci lambda. Fungsi ini mengembalikan jumlah dari dua argumennya: lambda a, b: a+b. Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Secara sintaksis terbatas pada satu ekspresi. Secara semantik, mereka hanyalah gula sintaksis untuk definisi fungsi normal. Seperti definisi fungsi bersarang, fungsi lambda dapat mereferensikan variabel dari cakupan yang berisi.
