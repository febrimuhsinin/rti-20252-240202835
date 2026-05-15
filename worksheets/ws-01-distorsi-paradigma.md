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
   - Apakah dataset yang digunakan seimbang (balanced) dan bagaimana performa metode tersebut dibandingkan dengan baseline yang sudah ada?
   - Data yang dibutuhkan untuk verifikasi: Matriks konfusi (Confusion Matrix), distribusi kelas pada dataset, dan kondisi lingkungan eksperimen (perangkat/koneksi).

2. Posisi paradigma:
   - Pendekatan: [x] Positivis [ ] Interpretivis [x] Design Science [ ] Mixed
   - Alasan: Usability dapat diukur secara objektif melalui metrik kuantitatif (SUS), dan penelitian ini sering kali melibatkan evaluasi artefak digital (aplikasi) untuk membuktikan proposisi kemudahan penggunaan.
3. Identifikasi distorsi:
   - Asumsi tersembunyi: Pengguna Generasi Z dianggap mewakili seluruh populasi pengguna e-commerce.
   - Sumber bias potensial: Sampling bias (responden hanya dari satu wilayah/universitas) dan social desirability bias (responden memberi skor tinggi karena menyukai brand).
   - Langkah mitigasi: Melakukan teknik random sampling yang lebih luas dan menegaskan anonimitas responden saat pengisian kuesioner.
4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Skor asli dari setiap responden dalam kuesioner SUS meskipun hasilnya tidak signifikan.
   - Batasan yang diakui sejak awal: Keterbatasan jumlah sampel dan spesifikasi perangkat yang digunakan oleh responden.   
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Analisis Aplikasi E-Commerce pada Generasi Z dengan  
Pendekatan System Usability Scale
> Penulis (Tahun): Lim et al. (2025)
> Sumber/Link DOI: IRPI - MALCOM Journal

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | *Mengumpulkan persepsi pengguna Gen Z di Batam.* | *Sampling Bias: Hasil di Batam mungkin tidak mencerminkan perilaku pengguna di pedesaan.* |
| Data → Processing | *Mengonversi skala Likert 1-5 menjadi skor SUS.*  | *Error Distorsi: Kesalahan rumus manual jika tidak menggunakan alat bantu otomatis.*  |
| Processing → Analysis | *Menghitung rata-rata skor (90.06).*  | *Outlier Distortion: Nilai ekstrem dari satu responden bisa menarik rata-rata terlalu tinggi.*  |
| Analysis → Inference | *Menyimpulkan Shopee "Best Imaginable".*  | *External Validity: Klaim terlalu luas hanya berdasarkan satu kelompok demografi.*  |
| Inference → Knowledge |*Menetapkan standar usability Gen Z.*  | *Construct Validity: SUS hanya mengukur persepsi, bukan efisiensi teknis nyata.*  |

**Distorsi paling besar di tahap:** Reality → Data (Sampling Bias).

**Dua distorsi spesifik yang teridentifikasi:**
1. Selection Bias: Hanya melibatkan responden dari satu kota (Batam), sehingga generalisasi secara nasional lemah.
2. Homogeneity Bias: Fokus hanya pada Gen Z yang secara alami lebih mahir teknologi, sehingga skor 90.06 mungkin terlalu optimis jika diterapkan pada pengguna lansia.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Peneliti menghapus 3 outlier agar hasil signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | *Menghapus data tanpa justifikasi metodologis yang jelas adalah bentuk fabrikasi halus yang merusak integritas riset.* |
| Transparansi | *Peneliti harus menjelaskan kriteria mengapa data tersebut dianggap outlier (misal: pengisian asal-asalan) dalam bab metodologi.* |
| Peer review | *Reviewer berhak melihat data mentah untuk memastikan penghapusan outlier tidak dilakukan hanya demi mendapatkan nilai p < 0.05.* |

**Keputusan akhir dan justifikasi:**
> Tetap melaporkan seluruh data. Jika outlier dihapus, berikan alasan teknis (misal: responden mengisi pola zigzag yang tidak valid). Idealnya, laporkan hasil dengan dan tanpa outlier agar pembaca mendapatkan gambaran yang jujur mengenai variansi data.
---

## Latihan 3 — Posisi Paradigma

**Topik riset:**Evaluasi Usability dan User Experience Aplikasi Shopee Menggunakan Metode System Usability Scale (SUS).

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| *Kesesuaian dengan topik (1–5)* | *5* | *2* | *4* |
| *Jenis data yang dikumpulkan* | *Skor SUS (Numerik).* | *Hasil wawancara mendalam.* | *Performa prototipe baru.* |
| *Limitasi paradigma* | *Mengabaikan perasaan subjektif yang tidak terwakili angka.* | *Sulit untuk digeneralisasi.* | *Fokus pada pembuatan alat, bukan hanya pemahaman.* |

**Paradigma yang dipilih:**Positivis diperkuat dengan Design Science Research.
**Alasan:**Topik ini menuntut pembuktian objektif terhadap tingkat usability yang dapat diukur secara statistik (Positivis), namun juga bertujuan untuk memberikan rekomendasi perbaikan desain pada artefak aplikasi (Design Science).

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum memahami materi ini, saya cenderung menerima angka "95% akurat" sebagai kebenaran mutlak. Namun, setelah memahami Rantai Distorsi, pertanyaan yang akan saya ajukan adalah: "Bagaimana distribusi datanya? Apakah ada bias dalam pemilihan sampel? Dan apakah metrik tersebut benar-benar mencerminkan pengalaman nyata pengguna atau hanya angka di atas kertas?" Pemahaman ini membuat saya lebih kritis dalam melihat setiap klaim riset, terutama di bidang TI yang sangat dinamis.
