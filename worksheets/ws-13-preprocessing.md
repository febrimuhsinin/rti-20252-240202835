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
| Missing | 36 Kasus (Struktural) | Imputasi nilai Netral (3) | Pertanyaan No. 2 pada kuesioner Shopee Food tidak dimasukkan ke dalam Google Form. Nilai diimputasi dengan skor 3 agar formula SUS tetap valid (10 pertanyaan). |
| Duplikat| 0           | Pengecekan                      | Identifikasi via nama menunjukkan tidak ada responden ganda. |
| Error   | 0           | Tidak ada                       | Semua 36 responden masuk kriteria Gen Z dan tidak melakukan pengisian *straight-lining* ekstrem. |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Konversi Skor SUS | Item Pernyataan Likert | Item Ganjil (X-1). Item Genap (5-Y). Total dikali 2,5. | Mengubah data ordinal (Likert 1-5) menjadi data interval (Skala absolut 0-100) sesuai standar baku System Usability Scale. Khusus Food Q2 menggunakan asumsi skor netral. |

Normalization (Feature Scaling):
  Metode    : Tidak diterapkan (Tidak Perlu Scaling) 
  Alasan    : Skor SUS sudah memiliki batasan rentang absolut yang baku secara internasional (0 hingga 100). Melakukan Z-Score atau Min-Max Scaling justru akan merusak interpretasi standar kelas SUS (Grade Scale / Adjective Rating).
  Parameter : -

Leakage Check (Dalam konteks eksperimen UX):
  [x] Tidak ada kontaminasi antar skenario (Counterbalancing Form A & Form B sudah diterapkan untuk mencegah efek pembelajaran / Order Bias).
  [x] Transformasi data Likert dilakukan secara terpisah dsn independen untuk tiap sesi (Sesi Reguler vs Sesi Food).

Jumlah data akhir : 36 Responden Valid 
Script tersedia   : [x] Ya → path: `process_real_corrected.py` | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau simulasi dataset jika sedang mengambil data) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| *Missing Data Struktural (Shopee Food Q2 Hilang)* | *36 baris (Semua data)* | *Imputasi (Constant Imputation) = 3* | *Google Form luput menyertakan Q2 untuk bagian Shopee Food. Karena SUS butuh 10 skor absolut, Q2 diimputasi dengan nilai netral (3).* |

**Jumlah data sebelum cleaning:** 36 partisipan
**Jumlah data setelah cleaning:** 36 partisipan (Data utuh, hanya diimputasi)
**Persentase data yang diimputasi:** 5% (1 dari 20 pertanyaan per responden)

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
2. Data awal: 36 records responden, 19 features SUS (10 Reguler + 9 Food)
3. Cleaning:
   - Missing values: Q2 Shopee Food missing secara struktural untuk semua baris. Metode: *Constant Imputation* dengan skor netral (3).
   - Duplikat: 0 kasus
   - Error (Outlier Kontrol): 0 kasus (Semua responden Gen Z dan mengisi dengan wajar).
4. Transformation: Konversi jawaban ordinal Likert (1-5) menjadi Skor SUS [(X-1) ganjil, (5-Y) genap, dikali 2.5] melalui *script* Python `process_real_corrected.py`.
5. Normalisasi: Tidak diterapkan, parameter range dikunci absolut 0-100.
6. Data akhir: 36 records valid, 2 features utama (Skor SUS Reguler & Skor SUS Food siap uji T-Test).
7. Leakage check: [x] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Banyak pemula yang secara otomatis menerapkan algoritma Min-Max Scaling atau Z-score Normalization pada semua kolom dataset di Python/SPSS hanya karena mengikuti kebiasaan atau tutorial, tanpa melihat konteks variabelnya.

Risiko dari over-preprocessing ini, terutama pada riset UI/UX, adalah hilangnya makna kontekstual dari data. Jika nilai SUS sebesar "40" (yang secara universal berarti aplikasi tersebut sangat buruk/Not Acceptable)  dinormalisasi paksa menggunakan Z-score di dalam kelompok data yang semuanya bernilai rendah, angka tersebut bisa saja terdistorsi terlihat normal atau di tengah-tengah rentang. Distorsi ini akan menipu peneliti dsn menghasilkan kesimpulan akhir yang salah fatal terhadap usability aplikasi yang diuji. Karena itu, prinsip Minimal Distortion sangat penting dijaga.

