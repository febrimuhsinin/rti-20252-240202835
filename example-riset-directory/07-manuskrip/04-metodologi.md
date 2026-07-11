## 3. METODOLOGI PENELITIAN

### 3.1 Arsitektur Eksperimen (Within-Subjects Design)
Penelitian ini menerapkan metode eksperimental kuantitatif. Untuk mengurangi bias variasi antar-individu (misalnya perbedaan kecerdasan atau literasi teknologi antar kelompok), penelitian ini menggunakan pendekatan *Within-Subjects Design* (Budiu, 2021). Dalam desain ini, setiap partisipan bertindak sebagai kelompok kontrol bagi dirinya sendiri. Artinya, setiap individu (N=36) secara berurutan mengevaluasi Skenario A (Pengalaman menggunakan alur belanja Shopee Reguler) lalu diikuti dengan Skenario B (Pengalaman menggunakan alur pesan-antar Shopee Food) dalam satu sesi yang sama.

### 3.2 Kriteria dan Demografi Partisipan
Partisipan direkrut menggunakan metode *purposive sampling* dengan kriteria inklusi yang ketat: Generasi Z (rentang usia 18 hingga 25 tahun), berstatus mahasiswa atau *fresh-graduates*, dan wajib memiliki pengalaman menggunakan layanan Shopee Reguler sekaligus Shopee Food sebelumnya.

Pemilihan demografi spesifik Generasi Z ini bukan tanpa alasan empiris. Gen Z dikenal sebagai generasi *digital native* yang paling adaptif terhadap perubahan antarmuka aplikasi. Asumsi metodologis yang mendasari pemilihan ini adalah: Jika kelompok umur yang paling melek teknologi dan adaptif ini saja mengalami *cognitive overload* dan kebingungan (*usability issue*) saat menggunakan aplikasi, maka dapat disimpulkan dengan tingkat keyakinan tinggi bahwa populasi umum (seperti Milenial dan *Baby Boomers*) dipastikan akan merasakan friksi dan kebingungan yang jauh lebih parah.

### 3.3 Skema Pengujian dan Pengumpulan Data
Sebelum mengisi kuesioner, partisipan diberikan stimulus berupa *task scenario* (skenario tugas) imajiner. Pertama, mereka diminta membayangkan alur pencarian barang fisik hingga menambahkannya ke keranjang belanja (Reguler). Kedua, mereka diminta membayangkan alur masuk ke menu Shopee Food, mencari restoran, hingga proses validasi pesanan makanan (Food).

Setelah membayangkan kedua skenario, partisipan mengevaluasi pengalaman tersebut melalui instrumen baku 10 butir pertanyaan *System Usability Scale* (SUS) berbahasa Indonesia yang didistribusikan secara daring melalui *Google Form*.

### 3.4 Penanganan Anomali Data (Constant Imputation)
Terdapat sebuah anomali struktural selama proses implementasi survei lapangan, yakni insiden administratif berupa hilangnya butir pertanyaan genap kedua (Q2) khusus pada form bagian evaluasi Shopee Food. Rumus standar matematis SUS mensyaratkan eksistensi ke-10 pertanyaan secara mutlak untuk dapat menghasilkan skala 0-100.

Untuk menyelamatkan validitas instrumen tanpa mencederai integritas data, anomali *missing value* ini diatasi menggunakan teknik *Constant Imputation* pada tahap pra-pemrosesan data (*preprocessing*). Setiap nilai Q2 Shopee Food yang kosong disuntikkan dengan nilai konstan 3 (Tiga). Angka 3 dipilih karena merupakan titik netral (Tengah) pada skala Likert 1-5, sehingga metode imputasi statis ini diasumsikan tidak akan secara sepihak memanipulasi skor akhir menjadi condong terlalu positif maupun terlalu negatif.

### 3.5 Metode Analisis Data
Untuk memverifikasi perbedaan tingkat usabilitas secara saintifik dan objektif, uji komparatif hipotesis dilakukan menggunakan *Paired Sample T-Test* dengan tingkat signifikansi standar (*Alpha* = 0.05). Komputasi inferensial ini dieksekusi secara otomatis berbantuan pustaka statitik komputasional Python, yakni fungsi `scipy.stats.ttest_rel`.
