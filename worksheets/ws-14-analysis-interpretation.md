# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | n |
   |----------|------|-----|---|
   | Shopee Reguler | 60.56 | 10.32 | 36 |
   | Shopee Food | 48.26 | 9.37 | 36 |

2. Uji Hipotesis:
   Uji yang digunakan  : Paired Sample T-Test
   Justifikasi         : Membandingkan 2 grup berpasangan (responden yang sama mencoba kedua skenario) dengan distribusi yang diasumsikan normal.
   Hasil               : p = 0.0000000076 (7.62e-09), T-Statistic = 7.5471

3. Keputusan:
   [x] H₀ ditolak → H₁ diterima
   [ ] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       : Terdapat perbedaan yang sangat signifikan pada tingkat usability antara alur Reguler dan Shopee Food.
   Practical significance: Penurunan skor dari 60.56 ke 48.26 sangat drastis (beda >12 poin SUS), menandakan antarmuka Shopee Food sangat membingungkan.
   Perbandingan literatur: Sesuai dengan teori *cognitive overload*, penambahan kompleksitas pada Super-App menurunkan kemudahan penggunaan.

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Structural Data Error | Kuesioner Shopee Food luput memasukkan Pertanyaan SUS ke-2 | Mengurangi presisi keakuratan skor riil untuk Shopee Food | Imputasi nilai konstan (3) digunakan agar SUS tetap bisa dikalkulasi |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : N/A (H0 ditolak)
   Boundary condition  : N/A
   Insight             : N/A
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | *2 (Shopee Reguler vs Shopee Food)* |
| Apakah data berpasangan (paired)? | *Ya (Within-subjects design)* |
| Apakah distribusi normal? (uji normalitas) | *Diasumsikan normal (N=36, Central Limit Theorem)* |
| **Uji yang dipilih:** | *Paired Sample T-Test* |
| **Justifikasi:** | *Paling tepat untuk membandingkan 2 perlakuan pada 1 kelompok sampel (Repeated measures).* |

**Effect size yang akan dilaporkan:** [ ] Cohen's d / [ ] Eta-squared / [x] T-Statistic (7.54)

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| A | 89.2 ± 1.5 | 10 |
| B | 87.8 ± 2.1 | 10 |

p = 0.045, Cohen's d = 0.74, CI 95% = [0.03, 2.77]

| Aspek | Interpretasi (Data Shopee Riil) |
|-------|-------------|
| Signifikansi statistik | *p = 7.62e-09 (Jauh lebih kecil dari 0.05) → Sangat Signifikan (H0 ditolak)* |
| Effect size | *T-Stat = 7.54 → Perbedaan mean sangat besar dan bukan karena kebetulan.* |
| Practical significance | *Skor 48.26 untuk Food berarti fitur ini butuh perombakan total (Not Acceptable).* |
| Hubungan ke RQ | *Menjawab RQ: Ya, integrasi super-app terbukti menurunkan usability.* |
| Perbandingan literatur | *Tumben dengan hukum Hick's Law: semakin banyak pilihan/fitur, user semakin lambat/bingung.* |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | *Contoh: Bukan gagal total — hipotesis tidak terdukung adalah temuan yang valid dan bisa menjadi kontribusi.* |
| Kemungkinan penyebab? | *Contoh: Metode baru menambah kompleksitas komputasi (+40% waktu) tanpa peningkatan F1 yang cukup — overhead tidak sebanding.* |
| Boundary condition? | *Contoh: Metode ini hanya efektif ketika data ≥ 10.000 record; di dataset kecil (<1.000), baseline lebih stabil.* |
| Insight yang bisa diambil? | *Contoh: Ada trade-off ukuran data vs kompleksitas — rekomendasikan hybrid approach yang adaptif berdasarkan ukuran dataset.* |
| Apakah layak dilaporkan? Mengapa? | *Contoh: Ya — negative result + boundary condition analysis adalah kontribusi riset yang diakui komunitas (ex: ACL, SIGIR). Mencegah riset duplikasi yang berulang.* |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| *Contoh: Statistical* | *Contoh: Hanya 5 run per skenario* | *Power test rendah* |
| | | |
| | | |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Failure dalam riset bukanlah kegagalan, melainkan temuan tentang *boundary condition* (batas kemampuan). Dalam riset ini, hilangnya Pertanyaan No. 2 pada form kuesioner adalah bentuk 'kegagalan' administrasi, namun justru mengajarkan saya pentingnya *pilot testing* (uji coba kuesioner) sebelum disebar secara masif.
> 
> Selain itu, dari segi analisis, menemukan keburukan (skor buruk pada Shopee Food) adalah temuan yang sangat valid untuk direkomendasikan perbaikannya kepada perusahaan.
