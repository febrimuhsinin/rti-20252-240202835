# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah terdapat perbedaan skor System Usability Scale (SUS) yang signifikan antara alur transaksi belanja umum dengan alur transaksi pada fitur Shopee Food bagi pengguna Generasi Z?
Hypothesis        : Alur transaksi Shopee Food memiliki rata-rata skor SUS yang secara signifikan lebih rendah dibandingkan alur belanja reguler (H₁).
Tipe Eksperimen   : [x] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control   | Alur transaksi belanja reguler (Checkout barang fisik).| Belanja Reguler | Responden Gen Z, Smartphone yang sama, Jaringan stabil.            |
| Treatment | Alur transaksi Shopee Food (Checkout makanan).         | Shopee Food     | Responden yang sama (Within-subjects), Durasi pengerjaan yang sama.|

Fairness Checklist:
  [x] Dataset identik: Menggunakan kelompok responden yang sama untuk kedua kondisi.
  [x] Preprocessing setara: Instruksi tugas diberikan dengan tingkat kejelasan yang sama.
  [x] Tuning effort setara: Kedua fitur diuji pada versi aplikasi yang sama (versi terbaru).
  [x] Environment identik: Pengujian dilakukan di laboratorium/ruangan yang sama.
  [x] Metrik evaluasi sama: Keduanya diukur menggunakan instrumen SUS 10 item.

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Learning Effect: User lebih cepat di tugas kedua karena sudah familiar dengan UI.        | Melakukan counterbalancing (Urutan tugas diacak untuk setiap user). |
| External    | Selection Bias: Responden hanya berasal dari satu universitas (Gen Z).                   | Menambah keberagaman fakultas dan latar belakang penggunaan aplikasi.          |
| Construct   | Social Desirability Bias: Responden cenderung memberi skor tinggi karena suka brand-nya. | Menegaskan anonimitas dan meminta kejujuran demi pengembangan ilmu.                 |
| Conclusion  | Social Desirability Bias: Responden cenderung memberi skor tinggi karena suka brand-nya. | Memastikan jumlah sampel memenuhi syarat minimal uji statistik (N=30-50).          |

Statistical Plan:
  Uji statistik   : Paired Sample T-Test.
  Justifikasi      : Membandingkan rata-rata dari dua kondisi yang diberikan kepada kelompok responden yang sama (dependent samples).
  Alpha            : 0.05.
  Effect size min  : 0.5 (Medium effect size berdasarkan Cohen’s d).
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Sejauh mana efisiensi alur pembayaran Shopee Food dibandingkan belanja reguler jika diukur dari perspektif pengguna ahli (Gen Z)?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | *Skenario membeli 1 barang di Shopee Mall hingga halaman pembayaran.* | *Belanja Reguler* | *Versi Aplikasi 3.x, Smartphone Android/iOS, Lokasi Kampus.* |
| Treatment | *Skenario memesan 1 menu di Shopee Food hingga halaman pembayaran.* | *Shopee Food* | *Versi Aplikasi 3.x, Smartphone Android/iOS, Lokasi Kampus.* |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| *Dataset identik* | *✅* | *Responden yang mengisi kuesioner Shopee Food adalah orang yang sama dengan pengisi Shopee Mall.* |
| *Preprocessing setara* | *✅* | *Skenario tugas ditulis dengan jumlah langkah yang setara (rata-rata 5-7 klik).* |
| *Tuning effort setara* | *✅* | *Peneliti tidak memberikan bantuan tutorial pada salah satu fitur saja.* |
| *Environment identik* | *✅* | *Menggunakan satu koneksi Wi-Fi publik yang sama untuk meminimalkan latency.* |
| *Metrik evaluasi sama* | *✅* | *Keduanya dihitung menggunakan formula SUS: (X-1) + (5-Y) \ 2.5* |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| *Internal* | *Kelelahan responden (Respondent Fatigue) saat mengisi kuesioner kedua.* | *Memberikan jeda waktu 5 menit antar tugas dan menjaga kuesioner tetap singkat.* |
| *External* | *Hasil mungkin tidak berlaku untuk pengguna usia lansia (Silver Gen).* | *Membatasi klaim generalisasi hanya untuk populasi Gen Z.* |
| *Construct* | *Membatasi klaim generalisasi hanya untuk populasi Gen Z.* | *Menambahkan metrik sekunder berupa Success Rate atau Task Completion Time.* |
| *Conclusion* | *Data tidak terdistribusi normal sehingga T-Test tidak valid.* | *Melakukan uji normalitas (Shapiro-Wilk) terlebih dahulu; jika tidak normal gunakan Wilcoxon Signed-Rank Test.* |

**Ancaman mana yang paling sulit dimitigasi?** Ancaman Eksternal (Generalisasi).
Mengapa?
**Mengapa?**
> Sangat sulit mengumpulkan sampel yang benar-benar mewakili seluruh pengguna Shopee di Indonesia yang mencapai jutaan orang dengan latar belakang pendidikan dan geografi yang sangat beragam.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
Jika sebuah paper mengklaim metodenya mengalahkan semua baseline, 3 pertanyaan kritis untuk mengevaluasi klaim tersebut adalah:
1. Siapa baselinenya? Apakah baseline yang dipilih adalah metode State-of-the-Art (SOTA) terbaru atau hanya metode usang yang sengaja dipilih agar terlihat lemah (straw man comparison)?
2. Apakah kondisinya identik? Apakah baseline dijalankan dengan tuning parameter yang maksimal, atau hanya menggunakan pengaturan default sementara metode baru dioptimalkan secara agresif?
3. Seberapa signifikan perbedaannya secara statistik? Apakah kenaikan performa tersebut memiliki p-value yang rendah dan effect size yang cukup besar, atau hanya kenaikan angka marjinal yang bisa terjadi karena faktor kebetulan?
