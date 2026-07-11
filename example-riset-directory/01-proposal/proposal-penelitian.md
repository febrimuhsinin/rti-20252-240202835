# PROPOSAL PENELITIAN

## A. JUDUL
Evaluasi Dampak Usability Integrasi Layanan Pesan-Antar Makanan pada Super-App E-Commerce: Studi Kasus Perbandingan Shopee Reguler dan Shopee Food

## B. RINGKASAN
Penelitian ini mengevaluasi dampak penggabungan fitur (*feature bloat*) terhadap tingkat kegunaan aplikasi Shopee sebagai *super-app*, dengan memfokuskan komparasi antara layanan belanja reguler dan layanan pesan-antar makanan (Shopee Food). Evaluasi eksperimental kuantitatif dilakukan dengan pendekatan *within-subjects design* kepada 36 pengguna Generasi Z. Pengukuran kemudahan penggunaan dilakukan melalui kuesioner baku *System Usability Scale* (SUS). Tujuan utamanya adalah untuk menguji apakah arsitektur informasi pada fitur sekunder (Shopee Food) memicu beban kognitif berlebih (*cognitive overload*) yang signifikan dibandingkan dengan alur transaksi belanja utama. Metode analisis yang digunakan adalah *Paired Sample T-Test* melalui skrip Python. Luaran yang ditargetkan dari penelitian ini adalah artikel ilmiah pada jurnal Sinta 2 (seperti Jurnal RESTI) atau Scopus Q3/Q4, yang akan memberikan panduan evaluasi berbasis data bagi pengembang produk e-commerce dalam menata kompleksitas navigasi antarmuka *super-app*.

## C. KATA KUNCI
Super-App; Usability; System Usability Scale; Feature Bloat; Cognitive Overload;

## D. PENDAHULUAN

### D.1. LATAR BELAKANG DAN RUMUSAN MASALAH
Dalam beberapa tahun terakhir, ekosistem digital di Asia Tenggara mengalami tren transisi masif dari aplikasi fungsi tunggal (e-commerce konvensional) menjadi *Super-App* (aplikasi serbaguna). Shopee kini telah mengintegrasikan berbagai layanan, salah satunya adalah Shopee Food. Meskipun penambahan turunan layanan ini ditujukan untuk meretensi pengguna ke dalam satu ekosistem, dari kacamata *User Experience* (UX) dan *Human-Computer Interaction* (HCI), penjejalan terlalu banyak fitur yang berbeda konteks ke dalam satu aplikasi memunculkan risiko *Cognitive Overload* pada pengguna (terutama Generasi Z). Pengguna yang sekadar ingin membeli barang bisa kebingungan karena banyaknya opsi, banner, dan navigasi yang saling tumpang tindih. Akar masalahnya adalah memaksakan kerangka informasi pemesanan makanan ke dalam platform belanja fisik. Dampaknya, jika tingkat kemudahan (*usability*) pada layanan Shopee Food ternyata sangat rendah, hal ini dapat mengurangi daya saing perusahaan.

Oleh karena itu, rumusan masalah utama penelitian ini adalah: "Apakah terdapat perbedaan tingkat kegunaan (*usability*) yang signifikan antara antarmuka alur belanja Shopee Reguler dibandingkan dengan antarmuka Shopee Food di kalangan pengguna Generasi Z?"

### D.2. PENDEKATAN PEMECAHAN MASALAH
Tujuan penelitian ini adalah membuktikan secara empiris ada atau tidaknya indikasi degradasi *usability* akibat penumpukan fitur (*feature bloat*) dengan membandingkan langsung skor kegunaan dua layanan di aplikasi yang sama. Hipotesis awal (H1) menyatakan bahwa alur pemesanan Shopee Food dinilai memiliki tingkat *usability* yang secara signifikan lebih membingungkan (skor lebih rendah) dibandingkan alur belanja reguler. Pendekatan pemecahan masalah yang diusulkan adalah komparasi metrik skor *System Usability Scale* (SUS) dengan eksperimen terkontrol, yang menetapkan layanan belanja reguler sebagai kondisi *baseline* terhadap intervensi layanan sekunder.

