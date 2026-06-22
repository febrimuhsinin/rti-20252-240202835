# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [ ] Problem → Gap: masalah terdokumentasi di literatur
  [ ] Gap → RQ: pertanyaan menjawab gap spesifik
  [ ] RQ → Hypothesis: hipotesis memprediksi jawaban
  [ ] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [ ] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [ ] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [x] Istilah sama di semua bagian
  [x] Variabel di RQ = variabel di hipotesis = metrik di desain
  [x] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [x] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [x] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [x] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [x] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [x] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        |      |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   |      |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail |      |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | *Pengguna Generasi Z rentan mengalami information overload dan kelelahan kognitif akibat kompleksitas antarmuka dan interupsi elemen manipulatif (dark patterns) pada sub-fitur tambahan seperti Shopee Food.* |
| Gap | WS-03 | *Berbagai studi terdahulu mengevaluasi e-commerce dengan asumsi homogenitas secara utuh (Shopee dinilai secara umum), sehingga luput mengukur degradasi kebergunaan aktual antar-fitur di dalam aplikasi yang sama.* |
| RQ | WS-04 | *Apakah terdapat perbedaan skor System Usability Scale (SUS) yang signifikan antara alur transaksi belanja reguler dengan alur transaksi pada sub-fitur Shopee Food bagi pengguna Generasi Z?* |
| Hipotesis | WS-04 | *H₁: Alur transaksi Shopee Food akan menghasilkan rata-rata skor SUS yang secara signifikan lebih rendah dibandingkan alur belanja reguler (Kondisi Baseline).* |
| Variabel & Metrik | WS-05 | *IV = Jenis alur transaksi (Belanja Reguler vs. Shopee Food); DV = Tingkat kebergunaan subjektif; Metrik = Skor global System Usability Scale rentang 0–100.* |
| Sistem | WS-06 | *Instrumen pengujian elektronik (Google Form) yang memuat screening kelayakan (CV), instruksi skenario tugas mandiri, dan matriks penghitung otomatis kuesioner SUS.* |
| Desain Eksperimen | WS-07 | *Eksperimen komparatif kuantitatif Unmoderated Remote Testing dengan within-subjects design (N=30 Gen Z), menggunakan teknik counterbalancing (Form A & B), dan dianalisis menggunakan Paired Sample T-Test.* |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | *✅* | *Masalah information overload dan dark patterns ditarik menjadi gap karena literatur terdahulu mengabaikan hidden friction pada sub-fitur.* |
| Gap → RQ | *✅* | *RQ secara langsung menjembatani gap tersebut dengan cara membandingkan skor SUS dari aplikasi induk reguler melawan sub-fiturnya.* |
| RQ → Hypothesis | *✅* | *H₁ memprediksi jawaban secara terarah (directional), yakni skor SUS pada alur Shopee Food diprediksi menurun.* |
| Hypothesis → Metric | *✅* | *"Penurunan kebergunaan" dikuantifikasi secara mutlak dengan metrik selisih skor SUS berskala interval 0-100.* |
| Metric → System | *✅* | *Metrik (Skor SUS) diukur secara terintegrasi oleh komponen matriks Likert 5-poin yang ada di dalam Google Form.* |
| System → Experiment | *✅* | *Google Form bertindak sebagai experimental artifact yang mengatur alur within-subjects dan teknik counterbalancing secara remote.* |

**Koneksi mana yang paling lemah?** System → Experiment
Bagaimana cara memperkuatnya?
**Bagaimana cara memperkuatnya?**
> Karena menggunakan metode remote testing via Google Form, kontrol terhadap lingkungan fisik dan gawai responden melemah. Hal ini diperkuat dengan menambahkan Screening Questions wajib di awal form untuk memastikan koneksi internet stabil dan lingkungan kondusif (self-reported control).

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [x] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? Semua terminologi dikunci secara konsisten dari Bab 1 hingga 3: "Alur Belanja Reguler", "Shopee Food", "Generasi Z", dan "System Usability Scale (SUS)".

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | *3* | *Seluruh 6 koneksi vertikal terhubung jelas. Argumen mengalir mulus dari fenomena dark patterns (Problem) menuju pengujian komparatif selisih SUS (Metode).* |
| Specificity | *3* | *Semua variabel memiliki angka yang terdefinisi: SUS skala 0-100, sampel minimal N=30, Skala Likert 5 poin, Signifikansi (Alpha) 0.05.* |
| Feasibility | *3* | *Desain Unmoderated Remote Testing via Google Form sangat realistis diselesaikan dalam estimasi timeline 8 minggu operasional.* |
| Rigor | *3* | *Baseline yang digunakan sangat kuat dan setara, yaitu alur belanja utama/reguler dari aplikasi Shopee itu sendiri (bukan membandingkan dengan aplikasi kompetitor yang berbeda UI-nya).* |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? Proposal sudah siap 100%. Langkah selanjutnya adalah membuat instrumen Google Form secara aktual (Form A dan Form B) dan mulai merekrut partisipan sesuai kriteria screening.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Mengidentifikasi instrumen pengukuran (menentukan SUS) dsn populasi responden (Generasi Z) karena keduanya sangat konkrit, banyak referensi ilmiahnya, dsn relevan dengan keseharian pengguna digital saat ini.
**Bagian tersulit:** Menuliskan rumusan Gap penelitian serta merancang Desain Eksperimen (Matrix 2), khususnya memastikan cara menekan confounding variables (prior exposure effect & order bias) agar hasil beda selisih kuantitatif nanti benar-benar valid, bukan karena kelelahan atau kebetulan.
**Yang akan dilakukan berbeda:**
> Jika mengulang dari awal, saya akan lebih dulu membedah taksonomi UI dark patterns pada banyak aplikasi secara berdampingan untuk memperkaya kajian literatur (State of the Art), sebelum akhirnya mengerucut memilih satu objek aplikasi yang paling observable untuk dilakukan eksperimen.
> ___________________________________________________
