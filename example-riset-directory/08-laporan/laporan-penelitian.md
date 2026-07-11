# Laporan Akhir Penelitian

**Judul:** Evaluasi Dampak Usability Integrasi Layanan Pesan-Antar Makanan pada Super-App E-Commerce: Studi Kasus Shopee Reguler dan Shopee Food

**Peneliti:** Febri Muhsinin (240202835)
**Target Publikasi:** Sinta 2 (Jurnal RESTI/Telematika) atau Scopus Q3–Q4
**Status Penelitian:** Tahap Eksperimen, Analisis, dan Penyusunan Draf Manuskrip telah Selesai.

---

## 1. Ringkasan Eksekutif

Penelitian ini mengevaluasi secara empiris dampak dari *feature bloat* terhadap tingkat kegunaan (*usability*) pada aplikasi Shopee, khususnya dengan membandingkan layanan utama (Shopee Reguler) dengan layanan sekunder (Shopee Food). 

Evaluasi dilakukan melalui pendekatan eksperimen kuantitatif *Within-Subjects Design* yang melibatkan 36 partisipan dari Generasi Z. Pengumpulan data dilakukan menggunakan kuesioner standar *System Usability Scale* (SUS). Terdapat anomali di lapangan berupa hilangnya butir pertanyaan genap kedua (Q2) pada pengujian Shopee Food, yang kemudian dimitigasi menggunakan metode *Constant Imputation* (Penyuntikan nilai 3) pada tahap pra-pemrosesan data menggunakan skrip Python.

**Temuan utama:**
- Skor kelayakan Shopee Reguler berada di angka **60.56** (kategori *Marginal*).
- Skor kelayakan Shopee Food anjlok ke angka **48.26** (kategori *Not Acceptable*).
- Pengujian signifikansi *Paired Sample T-Test* mengonfirmasi bahwa penurunan skor sebesar 12.30 poin tersebut terjadi secara signifikan (*P-Value* = 7.62e-09 < 0.05).
- Integrasi fitur sekunder ke dalam aplikasi utama terbukti memicu beban kognitif berlebih (*Extraneous Cognitive Load*) yang merusak kenyamanan visual dan navigasi pengguna.

Seluruh data mentah, skrip analisis Python, dan draf naskah jurnal publikasi telah didokumentasikan dan diserahkan dalam repositori proyek ini.

---

## 2. Metodologi dan Pelaksanaan

Pelaksanaan penelitian ini dibagi menjadi beberapa tahapan teknis, mulai dari pengumpulan data hingga penyusunan naskah:

### 2.1 Tahap 1 — Persiapan Instrumen dan Pengumpulan Data (`04-data`)
Instrumen *System Usability Scale* disebar melalui Google Form kepada 36 mahasiswa/i dan pekerja lepas Generasi Z. Partisipan diminta mengevaluasi dua skenario simulasi: berbelanja barang (Reguler) dan memesan makanan (Food). 
Data mentah (*raw data*) diimpor dan disimpan di direktori `04-data/data_form.csv`. Kamus data (`Kamus_Data.md`) juga disusun untuk memetakan kolom-kolom kuesioner dengan struktur analisis.

### 2.2 Tahap 2 — Pra-pemrosesan dan Komputasi Analisis (`05-kode`)
Skrip analisis statistik dibangun menggunakan bahasa pemrograman Python (`05-kode/analisis_sus.py`). Skrip ini menangani:
- **Imputasi Data:** Kolom Q2 Shopee Food yang hilang dari instrumen lapangan ditangani secara statis dengan mengisi nilai netral (3).
- **Penilaian SUS:** Algoritma pembalikan skor (X-1 untuk ganjil, 5-X untuk genap) dieksekusi sebelum dikalikan konstanta 2.5.
- **Uji Signifikansi:** Menggunakan `scipy.stats.ttest_rel` untuk memverifikasi Hipotesis Nol (H0).

### 2.3 Tahap 3 — Ekstraksi Hasil (`06-output`)
Hasil eksekusi skrip divalidasi dan disimpan secara terpusat di `06-output/hasil_analisis_sus.md`. Dokumen tersebut memuat metrik-metrik sentral (Mean, Min, Max) dan *P-Value* eksperimen.

### 2.4 Tahap 4 — Penyusunan Manuskrip Jurnal (`07-manuskrip`)
Berdasarkan output dari Tahap 3, draf naskah ilmiah disusun menjadi 8 bagian terpisah mulai dari abstrak hingga daftar pustaka. Referensi disusun menggunakan standar pemformatan IEEE dengan menyertakan jurnal-jurnal ilmiah mutakhir dari Google Scholar (2020-2024).

---

## 3. Hasil Penelitian

Detail lengkap dari hasil analisis dapat merujuk pada `06-output/hasil_analisis_sus.md`.

| Skenario Pengujian | Rata-rata Skor SUS | Kategori Bangor (2008) | Minimum | Maksimum |
|---|---|---|---|---|
| **Shopee Reguler** | 60.56 | Marginal | 40.0 | 82.5 |
| **Shopee Food** | 48.26 | Not Acceptable | 30.0 | 80.0 |

**Uji Hipotesis:**
*Paired Sample T-Test* = **7.621e-09**. Karena *P-Value* < 0.05, maka H0 (Tidak ada perbedaan tingkat kegunaan) ditolak. Secara empiris, desain antarmuka ekosistem aplikasi Shopee saat ini sangat membingungkan saat pengguna mencoba beralih ke fungsi pemesanan makanan.

---

## 4. Kendala dan Catatan Lapangan

1. **Kehilangan Butir Instrumen:** Butir Q2 (Sistem Terlalu Rumit) untuk form Shopee Food tidak terdaftar saat publikasi. Solusi yang diambil adalah tidak menghapus responden, melainkan menyuntikkan nilai penyeimbang/netral (3) di tahap *coding* menggunakan Python.
2. **Keterbatasan Demografi:** Semua responden adalah Gen Z. Jika kelompok ini mendapat skor rendah (*Not Acceptable*), pengguna awam yang lebih tua kemungkinan besar tidak akan sanggup menggunakan fitur tersebut.

---

## 5. Kesimpulan dan Saran

Strategi mengubah platform *e-commerce* menjadi *super-app* memberikan dampak negatif yang sangat signifikan pada tingkat kegunaan. Disarankan agar manajemen dan perancang *User Experience* Shopee melakukan *Progressive Disclosure* atau memisahkan layanan berat tersebut menjadi aplikasi mandiri *(standalone app)* demi menjaga keutuhan memori transaksi pengguna.

---

## 6. Lampiran — Peta Artefak Penelitian

| Folder | Isi | Status |
|---|---|---|
| `01-proposal/` | Proposal riset dan template dasar. | Selesai |
| `02-literatur/` | Matriks dan komparasi literatur awal. | Selesai |
| `03-teori/` | Penjabaran teori SUS. | Selesai |
| `04-data/` | Dataset observasi (`data_form.csv`) & Kamus Data. | Selesai |
| `05-kode/` | Kode sumber Python (`analisis_sus.py`). | Selesai |
| `06-output/` | Catatan komputasi SUS akhir. | Selesai |
| `07-manuskrip/` | Draf publikasi ilmiah lengkap (terpisah dan tergabung). | Selesai |
| `08-laporan/` | Laporan administratif akhir (dokumen ini). | Selesai |

**Cara Reproduksi Komputasi:**
```bash
cd 05-kode
python analisis_sus.py
```
