# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [x] Semua skenario tercakup (Rute Form A dan Form B sudah terdistribusi)
  [x] Jumlah run sesuai rencana (Total N=30 partisipan yang valid)
  [x] Tidak ada file output hilang (Semua data masuk ke Google Sheets)
  Missing: 0 dari 30 data points (setelah dilakukan rekrutmen pengganti untuk data yang cacat)

Format Consistency:
  [x] Semua file format sama (Diekspor ke CSV dari Google Sheets)
  [x] Header konsisten (Timestamp, Usia, Skor SUS 1, Skor SUS 2)
  [x] Tipe data konsisten (Jawaban skala Likert 1-5 semuanya berupa angka numerik, bukan teks)

Range & Logic:
  [x] Nilai dalam range masuk akal (Jawaban Likert 1-5, Total Skor SUS absolut 0 - 100)
  [x] Tidak ada waktu negatif (Timestamp pengiriman berurutan logis)
  [x] Metrik 0–100%, tidak di luar range (Tidak ada skor SUS > 100 atau < 0)
  Anomali ditemukan: Terdeteksi 1 responden yang mengisi "Sangat Setuju (5)" untuk semua pernyataan positif dan negatif (Straight-lining).

Cross-Validation:
  [x] Run identik → hasil mendekati (Responden pada Form A dan Form B memiliki rata-rata demografi yang setara)
  [x] Trend konsisten dengan ekspektasi teori (Alur dengan Dark Patterns cenderung memiliki waktu pengerjaan lebih lama)

Keputusan:
  [x] Data siap analisis (Setelah outlier dibuang dan diganti)
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul (Berdasarkan rancangan Counterbalancing).

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| *CForm A (Reguler -> Food)* | *15* | *16* | *0* | *1 data dihapus karena responden ternyata berusia > 25 tahun (melanggar Variabel Kontrol)* |
| *Form B (Food -> Reguler)* | *15* | *14* | *1* | *1 partisipan tidak men-submit form sampai akhir (Dropout)* |


**Total expected:** 30 partisipan | **Total actual:** 30 partisipan | **Missing:** 1 partisipan di Form B.

**Keputusan untuk data missing:**
> Data responden Form A yang usianya >25 tahun didiskualifikasi karena melanggar batas demografi Gen Z (18-25 tahun). Untuk 1 data yang missing di Form B, peneliti akan menyebarkan kembali link Form B kepada 1 orang partisipan baru yang memenuhi syarat agar sampel seimbang (balance) kembali menjadi 15 vs 15 (Total N=30) untuk mematuhi asumsi Paired Sample T-Test.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali (Contoh menggunakan sampel data Skor SUS responden).

**Dataset sampel (Simulasi 5 Responden Form A - Skor SUS Sesi 1):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | *75.0* |
| 2 | *72.5* |
| 3 | *77.5* |
| 4 | *77.5* |
| 5 | *70.0* |

**Deteksi outlier:**
- Q1 = 70.0 | Q3 = 75.0 | IQR (Q3 - Q1) = 5.0
- Batas bawah (Q1 - 1.5×IQR) = 70.0 - 7.5 = 62.5
- Batas atas (Q3 + 1.5×IQR) = 75.0 + 7.5 = 82.5
- Outlier terdeteksi: Run 4 (Skor 20.0 berada jauh di bawah batas 62.5)

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| *Run 4* | *20.0* | *Speeding / Straight-lining: Responden mengisi kuesioner secara asal-asalan dalam waktu kurang dari 1 menit (hanya klik nilai "1" untuk semua pertanyaan tanpa membaca instruksi).* | *Diskualifikasi data responden ini (dihapus dari dataset) karena cacat reliabilitas, lalu rekrut responden pengganti.* |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul (30 dari 30 data valid telah diamankan setelah proses rekrutmen pengganti).
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: Semua kolom jawaban Likert 1-5 sudah berupa integer numerik di spreadsheet (Excel).
**3. Range check (anomali):** Skor akhir konversi SUS dipastikan berada absolut dalam rentang 0 hingga 100. Tidak ada nilai desimal yang cacat.
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: Semua 30 responden secara logis mencentang konfirmasi berstatus Mahasiswa, Gen Z (18-25 tahun), dan memiliki jaringan stabil (lolos Screening Variable Control).

**Kesimpulan:** [x] Data siap analisis (diimpor ke IBM SPSS untuk diuji Shapiro-Wilk dan T-Test) / [ ] Perlu tindakan: ____

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> "Data yang benar" (Correct Data) adalah data yang secara format komputer berhasil terekam tanpa error, misalnya Google Form sukses menyimpan 30 baris respons dalam file CSV tanpa ada bug atau data yang corrupt.

Sebaliknya, "Data yang dipercaya" (Trusted Data) adalah data yang benar-benar merepresentasikan realitas psikologis dan perilaku asli responden sesuai batasan desain eksperimen. Misalnya, sistem mencatat skor SUS sebesar 20 (data "benar" karena berada dalam rentang 0-100), tetapi setelah divalidasi, ternyata responden mengisi form dalam 30 detik secara asal-asalan (speeding). Data ini tidak bisa "dipercaya" karena merusak validitas penelitian.

Proses validasi formal sangat diperlukan karena pengumpulan otomatis (seperti Google Form) tidak memiliki insting analitis manusia untuk mendeteksi human error, responden yang malas membaca (bias), atau anomali kontekstual. Tanpa validasi, garbage in (data sampah yang masuk) akan menghasilkan garbage out (kesimpulan statistik yang menyesatkan).
> ___________________________________________________
