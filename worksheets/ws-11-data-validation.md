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
  [x] Semua skenario tercakup (Satu Form Kombinasi Shopee Reguler & Food)
  [x] Jumlah run sesuai rencana (Total N=36 partisipan)
  [x] Tidak ada file output hilang (Terekam lengkap dalam `data form.csv`)
  Missing: 0 dari 36 data points (semua responden mengisi dengan lengkap)

Format Consistency:
  [x] Semua file format sama (Tersimpan sebagai CSV)
  [x] Header konsisten (Timestamp, Usia, Pekerjaan, 20 Item SUS)
  [x] Tipe data konsisten (Skor 1-5 berupa numerik)

Range & Logic:
  [x] Nilai dalam range masuk akal (Skala Likert 1-5 valid)
  [x] Tidak ada waktu negatif (Timestamp logis)
  [x] Semua parameter demografi sesuai (Usia 18-25 tahun, punya aplikasi)
  Anomali ditemukan: Tidak terdeteksi anomali (Tidak ada missing value atau straight-lining ekstrem).

Keputusan:
  [x] Data siap di-preprocessing
  [ ] Perlu cleaning
  [ ] Perlu re-run
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul (Berdasarkan rancangan Counterbalancing).

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| *Evaluasi Shopee Reguler & Food* | *36* | *36* | *0* | *Seluruh responden mensubmit data secara lengkap (100%).* |


**Total expected:** 36 partisipan | **Total actual:** 36 partisipan | **Missing:** 0 partisipan.

**Keputusan untuk data missing:**
> Tidak ada data yang hilang (missing values). Semua 36 partisipan berhasil merekam data secara penuh, sehingga data siap digunakan seluruhnya (N=36) untuk tahap berikutnya.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Berdasarkan hasil tinjauan *raw data* di file `data form.csv`:

**Deteksi Anomali:**
1. **Screening Criteria:** Semua responden terdeteksi memilih "18 - 25 tahun" dan "Ya" untuk kepemilikan aplikasi Shopee. (Tidak ada anomali demografi).
2. **Kelengkapan (Missing Values):** Setiap dari 36 baris memiliki 20 jawaban numerik lengkap (1-5) untuk pertanyaan SUS Reguler dan Food. Tidak ada cell kosong.
3. **Pola Ekstrem (Straight-lining):** Berdasarkan pengamatan visual singkat, tidak ditemukan responden yang hanya menekan tombol '5' terus-menerus di seluruh 20 pertanyaan tanpa memperhatikan polaritas soal positif/negatif.

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| *None*  | *N/A* | *N/A*               | *Dataset (36 baris) valid sepenuhnya dan tidak memerlukan penghapusan baris.* |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul (36 dari 36 responden terekam dengan lengkap).
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: Format output dari Google Form konsisten sebagai CSV (`data form.csv`). Nilai skala 1-5 terekam sebagai teks yang memuat angka dan siap diproses.
**3. Range check (anomali):** Seluruh isian matriks kuesioner berada pada rentang nilai (1-5).
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: Tidak ada pelanggaran parameter (seluruhnya Gen Z 18-25 tahun dan memiliki aplikasi Shopee).

**Kesimpulan:** [x] Data siap masuk ke tahap preprocessing / [ ] Perlu tindakan

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> "Data yang benar" (Correct Data) adalah data yang secara format komputer berhasil terekam tanpa error, misalnya Google Form sukses menyimpan 36 baris respons dalam file CSV tanpa ada bug atau data yang corrupt.

Sebaliknya, "Data yang dipercaya" (Trusted Data) adalah data yang benar-benar merepresentasikan realitas psikologis dan perilaku asli responden sesuai batasan desain eksperimen. Misalnya, sistem mencatat skor SUS sebesar 20 (data "benar" karena berada dalam rentang 0-100), tetapi setelah divalidasi, ternyata responden mengisi form dalam 30 detik secara asal-asalan (speeding). Data ini tidak bisa "dipercaya" karena merusak validitas penelitian.

Proses validasi formal sangat diperlukan karena pengumpulan otomatis (seperti Google Form) tidak memiliki insting analitis manusia untuk mendeteksi human error, responden yang malas membaca (bias), atau anomali kontekstual. Tanpa validasi, garbage in (data sampah yang masuk) akan menghasilkan garbage out (kesimpulan statistik yang menyesatkan).
> ___________________________________________________
