## 3. METODOLOGI PENELITIAN

### 3.1 Arsitektur Eksperimen (Within-Subjects Design)
Penelitian ini menerapkan metode eksperimental kuantitatif dengan pendekatan *Within-Subjects Design* (Budiu, 2021). Desain ini dipilih agar setiap partisipan (N=36) bertindak sebagai kontrol bagi dirinya sendiri; yakni secara berurutan mengevaluasi Skenario A (Shopee Reguler) lalu diikuti dengan Skenario B (Shopee Food).

### 3.2 Kriteria Partisipan
Partisipan direkrut secara *purposive sampling* dengan kriteria Generasi Z (usia 18-25 tahun) yang pernah menggunakan layanan Shopee Reguler dan Shopee Food. Pemilihan demografi Gen Z ini didasari oleh asumsi literasi digital: jika kelompok pengguna yang paling adaptif secara digital ini mengalami *cognitive overload*, maka populasi umum dipastikan akan merasakan friksi yang lebih berat.

### 3.3 Skema Pengujian dan Pengumpulan Data
Instrumen pengumpulan data diadopsi secara penuh dari kuesioner baku *System Usability Scale* (SUS) yang ditransformasi ke dalam media *Google Form*. Terdapat anomali struktural selama pengumpulan data lapangan berupa tidak tersedianya butir Q2 pada bagian evaluasi Shopee Food. Mengikuti prinsip keutuhan matematis 10-butir dari formula SUS, anomali data yang hilang tersebut diatasi melalui teknik *Constant Imputation* dengan menyuntikkan nilai netral (3) pada fase pra-pemrosesan data menggunakan skrip analisis.

### 3.4 Metode Analisis Data
Untuk memverifikasi perbedaan tingkat usabilitas secara saintifik, uji hipotesis komparatif dilakukan menggunakan *Paired Sample T-Test* (Alpha = 0.05) dengan bantuan pustaka statitik komputasional Python (`scipy.stats.ttest_rel`).
