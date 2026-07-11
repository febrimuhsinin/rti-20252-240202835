# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Human-Computer Interaction (HCI) / Interaksi Manusia dan Komputer.
  Konteks  : Evaluasi pengalaman pengguna (User Experience) pada aplikasi mobile commerce.

System Context
  Input       : Interaksi navigasi pengguna, input data pencarian, dan pemilihan produk.
  Process     : Rendering antarmuka, pemrosesan filter, alur penggunaan fitur (task flow).
  Output      : Penyelesaian tugas (misal: sukses checkout atau klaim voucher).
  Outcome     : Tingkat kepuasan pengguna dan persepsi kemudahan penggunaan.
  Constraints : Keterbatasan layar perangkat mobile, kecepatan koneksi internet, dan beban kognitif pengguna.
  Stakeholders: Pengguna akhir (Gen Z), Tim UI/UX Shopee, dan Pengembang Aplikasi.
Fenomena → Problem
  Fenomena yang diamati             : Shopee merupakan aplikasi dengan fitur yang sangat padat (super app), namun sering terjadi inkonsistensi pengalaman antar fiturnya.
  Gejala (symptom) yang terukur     : Adanya fluktuasi skor SUS (antara 67 hingga 90) pada berbagai studi literatur terkait fitur yang berbeda.
  Masalah yang didiagnosis          : Struktur informasi yang terlalu kompleks (information overload) menyebabkan penurunan learnability pada fitur spesifik seperti Shopee Food atau manajemen voucher.
  Masalah riset (researchable)      : Belum adanya analisis komparatif yang mengukur secara spesifik disparitas usability antara alur transaksi utama dan alur fitur tambahan pada satu kelompok subjek yang sama.
  Variabel yang terukur             : Skor SUS (System Usability Scale).

Problem Quality Check
  [X] Clarity — Masalah berfokus pada perbandingan usability fitur.
  [X] Measurability — Masalah berfokus pada perbandingan usability fitur.
  [X] Relevance — Penting untuk optimalisasi retensi pengguna e-commerce.
  [X] Testability — Hipotesis dapat diuji melalui pengujian langsung ke pengguna.
  [X] Impact — Memberikan rekomendasi desain spesifik untuk fitur yang memiliki skor rendah.

Problem Statement (1 paragraf):
  Meskipun Shopee memiliki dominasi pasar yang kuat, kompleksitas antarmuka dan kepadatan fitur sering kali menimbulkan beban kognitif yang mengakibatkan inkonsistensi pengalaman pengguna. Gejala ini terlihat dari adanya disparitas skor usability (SUS) antara alur belanja reguler dan fitur tambahan seperti Shopee Food, di mana hambatan navigasi pada fitur spesifik dapat menurunkan efisiensi transaksi. Oleh karena itu, diperlukan penelitian untuk menganalisis perbandingan tingkat usability antar fitur tersebut guna mengidentifikasi akar masalah pada struktur desain yang menghambat kenyamanan berinteraksi bagi pengguna Generasi Z.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Evaluasi Komparatif Usability pada Super-app E-Commerce (Shopee Reguler vs Shopee Food)

| Tahap | Hasil |
|-------|-------|
| Reality | *Aplikasi e-commerce saat ini berkembang menjadi super-app dengan banyak fitur tambahan.* |
| Observed Issue (Symptom) | *Pengguna sering melaporkan kesulitan saat mencari menu spesifik atau menggunakan voucher promo yang bertumpuk.* |
| Diagnosed Problem (Root Cause) | *Hirarki visual yang tidak jelas dan terlalu banyak interupsi (pop-up) yang mengganggu alur tugas utama.* |
| Researchable Problem | *Sejauh mana pengaruh elemen dark patterns dan kepadatan informasi terhadap skor SUS pada alur transaksi kritis?* |
| Measurable Variable | *Skor SUS, Time on Task, dan Error Rate.* |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> 

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | *Navigasi menu, pencarian produk, dan input kode voucher oleh pengguna.* |
| Process | *Alur dari keranjang belanja hingga halaman pembayaran (checkout flow).* |
| Output | *Status penyelesaian transaksi atau keberhasilan aplikasi voucher.* |
| Outcome | *Skor kepuasan pengguna yang diukur melalui kuesioner SUS.* |
| Constraints | *Aturan promosi yang kompleks dan desain pop-up iklan yang menutupi konten utama.* |
| Stakeholders | *Pengguna Gen Z yang memiliki ekspektasi kecepatan navigasi yang tinggi.*|

**Komponen mana yang paling relevan dengan masalah riset?** Proses, (karena usability berfokus pada bagaimana alur/proses dijalankan oleh pengguna).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | *5* | *Fokus pada perbandingan fitur utama vs fitur tambahan sudah sangat jelas.* |
| Measurability | *5* | *Fokus pada perbandingan fitur utama vs fitur tambahan sudah sangat jelas.* |
| Relevance | *5* | *Sangat relevan bagi pengembang aplikasi e-commerce besar.* |
| Testability | *5* | *Eksperimen sangat mungkin dilakukan dengan responden yang tersedia.* |
| Impact | *4* | *Hasilnya bisa menjadi masukan konkret bagi tim UI/UX.* |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Penelitian ini dilatarbelakangi oleh fenomena inkonsistensi usability pada aplikasi Shopee yang disebabkan oleh kepadatan informasi dan fitur yang berlebihan. Meskipun aplikasi secara umum dianggap fungsional, terdapat indikasi penurunan efisiensi pada alur transaksi spesifik dibandingkan dengan alur belanja utama, yang ditandai dengan keluhan pengguna mengenai kompleksitas klaim voucher dan navigasi. Penelitian ini bertujuan untuk mengukur secara komparatif tingkat usability menggunakan metode SUS guna membuktikan adanya hambatan desain pada fitur-fitur tertentu yang berpotensi menurunkan pengalaman pengguna secara keseluruhan.
> ___________________________________________________

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamental antara masalah coding dan masalah riset terletak pada tujuannya. Dalam coding, masalah (bug/error) didefinisikan sebagai kegagalan sistem untuk menjalankan fungsi tertentu, dan pendekatannya adalah mencari solusi teknis agar sistem kembali berjalan (how to fix).

> Dalam riset, masalah didefinisikan sebagai celah pengetahuan (knowledge gap). Pendekatannya bukan sekadar memperbaiki "error", tetapi memahami mengapa fenomena itu terjadi dan membuktikannya secara empiris (why it happens & prove it). Jika coding berakhir pada sistem yang berfungsi, riset berakhir pada bukti atau generalisasi yang dapat dipertanggungjawabkan secara ilmiah.
