# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Responden | Skenario | Alat Uji | Parameter (Kriteria) | Status | Output File |
|-----------|----------|----------|----------------------|--------|-------------|
| R-01 s.d R-36 | Evaluasi Shopee Reguler & Food | Google Form | Gen Z (18-25), Punya Aplikasi Shopee | Selesai (Terkumpul) | data form.csv |

Total runs : 36 partisipan

DATA LOG (per run):
  Run ID    : R-001 s.d R-036 (diambil dari Nama)
  Timestamp : 3 Juli 2026 - 11 Juli 2026
  Input     : Profil Demografis (Usia, Status Pekerjaan) & Screening
  Output    : 10 Item Kuesioner SUS Reguler (1-5) & 10 Item Kuesioner SUS Food (1-5)
  Anomali   : (Akan dianalisis di tahap validasi data)
  Catatan   : Data sudah terkumpul dalam satu file `data form.csv`
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # (Responden) | Skenario | Tipe Form | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| *R-001 s/d R-036* | *Evaluasi Usability Reguler & Food* | *Google Form (Single/Combined)* | *Gen Z (18-25 thn), Punya Aplikasi* | *Selesai (Executed)* |


**Total skenario:** 1 Rute Kuesioner
**Total run keseluruhan:** 36 Partisipan terkumpul (sesuai data form.csv)

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID (Responden) | *R-001* |
| Timestamp          | *2026-06-25T10:30:00* |
| Kualifikasi Lolos  | *Ya / Tidak* |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Tipe Rute             | *Kuesioner Kombinasi Reguler & Food* |
| Platform Pengujian    | *Mobile (Aplikasi Shopee)* |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| *Skor SUS Belanja Reguler* | *Integer / Float* | *0.0 – 100.0*       |
| *Skor SUS Shopee Food*     | *Integer / Float* | *0.0 – 100.0*       |
| *Waktu Pengisian Form*     | *Time / Duration* | *> 3 Menit (Wajar)* |

**Format output:** [x] CSV (`data form.csv`) / [ ] JSON / [ ] Database

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (Dropout)             | *Partisipan keluar di tengah jalan dan tidak men-submit kuesioner Sesi 2.* | *Abaikan data yang tidak lengkap, rekrut partisipan pengganti agar total N tetap 36.* |
| Hasil ekstrem (Straight-lining) | *Partisipan menjawab nilai "5" untuk SEMUA pernyataan SUS (padahal SUS punya pertanyaan negatif yang seharusnya dibalik nilainya).* | *Karantina/Hapus data tersebut dari dataset analisis (Outlier Removal), dokumentasikan sebagai data cacat/bias, rekrut pengganti.* |
| Waktu eksekusi anomali | *Durasi pengerjaan form sangat cepat (misal: di bawah 1 menit).* | *Investigasi kepalidan data. Jika terbukti mengisi secara asal (speeding), diskualifikasi responden tersebut.* |
| Inkonsistensi dengan run lain | *Di tengah form, partisipan menuliskan umur 28 tahun.* | *Diskualifikasi otomatis karena melanggar variabel kontrol (Gen Z usia 18-25 tahun).* |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Sebelumnya, evaluasi antarmuka seringkali hanya ditanyakan kepada 2 atau 3 orang teman secara kasual tanpa instrumen terstandar. Risikonya, simpulan yang ditarik sangat bias, tidak mewakili populasi, dan tidak bisa diuji signifikansinya secara statistik. Jika 1 teman bilang aplikasinya "jelek", kita langsung menganggap aplikasinya gagal, padahal itu murni opini subjektif satu individu.
**Yang akan dilakukan berbeda:**
> Dengan menerapkan multiple runs yang melibatkan 36 partisipan dan menggunakan teknik counterbalancing secara ketat, kepercayaan terhadap hasil riset menjadi jauh lebih kuat. Data 36 responden akan membentuk distribusi normal yang memungkinkan dilakukannya Uji Paired Sample T-Test. Dengan demikian, klaim bahwa kompleksitas fitur tambahan (seperti Shopee Food) menurunkan usability tidak lagi bersandar pada opini, melainkan pada pembuktian saintifik (P-Value) yang tidak bisa dibantah.
