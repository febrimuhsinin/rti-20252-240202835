## 4. HASIL DAN PEMBAHASAN

### 4.1 Statistik Deskriptif Skor SUS (Berdasarkan 06-output)
Berdasarkan perhitungan matematis SUS dari 36 partisipan valid yang mengacu pada data mentah di `04-data/` dan analisis `05-kode/analisis_sus.py`, didapatkan rekapitulasi data sebagai berikut:
- **Shopee Reguler:** Rata-rata Skor = 60.56 (Min = 40.0, Max = 82.5)
- **Shopee Food:** Rata-rata Skor = 48.26 (Min = 30.0, Max = 80.0)

Berdasarkan klasifikasi penilaian *Adjective Rating Scale* Bangor (2008), skor Shopee Reguler (60.56) berada di kelas kelayakan **Marginal** (Tingkat penerimaan rendah/sedang), sementara Shopee Food (48.26) jatuh secara mutlak ke kategori **Not Acceptable**.

### 4.2 Uji Hipotesis Komparatif (Paired T-Test)
Pengujian signifikansi *Paired T-Test* (N=36) antara kedua kondisi eksperimen (*within-subjects*) menghasilkan nilai signifikansi atau *P-Value* sebesar **7.621e-09**. Mengingat *P-Value* jauh lebih kecil dari standar signifikansi *alpha* (0.05), maka **Hipotesis Nol (H0) ditolak** secara meyakinkan.

### 4.3 Analisis Dampak (*Cognitive Overload*)
Penolakan H0 dan margin perbedaan skor (*mean difference* = 12.30) membuktikan secara empiris bahwa arsitektur antarmuka Shopee Food di dalam ekosistem *super-app* saat ini memicu *Extraneous Cognitive Load* yang masif. Data instrumen SUS mengindikasikan bahwa responden merasa harus mempelajari lebih banyak hal sebelum dapat memesan makanan (Q10) dan menilai sistem tidak praktis (Q8). Hal ini terjadi karena fitur yang saling bersilangan (belanja barang, dompet digital, promosi restoran) berbenturan dengan niat utama pengguna, yang secara logaritmik memperparah waktu dan beban kognitif pengambilan keputusan (*Hick's Law*).
