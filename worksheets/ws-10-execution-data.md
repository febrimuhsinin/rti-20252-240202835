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

| Responden | Skenario (Urutan) | Alat Uji | Parameter (Kriteria) | Status | Output File |
|-----------|-------------------|----------|----------------------|--------|-------------|
| R-01 s.d R-15 | Form A (Reguler -> Food) | Google Form A | Gen Z, Mahasiswa, Exp >1 thn | Planned | form_A_raw.csv |
| R-19 s.d R-36 | Form B (Food -> Reguler) | Google Form B | Gen Z, Mahasiswa, Exp >1 thn | Planned | form_B_raw.csv |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : 15 partisipan
Total runs               : 36 partisipan

DATA LOG (per run):
  Run ID    : R-001 (Anonim)
  Timestamp : Waktu pengiriman (submit) form
  Skenario  : Tipe Form (A atau B)
  Input     : Profil Demografis & Kualifikasi Screening
  Output    : Skor SUS Sesi 1 (0-100) dan Skor SUS Sesi 2 (0-100)
  Anomali   : Catatan jika ada outlier (misal: isi jawaban nilai 5 semua)
  Catatan   : Kelayakan data untuk diuji ke SPSS
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # (Responden) | Skenario (Counterbalancing) | Seed (Tipe Form) | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| *R-001 s/d R-015* | *Rute 1: Belanja Reguler -> Shopee Food* | *Form A* | *Mahasiswa Gen Z (18-25 thn), Sinyal Stabil* | *Planned* |
| *R-019 s/d R-036* | *Rute 2: Shopee Food -> Belanja Reguler* | *Form B* | *Mahasiswa Gen Z (18-25 thn), Sinyal Stabil* | *Planned* |


**Total skenario:** 2 Rute (Form A & Form B)
**Run per skenario:** 15 Partisipan
**Total run keseluruhan:** 36 Partisipan

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
| Tipe Rute (Seed)      | *Form A (Reguler -> Food)* |
| Versi Aplikasi Shopee | *v3.25.1*                  |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| *Skor SUS Belanja Reguler* | *Integer / Float* | *0.0 – 100.0*       |
| *Skor SUS Shopee Food*     | *Integer / Float* | *0.0 – 100.0*       |
| *Waktu Pengisian Form*     | *Time / Duration* | *> 3 Menit (Wajar)* |

**Format output:** [x] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

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
