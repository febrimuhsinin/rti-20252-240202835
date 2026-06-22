# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : AMD Ryzen 5 
  RAM     : 8 GB
  GPU     : Tidak relevan (CPU-only)
  Storage : 256 GB SSD

Software:
  OS        : Windows 11
  Runtime   : Web Browser (Chrome/Firefox) & Google Workspace
  Framework : IBM SPSS Statistics (Untuk Paired Sample T-Test / Wilcoxon)

Dependencies:
| Library / Alat Uji | Version / Tipe      | Sumber           | Fungsi Utama                                |
|--------------------|---------------------|------------------|---------------------------------------------|
| Aplikasi Shopee    | v3.25.x (Contoh)    | Google PlayStore | Objek eksperimen (harus dikunci versinya)   |
| Google Forms       | 2026 Release        | Google Workspace | Platform instrumen skenario & kuesioner SUS |
| IBM SPSS           | Versi 26.0 / JASP   | IBM              | Pengujian normalitas & uji beda statistik   |
| Microsoft Excel    | Office 365          | Microsoft        | Tabulasi skor mentah Likert & formula SUS   |

Konfigurasi:
  Config file     : Template Kuesioner (Form A: Reguler->Food | Form B: Food->Reguler)
  Random seed     : Counterbalancing logic (Distribusi link Form A & B secara berselang-seling)
  Hyperparameters : Batas inklusi responden = Gen Z (18-25 tahun), Mahasiswa, N=30.

Reproducibility Check:
  [x] Dependency terdokumentasi (Versi aplikasi Shopee dicatat sebelum pengujian)
  [x] Seed ditetapkan di semua level (Aturan Counterbalancing terdokumentasi)
  [x] Config di version control (Backup struktur Form di Word/PDF)
  [x] README instruksi reproduksi lengkap (Panduan dari sebar link hingga uji SPSS)
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | *AMD Ryzen 5 * |
| RAM | *8 GB RAM* |
| GPU | *CPU-only (Tidak memerlukan komputasi grafis)* |
| OS | *Windows 11* |
| Runtime | *Windows 11* |
| Framework | *IBM SPSS Statistics 26 & MS Excel* |
| Random Seed | *Distribusi Counterbalancing (Alternasi manual Link A & Link B ke tiap responden)* |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| *Aplikasi Shopee* | *Locked Version (Misal: 3.25.x)* | *Objek utama eksperimen; jika aplikasi update di tengah masa pengumpulan data, tata letak antarmuka bisa berubah dan mengancam validitas eksperimen.*                 |
| *Google Forms*    | *Current Web Version*            | *Platform utama untuk eksekusi skenario (Task Scenario), kontrol screening responden, dan pengumpulan skor instrumen SUS.*                                                |
| *IBM SPSS*        | *v26.0*                          | *Software pengolah statistik untuk menjalankan uji asumsi normalitas (Shapiro-Wilk) dan uji beda hipotesis (Paired Sample T-Test / Wilcoxon).*                     |
| *Microsoft Excel* | *Office 365*                     | *Digunakan untuk tabulasi data mentah (raw data) Likert dan melakukan kalkulasi formula konversi skor SUS secara matematis.*                                         |
| *Figma / Miro*    | *Current Web Version*            | *Tools desain yang digunakan untuk memvisualisasikan luaran penelitian, yaitu merancang User Journey Map (peta titik hambatan) dan prototipe Ethical UI Guidelines.* |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Algoritma/Tahap | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | *Konversi SUS di Excel*    | *Skor 0-100 per user*     | [x] Ya / [ ] Tidak | 
| 2 | *Uji Shapiro-Wilk di SPSS* | *P-Value Normalitas*      | [x] Ya / [ ] Tidak |
| 3 |  *Paired T-Test di SPSS*   | *T-Value & P-Value Akhir* | [x] Ya / [ ] Tidak |


**Jika hasil berbeda, kemungkinan penyebab:**

> Penyebab umum non-repeatability:
> - **Thermal throttling** — CPU/GPU overheating pada run berturut-turut → clock speed turun → waktu eksekusi berubah
> - **Background process** — antivirus scan, update OS, atau cloud sync aktif saat run berlangsung
> - **Cache dari run sebelumnya** — hasil tersimpan di memori/disk sehingga run berikutnya tidak menjalankan komputasi penuh
> - **Random state tidak dikontrol di semua level** — Python seed di-set, tapi NumPy/PyTorch/TensorFlow punya seed independen

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [x]  Formula perhitungan SUS di-set dan di-lock secara matematis di template Excel.
- [x]  Tidak ada background process yang mengganggu (Skenario eksperimen Google Form tidak diubah di tengah jalan).
- [x]  Dataset mentah (Raw CSV) di-backup (Read-only) sebelum dibersihkan.
- [x]  Langkah klik di SPSS dicatat secara berurutan.

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Evaluasi Komparatif Usability & Dark Patterns Shopee

## 1. Environment
> Instrumen: Google Forms (Form A & Form B untuk Counterbalancing).
> Objek: Aplikasi Shopee Versi [Tulis versi saat eksperimen berjalan].
> Analisis: MS Excel & IBM SPSS 26.

## 2. Installation
> 1. Buat Form A (Skenario Reguler -> SUS 1 -> Skenario Food -> SUS 2).
> 2. Duplikasi menjadi Form B (Skenario Food -> SUS 1 -> Skenario Reguler -> SUS 2).
> 3. Tentukan 30 partisipan mahasiswa Gen Z.

## 3. Data
> Sumber: Respons Google Sheets yang diekspor menjadi CSV.
> Format: 30 baris (Responden), Kolom Skor SUS Sesi 1 dan Skor SUS Sesi 2.
> Preprocessing: Data kualitatif disaring, data Likert dikonversi dengan rumus baku SUS (*2.5).

## 4. Execution
> 1. Sebar Link Form A ke 15 orang, Form B ke 15 orang.
> 2. Unduh CSV, gabungkan tabulasi Sesi Reguler dan Sesi Food.
> 3. Impor CSV ke SPSS -> Analyze -> Descriptive Statistics -> Explore (Shapiro-Wilk).
> 4. Analyze -> Compare Means -> Paired-Samples T Test.

## 5. Configuration
> Tingkat signifikansi (Alpha): 0.05
> Aturan Konversi SUS: P.Ganjil (X-1), P.Genap (5-Y), Total * 2.5.

## 6. Expected Output
> Hipotesis 1 terbukti: Rata-rata Skor SUS Shopee Food < Skor SUS Belanja Reguler secara signifikan (p-value < 0.05). Ditemukan identifikasi titik hambatan terkait dark patterns.
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [x] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> 1.  File draf pertanyaan instrumen kuesioner Google Form yang final (belum dibuat tautan/URL aktualnya).

> 2. Format pencatatan versi aktual aplikasi Shopee yang akan digunakan saat pengujian berlangsung (karena aplikasi rill terus update).

> 3. Catatan langkah-langkah (syntax) di SPSS secara mendetail agar peneliti lain yang tidak paham statistik tetap bisa mengikuti alur analisis data yang saya lakukan.