### D.3. STATE OF THE ART DAN KEBARUAN
Studi literatur terdahulu, seperti Hidayat et al. (2021) dan penelitian lain mengenai Shopee, sebagian besar hanya mengevaluasi skor kegunaan aplikasi Shopee secara utuh (agregat), tanpa melakukan isolasi evaluasi perbandingan antar-fitur (*super-app versus layanan utama*). *Benchmark* praktik pengukuran SUS sebelumnya jarang yang mempertanyakan dampak integrasi fitur silang secara kuantitatif. Terdapat *research gap* atau celah riset terkait komparasi presisi antara layanan utama dengan layanan ekspansi dalam suatu ekosistem yang sama. Kebaruan penelitian ini terletak pada penerapan metode *within-subjects design* untuk mengisolasi efek perubahan layar secara sangat spesifik dan mengevaluasi kerusakan kenyamanan (*cognitive overload*) ketika pengguna beralih konteks (dari transaksi belanja ke pemesanan makanan).

### D.4. PETA JALAN PENELITIAN
1. Perancangan usulan penelitian dan penyusunan instrumen (menentukan hipotesis komparatif dan variabel *super-app*).
2. Persiapan instrumen kuesioner SUS dan penyebaran form daring ke sampel (36 responden Generasi Z).
3. Tabulasi data awal dan penulisan pra-pemrosesan data dengan bahasa *Python*.
4. Eksekusi eksperimen analitis untuk menangani kendala teknis *missing value* (hilangnya butir instrumen secara struktural) menggunakan imputasi konstanta.
5. Eksekusi komputasi statistik *Paired Sample T-Test*.
6. Ekstraksi visualisasi hasil *usability* (skor, *mean difference*, signifikansi *P-Value*).
7. Penulisan manuskrip untuk publikasi di jurnal berstandar tinggi (Sinta 2 / Scopus).

## E. METODE

### E.1. Desain Penelitian dan Unit Analisis
Penelitian ini merupakan penelitian kuantitatif eksperimental dengan tipe rancangan penelitian *Within-Subjects Design*. Tipe desain ini memastikan setiap subjek/responden akan menguji kedua kondisi eksperimen secara berurutan. Hipotesis utama berfokus pada penurunan skor SUS secara signifikan. Objek/unit analisis pada riset ini adalah kualitas arsitektur antarmuka aplikasi seluler. Kondisi *baseline* adalah skenario pengalaman antarmuka berbelanja fisik pada Shopee Reguler, sedangkan *intervensi* (pembanding) adalah pengalaman antarmuka layanan pesan-antar Shopee Food.

### E.2. Variabel, Metric, Instrumen, dan Data
- **Variabel Independen:** Konteks skenario tugas pada aplikasi (Kondisi A: Shopee Reguler, Kondisi B: Shopee Food).
- **Variabel Dependen:** Tingkat kebergunaan (skor SUS).
- **Variabel Kontrol:** Rentang demografi usia (18-25 tahun/Gen Z) dan *platform* sistem operasi (*smartphone*).
- **Metric Utama:** Skor akhir skala absolut (0-100).
- **Instrumen:** Kuesioner baku *System Usability Scale* (10 pernyataan dengan skala *Likert* 1-5).
- **Sumber Data/Responden:** 36 partisipan yang dikumpulkan melalui sampel *purposive* kuesioner *Google Form*.

### E.3. Skenario dan Prosedur Pengujian
Responden diinstruksikan untuk membayangkan atau menyelesaikan simulasi tugas (berbelanja produk) menggunakan Shopee Reguler (kondisi *baseline*), lalu mengisi kuesioner 10 poin instrumen SUS untuk mengevaluasi interaksinya. Setelah itu, pada form yang sama, responden diminta mensimulasikan tugas pemesanan pada layanan Shopee Food, dan kembali mengisi 10 poin instrumen SUS. Prosedur ini dijaga ketat agar dilakukan oleh partisipan yang persis sama untuk meredam variabel pengganggu seperti ketimpangan tingkat literasi digital.

