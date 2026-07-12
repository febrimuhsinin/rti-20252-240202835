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
| Control   | Skenario alur belanja reguler (Baseline).       | Belanja Reguler | Demografi Gen Z, Mahasiswa aktif, Koneksi Internet Stabil, Gawai Smartphone            |
| Treatment | Skenario pemesanan fitur tambahan (Shopee Food) | Shopee Food     | Demografi Gen Z, Mahasiswa aktif, Koneksi Internet Stabil, Gawai Smartphone            |

Fairness Checklist:
  [x] Dataset identik: untuk semua kondisi (Menggunakan kelompok responden yang sama / within-subjects)
  [x] Preprocessing setara: (Instruksi dan kompleksitas langkah dibuat seimbang)
  [x] Tuning effort setara: (Waktu istirahat jeda 5 menit antar sesi agar tidak lelah)
  [x] Environment identik: (Koneksi dan perangkat diseragamkan via screening kualifikasi awal)
  [x] Metrik evaluasi sama: (Menggunakan instrumen 10-item SUS Likert Scale)

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Order Bias / Learning Effect (Hafal urutan tombol aplikasi).                             | Menerapkan teknik Counterbalancing (Setengah responden mulai dari Reguler, setengah dari Food).|
| External    | Hasil penelitian terlalu spesifik pada kalangan tertentu.                                | Membatasi ruang lingkup (scope) populasi sasaran sejak awal dengan inklusi spesifik Gen Z usia 18-25.   |
| Construct   | Social Desirability Bias: Responden cenderung memberi skor tinggi karena suka brand-nya. | Menegaskan anonimitas dan meminta kejujuran demi pengembangan ilmu.                 |
| Conclusion  | Social Desirability Bias: Responden cenderung memberi skor tinggi karena suka brand-nya. | Memastikan jumlah sampel memenuhi syarat minimal uji statistik (N=30-50).          |

Statistical Plan:
  Uji statistik   : Paired Sample T-Test.
  Justifikasi      : Membandingkan perbedaan rata-rata dari dua kondisi pada kelompok responden yang sama (paired data).
  Alpha            : 0.05.
  Effect size min  : 0.5 (Medium effect size berdasarkan Cohen’s d).
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah terdapat perbedaan skor System Usability Scale (SUS) yang signifikan antara alur transaksi belanja reguler dengan alur transaksi pada fitur Shopee Food bagi pengguna Generasi Z?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | *Alur belanja retail fisik reguler pada Shopee (Baseline)* | *Belanja Reguler* | *Pengguna Gen Z, Mahasiswa aktif, Pengalaman > 1 tahun, Jaringan stabil* |
| Treatment | *Skenario memesan 1 menu di Shopee Food hingga halaman pembayaran.* | *Shopee Food* | *Pengguna Gen Z, Mahasiswa aktif, Pengalaman > 1 tahun, Jaringan stabil* |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| *Dataset identik* | *✅* | *Responden yang menguji Skenario Reguler adalah orang yang persis sama dengan yang menguji Skenario Food (within-subjects N=36).* |
| *Preprocessing setara* | *✅* | *Responden diberikan jeda interval waktu 5 menit antar skenario untuk mencegah kejenuhan/kelelahan kognitif.* |
| *Tuning effort setara* | *✅* | *Karena remote testing, environment dikunci via Form Screening awal (wajib centang internet stabil dan ruangan kondusif).* |
| *Environment identik* | *✅* | *Menggunakan satu koneksi Wi-Fi publik yang sama untuk meminimalkan latency.* |
| *Metrik evaluasi sama* | *✅* | *Skor dievaluasi menggunakan instrumen baku System Usability Scale (SUS) dengan perhitungan konstanta yang sama persis (Skala 0-100).* |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| *Internal* | *Bias urutan pengerjaan (Order Bias) / Partisipan kelelahan di skenario kedua.* | *Penyeimbangan silang (Counterbalancing): 15 orang rute Reguler->Food, 15 orang rute Food->Reguler.* |
| *External* | *Riwayat penggunaan partisipan sangat berbeda (ada yang sering pakai Food, ada yang tidak pernah).* | *Pencatatan riwayat transaksi 30 hari terakhir di form awal sebagai variabel kovariat.* |
| *Construct* | *Bias Loyalitas Merek (Habituation Effect); responden menilai tinggi aplikasi semata karena sudah terbiasa/suka.* | *Penggunaan SUS yang fokus pada metrik interaksi fisik operasional (perceived usability) daripada sekadar tanya kepuasan subjektif.* |
| *Conclusion* | *Asumsi normalitas ditolak karena respons pengguna terlalu ekstrem.* | *Disiapkan prosedur kontinjensi uji statistik non-parametrik ekuivalen (Wilcoxon Signed-Rank Test).* |

**Ancaman mana yang paling sulit dimitigasi?** Ancaman Eksternal (Generalisasi).
Mengapa?
**Mengapa?**
> Karena Shopee berstatus sebagai super-app yang sudah digunakan bertahun-tahun oleh responden Gen Z, secara tidak sadar mereka sudah memaklumi kerumitan UI-nya. Menyadarkan responden untuk secara kritis menilai feature bloat (seperti menumpuknya banner promo dan navigasi pihak ketiga) melalui instrumen skala persepsional tanpa eye-tracking secara langsung merupakan tantangan terbesar yang dapat menimbulkan deviasi skor.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
Jika sebuah paper mengklaim metodenya mengalahkan semua baseline, 3 pertanyaan kritis untuk mengevaluasi klaim tersebut adalah:
1. Apakah "baseline" yang dipakai merupakan kontrol standar yang layak dan optimal, atau hanya straw man (metode usang yang sengaja dilemahkan/tidak dioptimasi agar metode peneliti terlihat lebih bagus)?

2. Apakah kondisi eksperimen (seperti dataset, spesifikasi lingkungan/instrumen pengujian, dan teknik evaluasi) diperlakukan 100% sama (identik) untuk semua metode yang sedang dibandingkan?

3. Apakah selisih pengukurannya terbukti signifikan secara statistik (terdapat uji p-value atau estimasi effect size), atau perbedaannya terjadi karena kebetulan (variance kebetulan akibat sampel data yang terlampau kecil)?
