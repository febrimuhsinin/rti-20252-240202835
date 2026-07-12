# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah terdapat perbedaan skor System Usability Scale (SUS) yang signifikan antara alur transaksi belanja umum dengan alur transaksi pada fitur Shopee Food bagi pengguna Generasi Z?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|    Fitur Aplikasi   | IV   | Alur navigasi sistem              | Jenis Fitur (Reguler vs Food) | Nominal  |      —       |          Kategorisasi tugas eksperimen | Untuk membandingkan dua kondisi sistem yang berbeda.                            |
|      Usability      | DV   | Persepsi kemudahan & efisiensi    | Total SUS Score               | Interval | Skor (0-100) |          Kuesioner SUS (10 instrumen)  | Instrumen standar industri yang reliabel untuk mengukur usability.              |
| Pengalaman Pengguna | CV   | Familiaritas teknologi            | Durasi penggunaan aplikasi    | Ordinal  | Bulan/ Tahun |          Profiling data responden      | Memastikan perbedaan skor bukan karena responden baru belajar memakai aplikasi. |

Alignment Check:
  RQ (Perbedaan usability) → Concept (Kemudahan) → Variable (SUS Score) → Metric (Kuesioner) → Data (Likert) → Result (T-Test)
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah alur transaksi Shopee Food menghasilkan skor SUS yang lebih rendah dibandingkan alur belanja reguler pada pengguna Gen Z?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| *Jenis Layanan* | *IV* | *Alur Navigasi (Feature Bloat)* | *Categorical: Shopee Reguler vs Shopee Food* | *Nominal* | *—* |
| *Kemudahan Penggunaan* | *DV* | *Usability* | *Skor Akhir SUS* | *Interval* | *Poin (0-100)* |
| *Perangkat* | *CV* | *Lingkungan pengujian* | *Model Smartphone & OS* | *Nominal* | *—* |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? Justifikasi: Konsep usability dioperasionalisasikan secara langsung melalui instrumen SUS yang memang divalidasi untuk mengukur konsep tersebut.

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV (SUS Score) menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| *Representative* | *5* | *SUS mencakup efektivitas, efisiensi, dan kepuasan secara global.* |
| *Sensitive* | *4* | *Skala Likert 5 poin cukup sensitif menangkap perbedaan persepsi halus antar alur.* |
| *Feasible* | *5* | *Sangat mudah dikumpulkan melalui kuesioner digital pasca-eksperimen.* |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Time on Task (Ratio). Skor SUS bersifat subjektif; metrik waktu memberikan bukti objektif apakah kebingungan user (seperti pada alur voucher) benar-benar memperlambat proses.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika semua responden adalah pakar (power user) Shopee, skor SUS mungkin akan menumpuk di angka 90-100 untuk kedua fitur, sehingga perbedaan kesulitan antar alur tidak terlihat lagi.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| *Completeness* | *Apakah semua data point terkumpul?* | *ya* | *Menetapkan semua pertanyaan kuesioner sebagai "required".* |
| *Consistency* | *Apakah ada kontradiksi internal?* | *mungkin* | *Menggunakan teknik pembersihan data untuk jawaban yang pola "zigzag" (tidak serius).* |
| *Validity* | *Apakah benar-benar mengukur yang dimaksud?* | *ya* | *Menggunakan instrumen SUS asli (John Brooke) yang sudah baku.* |
| *Representativeness* | *Apakah sampel mewakili populasi target?* | *ya* | *Melakukan screening hanya pada mahasiswa/Gen Z pengguna aktif.* |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dianggap p-hacking karena peneliti cenderung "mencari-cari" metrik yang hanya menunjukkan hasil signifikan (nilai p < 0.05) untuk mendukung hipotesis mereka, sambil mengabaikan metrik lain yang tidak signifikan. Ini adalah bentuk manipulasi ilmiah yang merusak objektivitas.

Perbedaannya dengan eksplorasi data yang sah:

Eksplorasi Sah: Peneliti menganalisis data secara luas untuk menemukan pola baru atau tren menarik tanpa mengklaimnya sebagai pembuktian hipotesis awal. Temuan ini biasanya dilaporkan sebagai insight tambahan untuk riset masa depan.

p-hacking: Peneliti berpura-pura bahwa metrik yang "beruntung" signifikan tersebut adalah metrik utama yang sudah direncanakan sejak awal untuk memvalidasi hipotesis mereka (confirmatory research).

Apakah data metrik ini sudah sesuai dengan rencana metodologi penelitianmu, atau kamu ingin menambahkan metrik performa teknis seperti error rate?