### E.4. Artifact, Setup, atau Kesiapan Implementasi
Lingkungan eksperimen dijalankan secara *in-the-wild* pada aplikasi Shopee yang telah terpasang di masing-masing perangkat *smartphone* responden tanpa modifikasi aplikasi. Instrumen pengumpulan data menggunakan Google Form. Kesiapan komputasi analisis diimplementasikan dalam skrip bahasa *Python* (dengan library *Pandas* dan *SciPy*) yang secara otomatis memroses data mentah (.csv) untuk mengubah bobot skor positif/negatif kuesioner dan menghitung statistik parametriknya.

### E.5. Teknik Analisis, Asumsi, dan Validitas
Data tanggapan form akan dibaca, dikonversi sesuai bobot algoritma SUS, lalu dijumlahkan dan dikalikan faktor 2,5. Teknik analisis akhir menggunakan uji parametrik *Paired Sample T-Test* untuk menilai signifikansi selisih *Mean* (P-Value). Asumsi pengujian normalitas dipenuhi dengan mempertimbangkan teorema *Central Limit Theorem* (n=36 > 30). Ancaman validitas yang ada adalah absennya butir ke-2 (Q2) instrumen Shopee Food dari publikasi *form*. Solusi validitasnya adalah skrip akan mengimputasi skor netral sentral (nilai 3) secara paksa (*Constant Imputation*) sehingga komparasi absolut dengan skor SUS reguler dapat tetap dipertanggungjawabkan tanpa memotong kuota subjek.

## F. HASIL YANG DIHARAPKAN
Hasil yang ditargetkan dari riset ini adalah ditemukannya bukti kuantitatif empiris yang solid mengenai degradasi *usability* (*cognitive overload*) pada Shopee Food dibandingkan dengan fitur *baseline* e-commerce utama. Hasil ini akan menjadi dasar bagi usulan praktik perbaikan antarmuka *super-app* (misalnya penggunaan *Progressive Disclosure*). Luaran konkret (*deliverable*) berupa dataset primer observasi lapangan, berkas kode pemrograman, laporan penelitian teknis, dan sebuah draf artikel jurnal siap *publish* berformat IEEE.

## G. JADWAL PENELITIAN
| No | Nama kegiatan | Bulan 1 | Bulan 2 | Bulan 3 | Bulan 4 |
|---|---|---|---|---|---|
| 1 | Identifikasi *gap* permasalahan (observasi awal) | X | | | |
| 2 | Desain eksperimen dan persiapan kuesioner SUS | X | | | |
| 3 | Pengumpulan data dari responden eksperimental | | X | | |
| 4 | Koding dan otomatisasi pra-pemrosesan data (*Python*) | | X | | |
| 5 | Analisis skor dan eksekusi komputasi *Paired T-Test* | | | X | |
| 6 | Interpretasi data, validasi, dan penulisan luaran | | | X | X |
| 7 | Penyusunan laporan penelitian dan manuskrip akhir | | | | X |

## H. DAFTAR PUSTAKA
[1] J. Brooke, "SUS - A quick and dirty usability scale," *Usability Evaluation in Industry*, vol. 189, no. 194, pp. 4-7, 1996.

[2] W. E. Hick, "On the rate of gain of information," *Quarterly Journal of Experimental Psychology*, vol. 4, no. 1, pp. 11-26, 1952.

[3] A. Bangor, P. Kortum, and J. Miller, "An Empirical Evaluation of the System Usability Scale (SUS)," *International Journal of Human-Computer Interaction*, vol. 24, no. 6, pp. 574-594, 2008.

[4] R. Budiu, "Between-Subjects vs. Within-Subjects Study Design," *Nielsen Norman Group*, 2021. [Online]. Available: https://www.nngroup.com/articles/between-within-subjects/

[5] A. T. Hidayat, et al., "Analisis Usability Pada Aplikasi Shopee Menggunakan Metode System Usability Scale (SUS)," *Jurnal Ilmiah Komputasi*, vol. 20, no. 3, 2021.

[6] N. F. Rozi, et al., "Analisis Usability Fitur Live Shopping pada Aplikasi Shopee Menggunakan Metode System Usability Scale (SUS)," *Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi)*, 2023.
