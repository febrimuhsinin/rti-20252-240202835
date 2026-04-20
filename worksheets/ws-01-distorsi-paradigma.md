# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Febri Muhsinin
Tanggal          : ____________________

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: "Berapa jumlah data (N) yang digunakan dan bagaimana pembagian training/testing set-nya?"
   - Data yang dibutuhkan untuk verifikasi: "Berapa jumlah data (N) yang digunakan dan bagaimana pembagian training/testing set-nya?"

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [x] Design Science  [ ] Mixed
   - Alasan: Saya lebih banyak mengembangkan solusi teknis (seperti JavaFX/PostgreSQL) untuk memecahkan masalah spesifik.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Menganggap semua pengguna memiliki perilaku yang sama saat menggunakan aplikasi.
   - Sumber bias potensial: Data testing yang hanya diambil dari lingkungan kampus (homogen).
   - Langkah mitigasi: Menggunakan Cross-Validation dan mengambil sampel data dari luar lingkungan utama.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Menggunakan Cross-Validation dan mengambil sampel data dari luar lingkungan utama.
   - Batasan yang diakui sejak awal: Algoritma mungkin melambat pada dataset yang bersifat high-dimensional.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Optimasi Penjadwalan Mata Kuliah Menggunakan Algoritma Genetika (Studi Kasus: Fakultas Teknologi Informasi)
> Penulis (Tahun): R. Helilintar, dkk. (2021)
> Sumber/Link DOI: Jurnal Teknologi Informasi dan Terintegrasi (JITIKA)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | *Mengambil data mata kuliah, dosen, dan ketersediaan ruangan di kampus.* | *Sampling Bias: Data mungkin hanya diambil dari satu semester yang "ideal", tidak mencakup semester sibuk.* |
| Data → Processing | *Representasi data ke dalam bentuk kromosom dan penentuan parameter (Populasi, Mutasi, Crossover).*  | *Data Cleaning Bias: Menghapus mata kuliah yang sulit dijadwalkan secara manual agar algoritma terlihat lebih cepat konvergen.*  |
| Processing → Analysis | *Menjalankan iterasi algoritma untuk meminimalkan bentrok (fitness function).*  | *Hardware Bias: Kecepatan eksekusi hanya diukur pada satu PC spesifik tanpa mempertimbangkan variasi beban server.*  |
| Analysis → Inference | *Menyimpulkan bahwa algoritma genetika lebih efektif daripada penjadwalan manual.*  | *Cherry-picking: Hanya menampilkan hasil iterasi terbaik, sementara hasil yang gagal/stuck di lokal optimum tidak dibahas.*  |
| Inference → Knowledge |*Mengklaim metode ini adalah solusi terbaik untuk semua kasus penjadwalan serupa.*  | *Over-generalization: Belum tentu efektif jika jumlah ruangan sangat terbatas atau kendala (constraint) ditambah.*  |

**Distorsi paling besar di tahap:** Data → Processing (Penentuan bobot fitness function yang subjektif).

**Dua distorsi spesifik yang teridentifikasi:**
1. Algorithmic Bias: Penentuan nilai probabilitas mutasi dan crossover yang dilakukan secara trial-error tanpa justifikasi matematis yang kuat.
2. Measurement Bias: Mengukur kesuksesan hanya dari ketiadaan bentrok, namun mengabaikan preferensi dosen (aspek kualitatif).

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | *Menghapus outlier tanpa penjelasan adalah bentuk manipulasi data. Peneliti harus jujur bahwa data tidak seragam.* |
| Transparansi | *Peneliti wajib menjelaskan mengapa outlier tersebut muncul (apakah karena kesalahan sensor atau anomali nyata).* |
| Peer review | *Jika disembunyikan, reviewer tidak bisa memvalidasi kebenaran klaim. Transparansi justru meningkatkan kepercayaan reviewer.* |

**Keputusan akhir dan justifikasi:**
> Tetap menyertakan outlier dalam laporan. Jika outlier memang disebabkan oleh kesalahan teknis (misal: noise perangkat), jelaskan alasan penghapusannya secara eksplisit. Namun, jika outlier adalah bagian dari fenomena nyata, gunakan metode statistik yang robust (tahan outlier) agar hasil riset tetap valid tanpa berbohong.
---

## Latihan 3 — Posisi Paradigma

**Topik riset:** ________________________________________

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | * 4 * | * 2 * | * 5 * |
| Jenis data yang dikumpulkan | *Akurasi rekomendasi, nilai fitness, waktu eksekusi.* | *Kepuasan emosional pengguna saat memilih baju.* | *Artefak berupa sistem/aplikasi rekomendasi outfit.* |
| Limitasi paradigma |  *Mengabaikan selera fashion yang subjektif.* | *Sulit direplikasi secara sistematis/massal.* |  *Fokus sering bergeser ke pembuatan aplikasi (coding), bukan temuan ilmiah.* |

**Paradigma yang dipilih:**Design Science Research (DSR)
**Alasan:** Riset ini bertujuan membangun sebuah artefak (algoritma optimasi) untuk memecahkan masalah praktis (kebingungan memilih outfit). Keberhasilan diukur dari seberapa baik artefak tersebut bekerja melalui pengujian fungsionalitas dan kinerja.


---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Dulu saya sering menelan mentah-mentah angka akurasi yang tinggi sebagai indikator keberhasilan mutlak. Setelah memahami rantai distorsi, saya kini akan bertanya: "Di tahap mana data ini mungkin bias?" dan "Apakah hasil ini bisa direproduksi (reproducible) di lingkungan yang berbeda?" Saya menjadi lebih kritis terhadap validitas internal sebelum mempercayai sebuah kesimpulan.
