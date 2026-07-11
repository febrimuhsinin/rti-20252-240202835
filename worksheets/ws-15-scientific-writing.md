# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Evaluasi Dampak Usability Integrasi Layanan Pesan-Antar Makanan pada Super-App E-Commerce: Studi Kasus Shopee Reguler vs Shopee Food
Target  : [ ] Jurnal  [ ] Konferensi  [x] Laporan/Manuskrip Akademik

Section Check:
  [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [x] Related Work — concept-centric, gap positioning
  [x] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [x] Results — tabel + grafik + observasi (tanpa interpretasi)
  [x] Discussion — interpretasi, perbandingan, implikasi, limitation
  [x] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [ ] RQ di Introduction = RQ di Method = RQ di Conclusion
  [ ] Variabel di Method = variabel di Results
  [ ] Klaim di Discussion didukung data di Results
  [ ] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [ ] Clarity — mudah dipahami tanpa re-read
  [ ] Precision — tidak ada istilah ambigu
  [ ] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | *Transisi E-Commerce ke Super-App berisiko menurunkan usability. Studi ini membandingkan skor SUS antara Shopee Reguler dan Shopee Food dengan 36 responden Gen Z. Hasil uji T-Test menunjukkan degradasi usability yang sangat signifikan (p<0.05).* | 200-250 |
| Introduction | *Konteks: Fenomena Super-App di Asia Tenggara. Gap: Minimnya evaluasi komparasi UX antarmodul dalam satu aplikasi yang sama. RQ: Apakah kompleksitas fitur Shopee Food menurunkan kepuasan pengguna dibanding alur Reguler?* | 500-700 |
| Related Work | *Mengulas literatur mengenai Cognitive Overload pada mobile UI, efektivitas System Usability Scale (SUS), dan tren desain arsitektur Super-App.* | 700-1000 |
| Method | *Desain eksperimen within-subjects dengan instrumen SUS (versi kombinasi 19 item valid + 1 imputasi). Kriteria sampel: 36 partisipan Gen Z usia 18-25 tahun yang merupakan pengguna aktif Shopee.* | 800-1200 |
| Results | *Laporan data deskriptif: Skor SUS Reguler (60.56) vs Food (48.26). Hasil Paired Sample T-Test membuktikan p-value = 7.62e-09.* | 500-800 |
| Discussion | *Skor 48.26 masuk kategori 'Not Acceptable'. Ini membuktikan fitur terlalu padat (cluttered). Limitasi: Adanya missing data struktural pada instrumen untuk 1 butir pertanyaan SUS yang mengharuskan penggunaan Constant Imputation.* | 600-900 |
| Conclusion | *H0 ditolak. Penambahan fitur turunan secara signifikan mendegradasi usability aplikasi utama. Rekomendasi redesign difokuskan pada penyederhanaan navigasi.* | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ1 (Perbedaan Usability) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik utama (Skor SUS)   | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel IV (Tipe Alur)   | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel DV (Skor UX)     | ✓ | ✓ | ✓ | ✓ | ✓ |
| Klaim/kontribusi (Super-app rentan overload) | ✓ | ✓ | ✓ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Secara keseluruhan sudah konsisten. Namun sering kali detail *missing data* (imputasi pertanyaan No.2) lupa dijelaskan di bagian Introduction atau Method, lalu tiba-tiba muncul di Discussion.

**Tindakan perbaikan:**
> Menambahkan penjelasan eksplisit mengenai modifikasi/imputasi instrumen SUS langsung ke dalam bab Method (Sub-bab Pengumpulan Data), agar justifikasi statistik di Result menjadi valid sejak awal.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Hasil eksperimen kami membuktikan bahwa performa Shopee Food terasa lebih jelek dari belanja biasa. Ini ditunjukkan dari skor surveinya yang berbeda jauh.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Kata "jelek" sangat tidak profesional dan tidak jelas metriknya apa. | Ubah menjadi kata teknis *"tingkat usability yang lebih rendah"* |
| Precision | "Berbeda jauh" itu subjektif dan tidak ada angka pastinya. | Cantumkan *"(Mean: 48.26 vs 60.56; p < 0.05)"* |
| Conciseness | "Hasil eksperimen kami membuktikan bahwa..." agak bertele-tele. | Singkat menjadi *"Berdasarkan analisis statistik,..."* |

**Paragraf setelah perbaikan:**
> Berdasarkan analisis statistik menggunakan uji Paired Sample T-Test, alur transaksi Shopee Food terbukti memiliki tingkat *usability* yang secara signifikan lebih rendah dibandingkan alur belanja reguler (Mean: 48.26 vs 60.56; p < 0.05).

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset rasanya seperti sekadar mendongeng atau menceritakan kronologi kegiatan penelitian. Sebaliknya, menulis sebagai "argumen" berarti saya secara aktif meyakinkan pembaca (dengan menggunakan bukti-bukti statistik dan literatur) bahwa *cognitive overload* memang terjadi di aplikasi Shopee dan H1 saya terbukti valid. 
> Urutan penulisan yang dibalik (Method -> Result -> Discussion -> Introduction) mencegah *writer's block* dan memastikan Introduction yang saya tulis di akhir tidak memberi janji-janji palsu yang tidak bisa dibuktikan oleh Result.
