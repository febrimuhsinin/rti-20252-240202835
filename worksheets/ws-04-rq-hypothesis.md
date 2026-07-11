# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Adanya disparitas signifikan antara skor usability aplikasi utama (SOTA: 90.06) dengan fitur spesifik seperti Shopee Food/Voucher (Skor: 70) yang mengindikasikan adanya hambatan pada alur transaksi kritis.

Research Question:
  Tipe         : [x] Comparison [ ] Improvement [ ] Exploratory
  Formulasi    : Apakah terdapat perbedaan skor System Usability Scale (SUS) yang signifikan antara alur transaksi belanja umum dengan alur transaksi pada fitur Shopee Food bagi pengguna Generasi Z?
  Variabel IV  : Jenis alur transaksi (Belanja Umum vs Shopee Food).
  Variabel DV  : Skor Usability (SUS Score).
  Metrik       : Skor SUS (skala 0–100).
  Dataset      : Data primer dari 36+ responden (pengguna aktif Shopee).
  Baseline     : Skor SUS rata-rata aplikasi Shopee secara general (Lim et al., 2025).

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (survei & pengujian langsung)

Contribution Statement:
  Apa yang baru diketahui : Perbandingan empiris efisiensi antarmuka antara aplikasi induk dan sub-fitur yang sering dianggap membingungkan (information overload).
  Jenis kontribusi        : [ ] Improvement [x] Comparison [ ] Novel approach
  Gap yang diisi          : Menjelaskan penyebab penurunan skor usability pada alur transaksi spesifik (Voucher/Metode Pembayaran).

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan skor SUS antara alur transaksi belanja umum dan alur transaksi Shopee Food.
  H₁ : Skor SUS pada alur transaksi Shopee Food secara signifikan lebih rendah dibandingkan alur belanja umum (Selisih > 10 poin).
  Threshold              : alpha = 0.05 (Tingkat signifikansi statistik).
  Justifikasi threshold  : Standar umum dalam penelitian ilmu komputer dan psikologi untuk menolak hipotesis nol.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Ketidakkonsistenan performa usability pada alur transaksi kritis (pembayaran/voucher) dibandingkan navigasi belanja umum yang menyebabkan kebingungan pengguna (user lost).

**RQ versi pertama (tulis bebas):**
> Bagaimana perbandingan usability antara beli barang biasa di Shopee dengan beli makanan di Shopee Food?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | *ya* | *Perbandingan menggunakan metode SUS* |
| Metrik terukur | *ya* | *Skor SUS (0-100)* |
| Baseline | *ya* | *Alur Belanja Umum sebagai pembanding* |
| Dataset/konteks | *ya* | *Pengguna aktif Shopee (Gen Z)* |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> "Sejauh mana perbedaan tingkat usability (menggunakan metrik SUS) pada alur transaksi Shopee Food dibandingkan dengan alur transaksi belanja reguler pada aplikasi Shopee?"

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | *Tidak terdapat perbedaan rata-rata skor SUS yang signifikan antara alur transaksi belanja reguler dan alur transaksi Shopee Food.* |
| H₁ | *Alur transaksi Shopee Food memiliki rata-rata skor SUS yang secara signifikan lebih rendah dibandingkan alur transaksi belanja reguler.* |
| Metrik | *Mean SUS Score.* |
| Threshold | *Skor 68 (Average Acceptability).* |
| Justifikasi threshold | *Skor 68 adalah median score global untuk instrumen SUS; skor di bawah ini dianggap memerlukan perbaikan serius.* |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika hasil uji statistik (T-Test) menunjukkan nilai p > 0.05 atau jika skor SUS Shopee Food ternyata sama atau lebih tinggi dari belanja reguler.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | *Apakah alur transaksi Shopee Food menghasilkan skor SUS lebih rendah dari alur reguler?* |
| Variable (IV) | *Contoh: Jenis algoritma (CNN vs RF)* |
| Variable (DV) | *Fitur Aplikasi (Reguler vs Food).* |
| Metric | *Tingkat Usability (Skor SUS).* |
| Data source | *Pengujian langsung (UT) dan Kuesioner pasca-tugas (Post-task).* |
| Analysis method | *Paired Sample T-Test (Uji beda rata-rata).* |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Evaluation of Shopee Food Usability Using Usability Testing Methods and System Usability Scale (Sagala & Pakaja, 2024).
**RQ yang diekstrak:** "Bagaimana tingkat usability aplikasi Shopee Food berdasarkan metode SUS dan Usability Testing?"
**Komponen yang hilang:** Penelitian tersebut hanya mengukur satu sisi (Shopee Food) tanpa membandingkannya dengan standar aplikasi induk atau kompetitor secara langsung dalam satu eksperimen terkontrol. Hal ini membuat angka "70" tidak memiliki konteks apakah itu sudah cukup baik untuk standar Shopee atau justru sebuah penurunan performa.
