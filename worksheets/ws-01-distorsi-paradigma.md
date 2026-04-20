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
Tanggal          : 20 April 2026 

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: "Apakah hasil ini merupakan nilai optimal global atau hanya berhenti pada local optima karena siklus yang terbatas?"
   - Data yang dibutuhkan untuk verifikasi: "Parameter lengkap algoritma (ukuran populasi, probabilitas crossover, dan mutasi) serta perbandingan hasil dengan algoritma optimasi lain sebagai baseline."

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [x] Design Science  [ ] Mixed
   - Alasan: Penelitian ini membangun sebuah artefak berupa prosedur optimasi menggunakan Algoritma Genetika untuk menyelesaikan masalah praktis dalam penentuan rute pengiriman barang di PT. Pos.
3. Identifikasi distorsi:
   - Asumsi tersembunyi: Penelitian ini membangun sebuah artefak berupa prosedur optimasi menggunakan Algoritma Genetika untuk menyelesaikan masalah praktis dalam penentuan rute pengiriman barang di PT. Pos.
   - Sumber bias potensial: Penghentian siklus (syarat berhenti) dilakukan secara manual setelah 2 siklus hanya karena hasilnya sudah sama, yang mungkin belum mencapai konvergensi yang sebenarnya dalam algoritma stokastik.
   - Langkah mitigasi: Menjalankan simulasi dengan jumlah iterasi yang lebih besar (misalnya 100+ generasi) menggunakan bantuan pemrograman untuk memastikan stabilitas hasil.
4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Jarak antar titik lokasi yang diperoleh dari Google Maps dan nilai fitness yang dihitung dari panjang lintasan.
   - Batasan yang diakui sejak awal: Hasil penelitian ini bergantung pada ukuran populasi, besar generasi, serta nilai peluang crossover dan mutasi yang digunakan.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Penerapan Algoritma Genetika Dalam Menentukan Rute Terpendek PT. Pos Cabang Lamongan
> Penulis (Tahun): Ahmad Tohari & Yuliani Puji Astuti (2023)
> Sumber/Link DOI: MATHunesa: MATHunesa, Vol 11 No 03

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | *Mengumpulkan 19 titik lokasi kantor pos dan mencari koordinat serta jarak menggunakan Google Maps* | *Sampling Bias: Hanya menggunakan 19 titik tertentu, mungkin tidak mencakup seluruh variasi rute harian yang sebenarnya dihadapi kurir.* |
| Data → Processing | *Jarak diubah menjadi bilangan integer dalam satuan kilometer untuk perhitungan.*  | *Rounding Error: Pembulatan ke integer terdekat dapat menghilangkan akurasi jarak presisi (meter) yang krusial untuk optimasi.*  |
| Processing → Analysis | *Menjalankan Algoritma Genetika melalui 2 siklus dengan parameter populasi, crossover, dan mutasi.*  | *Algorithmic Bias: Hasil sangat bergantung pada ukuran populasi dan peluang mutasi/crossover yang ditentukan peneliti.*  |
| Analysis → Inference | *Menentukan rute A-L-K-J-I-H-G-F-E-D-C-B-A sebagai yang terpendek (158 km).*  | *Local Optima: Karena hanya dilakukan 2 siklus, ada kemungkinan algoritma terjebak di solusi "cukup baik" tapi bukan yang terbaik global.*  |
| Inference → Knowledge |*Menyimpulkan biaya operasional sebesar Rp 158.000 berdasarkan konsumsi BBM rata-rata*  | *Generalization Bias: Mengasumsikan harga BBM dan konsumsi kendaraan tetap (10km/liter), padahal kondisi jalan memengaruhi realitas.*  |

**Distorsi paling besar di tahap:** Generalization Bias: Mengasumsikan harga BBM dan konsumsi kendaraan tetap (10km/liter), padahal kondisi jalan memengaruhi realitas.

**Dua distorsi spesifik yang teridentifikasi:**
1. Convergence Bias: Penghentian eksperimen hanya pada 2 siklus karena hasil sudah sama, padahal algoritma genetika bersifat acak dan mungkin butuh lebih banyak iterasi untuk validitas maksimal.
2. Environmental Distortion: Perhitungan jarak menggunakan Google Maps tidak memperhitungkan faktor realitas seperti kemacetan atau perbaikan jalan yang bisa mengubah "rute terpendek" menjadi "rute terlama".

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Peneliti menghentikan siklus pada iterasi ke-2 karena hasilnya sudah sama (konvergen).

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | *Peneliti menghentikan siklus pada iterasi ke-2 karena hasilnya sudah sama (konvergen).* |
| Transparansi | *Peneliti secara transparan menyebutkan bahwa sifat algoritma genetika adalah random dan tidak diketahui pasti kapan hasil optimal muncul.* |
| Peer review | *Penelaah mungkin akan mempertanyakan apakah 2 siklus cukup untuk populasi yang kompleks, sehingga peneliti harus menyediakan data mentah setiap siklus.* |

**Keputusan akhir dan justifikasi:**
> Peneliti tetap melaporkan hasil 158 km tersebut namun memberikan limitasi bahwa hasil ini bergantung pada parameter yang disetel. Justifikasinya adalah efisiensi komputasi untuk studi kasus spesifik ini.
---

## Latihan 3 — Posisi Paradigma

**Topik riset:**Optimasi Rute Distribusi Logistik Menggunakan Algoritma Evolusioner.

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 (Fokus pada pengukuran objektif jarak dan biaya). | 1 (Tidak berfokus pada pengalaman subjektif kurir). | 5 (Membangun model/algoritma sebagai solusi masalah praktis). |
| Jenis data yang dikumpulkan | Jarak (km), Nilai Fitness, Biaya (Rp). | - | Hasil iterasi kromosom dan rute optimal.* |
| Limitasi paradigma |  Mengabaikan faktor manusia/cuaca di lapangan. | Mengabaikan faktor manusia/cuaca di lapangan. |  Mengabaikan faktor manusia/cuaca di lapangan. |

**Paradigma yang dipilih:**Design Science Research (DSR) diperkuat Positivis.
**Alasan:**Penelitian ini bertujuan memecahkan masalah nyata (rute PT. Pos) dengan membangun artefak berupa prosedur Algoritma Genetika dan menguji validitasnya secara kuantitatif melalui perhitungan jarak dan fitness.


---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelumnya, saya mungkin menganggap rute dari Google Maps adalah mutlak benar. Setelah memahami rantai distorsi, saya sekarang akan mempertanyakan: "Apakah pembulatan jarak ke integer memengaruhi akurasi rute?" atau "Apakah 2 siklus cukup untuk menjamin bahwa tidak ada rute yang lebih pendek lagi?".
