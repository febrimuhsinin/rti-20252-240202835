## 4. HASIL DAN PEMBAHASAN

### 4.1 Statistik Deskriptif Skor SUS (Berdasarkan Output Python)
Berdasarkan perhitungan algoritmik dari data mentah 36 partisipan valid menggunakan skrip analisis Python (`analisis_sus.py`), skor *System Usability Scale* dihitung dengan kaidah standar: skor pertanyaan ganjil dikurangi satu (X-1), dan skor pertanyaan genap dikurangkan dari lima (5-X), lalu totalnya dikalikan 2.5.

Rekapitulasi komparatif akhir menghasilkan statistik deskriptif sebagai berikut:
- **Shopee Reguler (Skenario Utama):** Rata-rata Skor = 60.56 (Min = 40.0, Max = 82.5)
- **Shopee Food (Skenario Sekunder):** Rata-rata Skor = 48.26 (Min = 30.0, Max = 80.0)

Berdasarkan rentang klasifikasi *Adjective Rating Scale* dari Bangor et al. (2008), skor Shopee Reguler (60.56) berada di persentil kelas kelayakan **Marginal** (Tingkat penerimaan menengah/rendah). Sementara itu, dampak *feature bloat* terlihat sangat destruktif pada skor Shopee Food (48.26) yang jatuh secara mutlak di bawah ambang batas aman 50, menjadikannya masuk ke kategori **Not Acceptable** (Tidak Dapat Diterima).

### 4.2 Uji Hipotesis Komparatif (Paired T-Test)
Untuk memastikan bahwa penurunan skor (selisih rata-rata sebesar 12.30 poin) ini bukan diakibatkan oleh kebetulan semata (*random chance*), dilakukan pengujian signifikansi menggunakan *Paired Sample T-Test* (N=36).

Hasil pengeluaran komputasi menghasilkan nilai probabilitas (*P-Value*) sebesar **7.621e-09** (atau 0.000000007621). Mengingat *P-Value* tersebut teramat jauh lebih kecil dibandingkan dengan standar level signifikansi *alpha* (0.05), maka **Hipotesis Nol (H0) ditolak** secara meyakinkan. Kesimpulan statistiknya adalah terdapat perbedaan tingkat kegunaan yang sangat persisten dan konsisten memburuk ketika pengguna berpindah dari alur belanja reguler ke alur pesan-antar makanan.

### 4.3 Analisis Dampak (*Cognitive Overload* dan Arsitektur UI)
Penolakan H0 membuktikan secara empiris tesis utama penelitian ini: desain arsitektur informasi Shopee Food yang disuntikkan secara paksa ke dalam ekosistem *super-app* memicu *Extraneous Cognitive Load* yang masif. 

Meskipun secara bisnis integrasi ini diklaim memudahkan pengguna tanpa perlu mengunduh aplikasi terpisah, realitas UX justru membuktikan sebaliknya. Data instrumen SUS mengindikasikan bahwa responden mayoritas memberikan penilaian negatif pada butir-butir krusial seperti Q8 (*Sistem sangat tidak praktis/Cumbersome*) dan Q10 (*Perlu banyak belajar sebelum mengoperasikan*). Hal ini selaras dengan dalil *Hick's Law*. Ketika pengguna memasuki laman Shopee Food, mereka dibombardir oleh antarmuka visual yang berebut atensi—mulai dari pop-up diskon yang tumpang tindih dengan menu restoran, ikon gamifikasi yang tidak pada tempatnya, hingga tombol integrasi dompet digital yang membingungkan alur *checkout* utama.

Kekacauan *Information Architecture* ini merampas memori kerja pengguna, memaksa otak (*cognitive processing*) bekerja keras hanya untuk melakukan penyaringan elemen (*visual filtering*) alih-alih mengambil keputusan pembelian makanan secara efisien.
