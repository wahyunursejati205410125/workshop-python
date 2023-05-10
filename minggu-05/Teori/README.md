Jika Anda ingin menulis nilai selain ekspresi dan fungsi print(), Anda juga dapat menggunakan metode write() dari objek file.

Ada beberapa cara untuk memformat output:


Untuk menggunakan string yang diformat secara harfiah, awali string dengan f atau F sebelum tanda kutip terbuka atau tiga. Di dalam string ini, Anda bisa menulis ekspresi Python di antara karakter { dan }, yang bisa merujuk ke variabel atau nilai literal.
Metode string str.format(). Menggunakan { dan } untuk menandai di mana variabel perlu diganti dapat memberikan instruksi pemformatan yang mendetail, tetapi juga harus memberikan informasi pemformatan. Anda dapat menangani sendiri semua string dengan membuat tata letak dengan fungsi pemotongan dan penyambungan string. Tipe string memiliki beberapa metode yang menjalankan fungsi yang berguna untuk mengisi string hingga lebar kolom tertentu.
str() digunakan untuk mengembalikan representasi nilai yang dapat dibaca manusia, sementara repr() digunakan untuk membuat representasi yang dapat dibaca juru bahasa (atau untuk memaksa SyntaxError jika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, str() mengembalikan nilai yang sama dengan repr().

Literal string berformat (f-string) memungkinkan nilai ekspresi Python untuk disertakan dalam string dengan mengawali string dengan f atau F dan menulis ekspresi sebagai {ekspresi}. Penggunaan dasar metode str.format() Tanda kurung dan karakter yang dikandungnya (disebut bidang format) diganti dengan objek yang diteruskan ke metode str.format(). Angka dalam tanda kurung dapat digunakan untuk menunjukkan posisi objek yang diteruskan ke metode str.format().

Pemformatan string lama:
Operator % (module) dapat digunakan untuk memformat string. Nilai % 'string', misalnya �lam string diganti dengan nol atau lebih elemen nilai. Operasi ini umumnya dikenal sebagai interpolasi string 
