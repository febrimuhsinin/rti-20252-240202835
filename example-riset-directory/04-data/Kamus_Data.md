# Kamus Data (*Data Dictionary*)

Dokumen ini menjelaskan struktur kolom dari data riil kuesioner `data form.csv` yang dikumpulkan selama penelitian komparasi *usability* Shopee Reguler dan Shopee Food.

## 1. Metadata Umum
| Indeks Kolom | Nama Kolom Asli (G-Form) | Deskripsi | Tipe Data | Format / Keterangan |
|---|---|---|---|---|
| 0 | Timestamp | Waktu pengisian survei | Datetime | `MM/DD/YYYY HH:MM:SS` |
| 1 | Email Address | Alamat email partisipan | String | Disamarkan / *Redacted* |
| 2 | Nama Lengkap | Nama lengkap partisipan | String | Indikator Cek Duplikat |
| 3 | Usia (Rentang 18-25 Tahun) | Konfirmasi Usia Gen Z | Kategori | Hanya 18-25 Tahun (Syarat Validitas) |
| 4 | Jenis Kelamin | Gender | Kategori | Laki-laki / Perempuan |
| 5 | Pernah Berbelanja di Shopee & Food? | Syarat Partisipan | Kategori | Ya (Valid) |

## 2. Bagian A: Shopee Reguler (10 Pertanyaan SUS)
Rentang Jawaban (1 - 5): 1=Sangat Tidak Setuju, 5=Sangat Setuju.

| Indeks Kolom | Kode Soal | Tipe | Pertanyaan Asli |
|---|---|---|---|
| 6 | REG_Q1 | Ganjil (+) | Saya berpikir akan sering menggunakan fitur belanja (Reguler) di Shopee |
| 7 | REG_Q2 | Genap (-) | Saya merasa fitur belanja (Reguler) di Shopee ini terlalu rumit |
| 8 | REG_Q3 | Ganjil (+) | Saya merasa fitur belanja (Reguler) di Shopee mudah digunakan |
| 9 | REG_Q4 | Genap (-) | Saya butuh bantuan teknis untuk menggunakan fitur belanja (Reguler) di Shopee |
| 10 | REG_Q5 | Ganjil (+) | Saya merasa fitur-fitur belanja (Reguler) di Shopee terintegrasi dengan baik |
| 11 | REG_Q6 | Genap (-) | Saya merasa ada ketidakkonsistenan yang besar dalam fitur belanja (Reguler) di Shopee |
| 12 | REG_Q7 | Ganjil (+) | Saya membayangkan orang lain akan cepat belajar memakai fitur belanja (Reguler) di Shopee |
| 13 | REG_Q8 | Genap (-) | Saya merasa desain fitur belanja (Reguler) di Shopee sangat tidak praktis |
| 14 | REG_Q9 | Ganjil (+) | Saya merasa yakin (percaya diri) saat menggunakan fitur belanja (Reguler) di Shopee |
| 15 | REG_Q10| Genap (-) | Saya harus belajar banyak hal sebelum saya bisa memulai fitur belanja (Reguler) di Shopee |

## 3. Bagian B: Shopee Food (Missing Q2)

> **[!] ANOMALI STRUKTURAL DATA:** 
> Pertanyaan **Q2 Shopee Food** (Genap/Negatif) tidak dimasukkan saat perancangan *Google Form*. Karena rumus SUS membutuhkan skor 10 butir pertanyaan secara mutlak, nilai untuk Q2 Food **diimputasi secara paksa (Constant Imputation)** dengan skor netral, yaitu angka **3**, di dalam *script* `process_real_corrected.py` dan `analisis_sus.py`.

| Indeks Kolom | Kode Soal | Tipe | Pertanyaan Asli |
|---|---|---|---|
| 16 | FOD_Q1 | Ganjil (+) | Saya berpikir akan sering menggunakan layanan pesan-antar ShopeeFood |
| - | **FOD_Q2** | **Genap (-)** | **[HILANG DARI FORM] Diimputasi Statis = 3 (Netral)** |
| 17 | FOD_Q3 | Ganjil (+) | Saya merasa layanan ShopeeFood mudah digunakan |
| 18 | FOD_Q4 | Genap (-) | Saya merasa butuh bantuan orang teknis untuk bisa memakai layanan ShopeeFood |
| 19 | FOD_Q5 | Ganjil (+) | Saya merasa fitur-fitur di layanan ShopeeFood sudah terintegrasi dengan baik |
| 20 | FOD_Q6 | Genap (-) | Saya merasa ada ketidakkonsistenan yang besar pada fitur-fitur di ShopeeFood |
| 21 | FOD_Q7 | Ganjil (+) | Saya membayangkan mayoritas orang akan cepat belajar memakai layanan ShopeeFood |
| 22 | FOD_Q8 | Genap (-) | Saya merasa sistem pada layanan ShopeeFood ini sangat tidak praktis |
| 23 | FOD_Q9 | Ganjil (+) | Saya merasa yakin (percaya diri) saat memakai layanan ShopeeFood |
| 24 | FOD_Q10| Genap (-) | Saya harus belajar banyak hal sebelum saya bisa memesan via ShopeeFood |

## 4. Konversi Data & Pembobotan (Preprocessing)
- **Pertanyaan Ganjil (+):** Nilai Skor = (Jawaban - 1)
- **Pertanyaan Genap (-):** Nilai Skor = (5 - Jawaban)
- **Total Skor SUS:** (Total Skor Ganjil + Total Skor Genap) * 2.5
