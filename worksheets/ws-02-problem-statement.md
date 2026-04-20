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
  Domain   : Optimasi Logistik dan Transportasi
  Konteks  : Penentuan rute distribusi barang pada PT. Pos Indonesia Cabang Lamongan menuju 12 drop point kecamatan

System Context
  Input       : 19 titik lokasi kantor pos dan jarak antar titik (dalam satuan kilometer).
  Process     : Iterasi Algoritma Genetika (populasi awal, evaluasi fitness, seleksi roulette wheel, crossover, mutasi)
  Output      : Urutan rute terpendek yang harus dilalui kurir.
  Outcome     : Meminimalkan waktu tempuh dan meminimalkan biaya bahan bakar kendaraan operasional.
  Constraints : Kurir harus mengunjungi setiap kantor tepat satu kali dan kembali ke lokasi awal keberangkatan.
  Stakeholders: PT. Pos Indonesia Cabang Lamongan, Kurir ekspedisi, Pelanggan layanan PosAja.

Fenomena → Problem
  Fenomena yang diamati             : Perusahaan logistik dihadapkan pada banyaknya rute pengiriman yang harus dilalui ke berbagai kecamatan.
  Gejala (symptom) yang terukur     : Proses distribusi berisiko dilakukan hanya berdasarkan insting petugas pos, sehingga jarak tempuh dan biaya perjalanan tidak minimum.
  Masalah yang didiagnosis          : Penentuan rute logistik ini merupakan masalah kombinatorial kompleks yang dikenal sebagai Travelling Salesman Problem (TSP) yang sulit diselesaikan tanpa bantuan algoritma optimasi.
  Masalah riset (researchable)      : Bagaimana penerapan Algoritma Genetika untuk mengoptimasi rute terpendek dan menekan biaya perjalanan kurir di PT. Pos Cabang Lamongan?
  Variabel yang terukur             : Total jarak tempuh (km) dan Biaya perjalanan (Rupiah)

Problem Quality Check
  [X] Clarity — Apakah satu orang membaca akan paham?
  [X] Measurability — Apakah ada metrik kuantitatif?
  [X] Relevance — Apakah penting untuk domain?
  [X] Testability — Apakah bisa gagal?
  [X] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  PT. Pos Indonesia Cabang Lamongan memiliki 12 titik drop point pengiriman, yang memicu kompleksitas kombinatorial (Travelling Salesman Problem) jika kurir menentukan rute secara manual. Hal ini dapat menyebabkan rute yang diambil tidak efisien, berujung pada membengkaknya waktu dan biaya operasional bahan bakar. Oleh karena itu, penelitian ini menerapkan Algoritma Genetika—yang dikenal stabil dalam mengatasi masalah kombinatorial besar—untuk mengukur secara kuantitatif rute paling optimal (dalam kilometer) dan mengkalkulasi efisiensi biayanya (dalam Rupiah)
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Optimasi Rute Pengiriman Barang (Travelling Salesman Problem)

| Tahap | Hasil |
|-------|-------|
| Reality | *Pengiriman barang dan surat memiliki banyak titik drop point yang tersebar di berbagai kecamatan.* |
| Observed Issue (Symptom) | *Kurir berpotensi melakukan proses distribusi berdasarkan keinginan/insting semata sehingga membuang waktu dan bahan bakar.* |
| Diagnosed Problem (Root Cause) | *Mencari kombinasi rute terpendek dari puluhan titik (TSP) secara manual membutuhkan waktu yang sangat lama dan rentan tidak optimal.* |
| Researchable Problem | *Dapatkah Algoritma Genetika digunakan untuk menemukan rute terpendek PT. Pos Cabang Lamongan dan menghitung estimasi biaya distribusinya?* |
| Measurable Variable | *Panjang lintasan atau kromosom (kilometer) dan total biaya operasional (Rp 1.000 per km).* |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> Karena masalah besarnya kombinasi rute (TSP) sudah ada terlebih dahulu di lapangan sebelum metode Algoritma Genetika diusulkan sebagai solusinya.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | *Data 19 titik koordinat kantor pos dari Google Maps beserta representasi jaraknya dalam kilometer.* |
| Process | *Mengubah urutan rute menjadi kromosom, mengevaluasi nilai fitness, lalu melakukan seleksi mutasi dan crossover selama 2 siklus pencarian.* |
| Output | *Terbentuknya kromosom terbaik yang merepresentasikan rute (misal: A-L-K-J-I-H-G-F-E-D-C-B-A) dengan total jarak 158 km.* |
| Outcome | *Kejelasan estimasi biaya perjalanan (Rp 158.000) yang bisa dialokasikan perusahaan logistik.* |
| Constraints | *Setiap kantor/titik harus dikunjungi tepat satu kali, tidak boleh lebih, dan harus kembali ke titik asal.* |
| Stakeholders | *Perusahaan logistik (PT. Pos Indonesia) dan kurir pengantar.*|

**Komponen mana yang paling relevan dengan masalah riset?** Proses (Process), karena di sinilah intervensi riset (penerapan perhitungan metode Algoritma Genetika) dilakukan untuk mencari pengetahuan baru (urutan rute).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | *5* | *Sangat jelas, pembaca langsung tahu masalahnya adalah mencari rute untuk kurir pos.* |
| Measurability | *5* | *Diukur dengan pasti menggunakan jarak (km) dan biaya operasional (Rupiah).* |
| Relevance | *5* | *Optimasi rute adalah masalah inti dan esensial dalam industri logistik.* |
| Testability | *4* | *Hipotesis pencarian rute bisa diuji coba, namun pembatasan manual pada "2 siklus" membuat uji konvergensi algoritma kurang komprehensif.* |
| Impact | *4* | *Berdampak langsung pada efisiensi PT Pos Lamongan, namun sulit digeneralisasi untuk cabang lain tanpa perhitungan ulang.* |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Permasalahan distribusi barang pada PT. Pos Indonesia Cabang Lamongan melibatkan banyak drop point yang harus dilalui kurir. Jika kurir menentukan rute berdasarkan insting, perusahaan berisiko menanggung biaya perjalanan dan waktu tempuh yang tidak efisien akibat kompleksitas rute (Travelling Salesman Problem). Oleh karena itu, penelitian ini menginvestigasi penerapan Algoritma Genetika untuk mengkalkulasi secara sistematis rute dengan jarak tempuh terpendek (dalam km) serta menghitung implikasi biaya bahan bakarnya (dalam Rupiah).
> ___________________________________________________

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamentalnya terletak pada tujuan akhir. Dalam engineering atau masalah coding (seperti rute kurir tidak muncul di aplikasi), pendekatannya berfokus pada "Bagaimana cara memperbaiki sistem ini agar fitur rute berfungsi?". Masalah selesai ketika kode berhasil compile dan klien puas. Sebaliknya, dalam masalah riset (seperti pada jurnal ini), pendekatannya adalah mencari pemahaman baru: "Apakah algoritma evolusioner benar-benar menghasilkan urutan rute yang lebih hemat biaya dibandingkan rute acak?". Outputnya bukan sekadar kode python yang berjalan , melainkan validasi ilmiah bahwa jarak 158 km dan pengeluaran Rp 158.000 adalah titik optimal berdasarkan variabel yang diuji.
> ___________________________________________________
