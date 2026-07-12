# Tahap 4: Ekstraksi Hasil Skor SUS

**Status:** Selesai

---

## 1. Penangkapan Metrik Statistik

Setelah eksekusi `analisis_sus.py` pada Tahap 3, langkah krusial berikutnya adalah menangkap seluruh nilai kuantitatif (*stdout*) dan mendokumentasikannya ke dalam berkas statistik akhir. 

Hasil utama yang ditangkap adalah sebagai berikut:

### A. Statistik Deskriptif (Mean Scores)
- **Shopee Reguler (Baseline):** 60.56
- **Shopee Food (Intervensi):** 48.26

### B. Hasil Uji Hipotesis (T-Test)
- **T-Statistic:** 7.378
- **P-Value:** 7.62e-09

## 2. Interpretasi Sistematis SUS

Skor rata-rata SUS dievaluasi menggunakan rentang standar interpretasi (Brooke, 2013; Bangor et al., 2008):

| Skor SUS | Acceptability Range | Grade Scale | Adjective Rating |
|----------|---------------------|-------------|------------------|
| < 50     | Not Acceptable      | F           | Poor             |
| 50 - 70  | Marginal            | D / C       | OK / Fair        |
| > 70     | Acceptable          | B / A       | Good / Excellent |

Berdasarkan tabel di atas:
- Skor Shopee Reguler (60.56) berada di tingkat **Marginal (OK/Fair)**.
- Skor Shopee Food (48.26) jatuh ke tingkat **Not Acceptable (Poor)**.

Penurunan ekstrim lebih dari 12 poin ini diklasifikasikan sebagai degradasi pengalaman pengguna yang signifikan.

## 3. Visualisasi Data (Opsional)

Dalam beberapa kasus ekstraksi data, hasil ini juga dikonversi menjadi visualisasi berupa:
1. **Bar Chart:** Membandingkan nilai rata-rata (*Mean*) Shopee Reguler vs Shopee Food dengan grafik pilar secara berdampingan.
2. **Box Plot (Whisker Plot):** Untuk menunjukkan sebaran kuartil dan varians dari tiap demografi, sekaligus melihat titik *outlier*.

*(Catatan: Visualisasi untuk penelitian ini dirender menggunakan representasi teks atau menggunakan software eksternal).* 

## 4. Output Tahap 4

Hasil rekapitulasi data ini disimpan ke dalam satu dokumen ringkasan akhir: `06-output/hasil_analisis_sus.md`. Dokumen ini menjadi sumber acuan utama (sumber kebenaran kuantitatif) yang akan disalin/dikutip di bagian `Results` dan `Discussion` pada bab Manuskrip.
