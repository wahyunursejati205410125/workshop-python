STRUKTUR DATA 

tipe data memiliki banyak metode

Data Daftar

dapat digunakan untuk berbagai hal seperti sebagai antrian, tumpukan, pemahaman. 
Untuk menambahkan item ke atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, 
gunakan pop()tanpa indeks eksplisit.
Untuk mengimplementasikan antrean, gunakan collections.dequewhich dirancang untuk 
menambahkan dan muncul dengan cepat dari kedua ujungnya.

Pernyataan Del 

Ada cara untuk menghapus item dari daftar yang diberikan indeksnya 
alih-alih nilainya: pernyataan del. Ini berbeda dari pop()metode yang 
mengembalikan nilai. Pernyataan itu deljuga dapat digunakan untuk menghapus 
irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya
dengan menugaskan daftar kosong ke irisan).

Tupen dan Urutan

pada tupel keluaran selalu tertutup dalam tanda kurung, 
sehingga tupel bersarang diinterpretasikan dengan benar; 
mereka mungkin dimasukkan dengan atau tanpa tanda kurung di sekitarnya, 
meskipun seringkali tanda kurung diperlukan (jika tuple adalah bagian 
dari ekspresi yang lebih besar).
Meskipun tupel mungkin tampak mirip dengan daftar, 
mereka sering digunakan dalam situasi yang berbeda
dan untuk tujuan yang berbeda. Tuple bersifat immutable , 
dan biasanya berisi rangkaian elemen heterogen yang diakses 
melalui pembongkaran (lihat nanti di bagian ini) atau 
pengindeksan (atau bahkan dengan atribut dalam kasus ) namedtuples. 
Daftar bisa berubah , dan elemennya biasanya homogen dan diakses dengan 
mengulangi daftar.

Set

Set objek mendukung operasi matematika seperti penyatuan, 
persimpangan, perbedaan, dan perbedaan simetris.
Kurung kurawal atau set()fungsi dapat digunakan untuk membuat himpunan.

Kamus

Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci 
dan mengekstraksi nilai yang diberikan kunci tersebut. 
Dimungkinkan juga untuk menghapus key:value pair dengan del.

Teknik Perulangan

Saat mengulang kamus, kunci dan nilai yang sesuai dapat diambil pada 
saat yang sama menggunakan items().
Saat mengulang urutan, indeks posisi dan nilai terkait dapat diambil 
pada saat yang sama menggunakan enumerate().
Untuk mengulangi dua urutan atau lebih secara bersamaan, 
entri dapat dipasangkan dengan fungsi zip().
Untuk mengulang urutan secara terbalik, pertama-tama tentukan urutan dalam 
arah maju dan kemudian panggil fungsinya reversed().

