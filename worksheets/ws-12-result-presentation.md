# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Apakah terdapat perbedaan skor System Usability Scale (SUS) yang signifikan antara alur transaksi belanja reguler dengan alur transaksi pada fitur Shopee Food bagi pengguna Generasi Z?
Metrik Utama      : Skor System Usability Scale (SUS) dengan skala 0 - 100

Tabel Hasil (Berdasarkan Data Riil N=36):
| Skenario        | Skor SUS (mean ± std) | n |
|-----------------|-----------------------|---|
| Belanja Reguler | 60.56 ± 10.32         | 36 |
| Shopee Food     | 48.26 ± 9.37          | 36 |

*(Catatan: Pertanyaan ke-2 pada kuesioner Shopee Food terlewat saat pengumpulan data di Google Form. Nilai untuk item ini diimputasi dengan nilai netral (3) agar kalkulasi SUS tetap dapat dilakukan).* 

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Box Plot                         | Distribusi sebaran skor SUS dan keberadaan nilai ekstrem/outlier                 | Skor SUS (0-100)            |
| 2 | Bar Chart + Error Bar            | Perbandingan visual beda rata-rata kepuasan antara kedua alur                    | Rata-rata Skor SUS ± Std     |
| 3 | User Journey Map / Peta Hambatan | Titik retensi spesifik di mana responden mengalami kebingungan (Friction points) | Frekuensi / Persentase Error |

Bias Check:
  [x] Y-axis mulai dari 0 (Sumbu Y pada grafik SUS wajib dikunci pada rentang absolut 0 - 100)
  [x] Error bar/CI ditampilkan (Untuk menunjukkan tingkat variabilitas data/standar deviasi responden)
  [x] Semua data disertakan (30 data valid tidak ada yang di-cherry-pick)
  [x] Tidak menggunakan 3D tanpa alasan (Desain grafik dibuat 2D minimalis dan akademis)
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda berdasarkan data riil yang telah diolah.

| Skenario               | Skor SUS (mean ± std)  |  n  |
|------------------------|------------------------|-----|
| *Alur Belanja Reguler* | *60.56 ± 10.32 (Marginal / Grade D)* | *36* |
| *Alur Shopee Food*     | *48.26 ± 9.37 (Not Acceptable / Grade F)* | *36* |

**Catatan Penting Data:** Terdapat *missing data* secara struktural di mana pertanyaan No.2 untuk Shopee Food tidak dimasukkan ke dalam Google Form. Kalkulasi di atas menggunakan asumsi nilai netral (3) untuk pertanyaan yang hilang tersebut.

**Checklist tabel:**
- [x] Self-contained (Tabel jelas menunjukkan perbandingan Skor SUS dan jumlah sampel N=36).
- [x] Mean ± std (Menyajikan rata-rata dan standar deviasinya, bukan single number).
- [x] Diurutkan berdasarkan metrik utama (Diurutkan dari skenario baseline menuju skenario perlakuan).
- [x] Format konsisten di semua baris.
---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | *Bar chart + Error bar*          | *Membuktikan bahwa terdapat penurunan signifikan skor SUS pada Shopee Food dibandingkan alur reguler.*                                        | *Mean Skor SUS ± Standard Deviation dari kedua skenario.* |
| 2 | *Box plot*                       | *Memperlihatkan distribusi jawaban kelompok Gen Z, melihat apakah datanya memusat atau tersebar jauh karena kebingungan yang bervariasi.* | *Skor absolut responden (0-100)*                                            |
| 3 | *Peta Visual (User Journey Map)* | *Memetakan di bagian mana kompleksitas antarmuka paling mendegradasi efisiensi pengguna saat bertransisi ke fitur Shopee Food.* | *Data kualitatif opsional dan metrik waktu di halaman spesifik.* |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan?        | *Ya — Y-axis yang dipotong (Truncated axis) membuat perbedaan 0.4% terlihat seperti selisih yang sangat masif, sehingga manipulatif.* |
| Apakah error bar ditampilkan?     | *Tidak — Tidak ada error bar sehingga kita tidak tahu variabilitas (standard deviation) datanya. Jangan-jangan 0.4% itu tidak signifikan sama sekali.* |
| Apakah semua kondisi ditampilkan? | *Ya, namun disajikan secara tidak proporsional dan tidak menggambarkan batas nilai absolut.* |
| Apa solusinya?                    | *Mulai sumbu Y dari angka 0, gunakan Y-axis skala penuh (0-100%), dan tambahkan Error Bar/Confidence Interval pada setiap batang.* |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus (Sumbu Y untuk skor SUS akan di-set ketat dari 0 hingga 100 agar representatif).
- [ ] Ada yang perlu diperbaiki: -

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Keduanya sangat diperlukan karena memiliki fungsi psikologis dsn analitis yang berbeda. Tabel diperlukan untuk validasi presisi (pembaca bisa melihat angka persis rata-rata dan standar deviasi hingga desimal tertentu untuk dihitung ulang). Sementara itu, Grafik/Visualisasi diperlukan untuk pengenalan pola (pattern recognition) secara instan; otak manusia jauh lebih cepat memproses "grafik Shopee Food terlihat anjlok/menurun" daripada harus membandingkan deretan angka di tabel.

Pengalaman: Saya mungkin pernah (tanpa sengaja) membuat grafik garis (line chart) di Excel di mana sumbu Y-nya otomatis menyesuaikan angka terendah (tidak mulai dari 0). Akibatnya, perbedaan data yang sebenarnya sangat tipis terlihat seperti penurunan tajam/drastis, yang berpotensi membiaskan kesimpulan orang yang membacanya. Kesalahan default setting software ini sering kali menjadi jebakan bias visualisasi.
> ___________________________________________________
