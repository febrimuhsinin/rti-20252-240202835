# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG (UX Research Context)

Dataset           : Respons Raw Google Form (Skenario Reguler & Shopee Food)
Jumlah data awal  : 32 Responden (Data mentah sebelum disaring)

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 0           | Dibiarkan                       | Semua pertanyaan di Google Form di-set "Wajib Isi" (Required) sehingga tidak ada data kosong. |
| Duplikat| 0           | Pengecekan                      | Identifikasi via nama/email menunjukkan tidak ada responden yang mengisi dua kali. |
| Error   | 2 Responden | Hapus baris (Listwise deletion) | 1 responden berusia 27 tahun (melanggar kontrol batas Gen Z 18-25 tahun). 1 responden terdeteksi straight-lining (menjawab skor 5 untuk semua item positif dsn negatif secara asal-asalan). |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Konversi Skor SUS | 10 Item Pernyataan Likert | Item Ganjil (X-1). Item Genap (5-Y). Total dikali 2,5. | Mengubah data ordinal (Likert 1-5) menjadi data interval (Skala absolut 0-100) sesuai aturan baku instrumen System Usability Scale. |

Normalization (Feature Scaling):
  Metode    : Tidak diterapkan (Tidak Perlu Scaling) 
  Alasan    : Skor SUS sudah memiliki batasan rentang absolut yang baku secara internasional (0 hingga 100). Melakukan Z-Score atau Min-Max Scaling justru akan merusak interpretasi standar kelas SUS (Grade Scale / Adjective Rating).
  Parameter : -

Leakage Check (Dalam konteks eksperimen UX):
  [x] Tidak ada kontaminasi antar skenario (Counterbalancing Form A & Form B sudah diterapkan untuk mencegah efek pembelajaran / Order Bias).
  [x] Transformasi data Likert dilakukan secara terpisah dsn independen untuk tiap sesi (Sesi Reguler vs Sesi Food).

Jumlah data akhir : 30 Responden Valid 
Script tersedia   : [x] Ya → path: Template_Kalkulator_SUS.xlsx | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau simulasi dataset jika sedang mengambil data) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| *Responden melanggar batas demografi*              | *1 (dari 32)* | *Hapus dari dataset (Listwise deletion)* | *Melanggar Variabel Kontrol (Harus Gen Z usia 18-25 tahun dsn Mahasiswa Aktif)* |
| *Straight-lining / Speeding (Mengisi asal-asalan)* | *1 (dari 32)* | *Hapus dari dataset (Listwise deletion)* | *Menjawab nilai "5" untuk semua pertanyaan ganjil dsn genap, memicu anomali logika karena pertanyaan SUS bersifat selang-seling (positif/negatif).* |

**Jumlah data sebelum cleaning:** 32 partisipan
**Jumlah data setelah cleaning:** 30 partisipan Persentase data yang hilang/berubah: 6.25% (Data dibuang dan diganti dengan responden baru agar target minimal N=30 terpenuhi).
**Persentase data yang hilang/berubah:** ____%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| *Skor SUS Belanja Reguler* | *0 - 100* | *Normal (diuji dgn Shapiro-Wilk)* | *Tidak* | *Tidak Perlu Feature Scaling* | *Rentang data sudah baku [0-100]. Skala tidak boleh diubah agar bisa dipetakan ke Acceptability Ranges standard SUS.* |
| *Skor SUS Shopee Food*     | *0 - 100* | *Normal (diuji dgn Shapiro-Wilk)* | *Tidak* | *Rentang data sudah baku [0-100].* |


**Apakah normalisasi diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
> Dalam analisis kuesioner UX seperti SUS, normalisasi data (seperti Z-score atau Min-Max) tidak diperbolehkan karena nilai instrumen sudah memiliki rasio absolut 0-100. Jika data dinormalisasi ulang, kita tidak akan bisa mencocokkan hasil eksperimen dengan benchmark literatur global. (Catatan: Normalisasi di sini merujuk pada scaling rentang data, BUKAN Uji Asumsi Normalitas Distribusi Statistik untuk Syarat T-Test yang tetap wajib dilakukan).

**Leakage check:**
- [ ] Parameter dihitung dari training set saja
- [ ] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: Respons Google Form Eksperimen Shopee (Reguler vs Food)
2. Data awal: 32 records responden, 20 features (10 Pertanyaan SUS x 2 Skenario)
3. Cleaning:
   - Missing values: 0 kasus, metode: Tidak ada (karena required field di form)
   - Duplikat: 0 kasus, tindakan: Verifikasi nama/identitas unik
   - Error (Outlier Kontrol): 2 kasus (1 di luar rentang usia, 1 mengisi asal-asalan), tindakan: Listwise deletion (dihapus).
4. Transformation: Konversi jawaban ordinal Likert (1-5) menjadi rasio Skor SUS menggunakan formula konvensional baku [(X-1) untuk ganjil, (5-Y) untuk genap, Total dikali 2.5].
5. Normalisasi: Tidak diterapkan (metode scaling dibiarkan raw), parameter range dikunci pada 0-100.
6. Data akhir: 30 records responden valid , 2 features utama (Skor SUS Reguler & Skor SUS Food).
7. Leakage check: [x] Lulus (Tidak ada kebocoran perlakuan berkat skema counterbalancing)  / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Banyak pemula yang secara otomatis menerapkan algoritma Min-Max Scaling atau Z-score Normalization pada semua kolom dataset di Python/SPSS hanya karena mengikuti kebiasaan atau tutorial, tanpa melihat konteks variabelnya.

Risiko dari over-preprocessing ini, terutama pada riset UI/UX, adalah hilangnya makna kontekstual dari data. Jika nilai SUS sebesar "40" (yang secara universal berarti aplikasi tersebut sangat buruk/Not Acceptable)  dinormalisasi paksa menggunakan Z-score di dalam kelompok data yang semuanya bernilai rendah, angka tersebut bisa saja terdistorsi terlihat normal atau di tengah-tengah rentang. Distorsi ini akan menipu peneliti dsn menghasilkan kesimpulan akhir yang salah fatal terhadap usability aplikasi yang diuji. Karena itu, prinsip Minimal Distortion sangat penting dijaga.

