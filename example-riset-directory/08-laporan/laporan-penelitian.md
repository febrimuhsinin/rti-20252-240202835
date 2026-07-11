# Laporan Penelitian

**Judul:** Evaluasi Dampak Usability Integrasi Layanan Pesan-Antar Makanan pada Super-App E-Commerce: Studi Kasus Shopee Reguler dan Shopee Food

**Peneliti:** Febri Muhsinin (240202835)
**Target Publikasi:** Sinta 2 (Jurnal RESTI/Telematika) atau Scopus Q3–Q4
**Status Penelitian:** Tahap 1–4 selesai; Tahap 5 (draf naskah jurnal) selesai disusun ([../07-manuskrip/](../07-manuskrip/))

---

## 1. Ringkasan Eksekutif

Penelitian ini mengevaluasi secara empiris dampak dari *feature bloat* terhadap tingkat kegunaan (*usability*) pada aplikasi Shopee, khususnya dengan membandingkan layanan utama (Shopee Reguler) dengan layanan sekunder (Shopee Food). Evaluasi dilakukan melalui pendekatan eksperimen terkontrol *Within-Subjects Design* yang melibatkan 36 partisipan dari Generasi Z. Pengumpulan data dilakukan menggunakan kuesioner standar *System Usability Scale* (SUS) untuk kedua alur layanan, dilanjutkan dengan komputasi statistik *Paired Sample T-Test* menggunakan skrip Python.

**Temuan utama:**

- Integrasi fitur sekunder terbukti memicu **beban kognitif berlebih** yang merusak kenyamanan visual dan navigasi pengguna.
- Terdapat **penurunan skor yang tajam** pada Shopee Food (48.26 / *Not Acceptable*) dibandingkan dengan Shopee Reguler (60.56 / *Marginal*).
- Pengujian signifikansi mengonfirmasi bahwa selisih skor tersebut (12.30 poin) terjadi secara **sangat signifikan** (*P-Value* = 7.62e-09 < 0.05).

Seluruh data mentah, skrip komputasi analisis, dan draf naskah jurnal tersedia di repositori ini (lihat §7 Lampiran untuk peta artefak).

---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang

Dalam ekosistem digital modern, perusahaan e-commerce sering kali mengekspansi layanannya menjadi *super-app*. Shopee mengintegrasikan dompet digital, *mini-games*, hingga layanan pesan-antar makanan (Shopee Food) ke dalam satu wadah aplikasi. Meskipun strategi ini menjaga retensi pengguna, penggabungan lusinan fitur dalam ruang layar terbatas berisiko tinggi memicu *feature bloat*. Dalam perspektif HCI, antarmuka yang dipenuhi oleh opsi navigasi yang terlalu kompleks memicu *Extraneous Cognitive Load* dan memperlambat pengambilan keputusan (*Hick's Law*).

### 2.2 Rumusan Masalah

1. Apakah integrasi layanan sekunder (Shopee Food) ke dalam aplikasi utama e-commerce memicu penurunan tingkat kegunaan (*usability*) secara signifikan dibandingkan dengan berbelanja reguler?
2. Seberapa besar perbedaan skor kelayakan SUS antara kedua skenario alur penggunaan tersebut?

### 2.3 Tujuan Penelitian

Mengevaluasi secara kuantitatif skor *usability* dari layanan utama dan sekunder, serta membuktikan secara empiris ada atau tidaknya indikasi *cognitive overload* yang signifikan secara statistik menggunakan komparasi instrumen baku *System Usability Scale* (SUS).

---

## 3. Metodologi dan Pelaksanaan

Penelitian dilaksanakan dalam 5 tahap. Bagian ini merangkum implementasi setiap tahap dalam repositori ini.

### 3.1 Tahap 1 — Perancangan Proposal dan Literatur

**Status: Selesai.** Merumuskan latar belakang, permasalahan desain UI/UX, serta komparasi *related work* yang relevan tentang *Super-app Usability*. Deliverable: Direktori `01-proposal` dan kerangka komparatif di `02-literatur`.

### 3.2 Tahap 2 — Persiapan Instrumen dan Pengumpulan Data

**Status: Selesai.** Instrumen *System Usability Scale* disebar melalui Google Form kepada 36 mahasiswa dan pekerja lepas Generasi Z. Partisipan mengevaluasi simulasi: belanja barang (Reguler) dan pesan makanan (Food).

Output: `04-data/data_form.csv` dan `04-data/Kamus_Data.md`.

### 3.3 Tahap 3 — Pra-pemrosesan dan Komputasi Analisis

**Status: Selesai.** Skrip analisis statistik dibangun menggunakan Python (`05-kode/analisis_sus.py`). 

**Verifikasi komputasi:**
- Imputasi: Butir Q2 (Sistem rumit) Shopee Food yang hilang dari instrumen lapangan ditangani statis dengan disuntik nilai netral (3) secara terprogram.
- Penilaian SUS: Transformasi *Likert* (X-1 ganjil, 5-X genap) dikalikan konstanta 2.5 secara massal dari baris ke 3-38 di file CSV.
- Uji Hipotesis: Eksekusi `scipy.stats.ttest_rel` terhadap kedua kelompok vektor nilai SUS.

### 3.4 Tahap 4 — Ekstraksi Hasil

**Status: Selesai.** Hasil output konsol dari komputasi skrip Python diabadikan di dalam dokumentasi. Deliverable: `06-output/hasil_analisis_sus.md`.

### 3.5 Tahap 5 — Penyusunan Manuskrip Jurnal

**Status: Selesai.** Draf konten naskah telah dirakit di `07-manuskrip/` dan dipecah menjadi 8 file terstruktur (Abstrak, Pendahuluan, Tinjauan Pustaka, Metodologi, Hasil, Kesimpulan, dan Daftar Pustaka format IEEE standar) agar siap disalin-tempel ke *template* universitas.

---

## 4. Hasil Penelitian

Ringkasan hasil komputasi (detail lengkap: [../06-output/hasil_analisis_sus.md](../06-output/hasil_analisis_sus.md) dan [../07-manuskrip/05-hasil-analisis.md](../07-manuskrip/05-hasil-analisis.md)).

### 4.1 Statistik Deskriptif Skor SUS

| Skenario Pengujian | Rata-rata Skor SUS | Kategori Bangor (2008) | Minimum | Maksimum |
|---|---|---|---|---|
| **Shopee Reguler** | 60.56 | Marginal | 40.0 | 82.5 |
| **Shopee Food** | 48.26 | Not Acceptable | 30.0 | 80.0 |

### 4.2 Uji Hipotesis Komparatif (Paired T-Test)

| Kondisi Eksperimen | Mean Difference | N | P-Value |
|---|---|---|---|
| Shopee Reguler vs Food | 12.30 poin | 36 | 7.621e-09 |

### 4.3 Interpretasi Singkat

1. Secara absolut, layanan sekunder Shopee Food memburuk di bawah batas standar kegunaan (*Not Acceptable*).
2. *P-Value* (7.62e-09) jauh di bawah standar probabilitas *alpha* (0.05), yang berarti penurunan skor ini memiliki signifikansi statistik yang mutlak (Bukan sebuah kebetulan).
3. Integrasi *super-app* Shopee memicu beban kognitif yang mematahkan kelancaran penggunaan aplikasi dasar bagi penggunanya.

---

## 5. Kendala dan Catatan Lapangan

- **Kehilangan Butir Instrumen:** Butir Q2 khusus Shopee Food tidak terdaftar (lupa di-*input*) ke *Google Form*. Solusi yang diambil adalah tidak membuang data partisipan (N=36), melainkan menyuntikkan nilai penyeimbang/netral (3) di tahap *coding* (disebut teknik *Constant Imputation*).
- **Isolasi Lingkungan Python:** Mengingat hanya dibutuhkan komputasi saintifik standar, pengguna cukup menyediakan interpreter Python 3.8+ dan modul `scipy` serta `pandas` lokal. Tidak ada kendala sistem.

---

## 6. Kesimpulan dan Saran

Transisi platform e-commerce konvensional menjadi *super-app* yang serba ada terbukti memberikan kerugian fungsional yang signifikan pada sisi kebergunaan antarmuka (*Usability*). Lebar kesenjangan UX ini secara akademis membuktikan bahwa penjejalan fitur yang agresif (*feature bloat*) secara langsung mengekskalasi beban memori kognitif pengguna (*Hick's Law*).

**Saran:** Sangat disarankan bagi tim UI/UX perusahaan *super-app* untuk menerapkan metode mitigasi *Progressive Disclosure*, atau melakukan separasi layanan berat menjadi aplikasi independen *(standalone app)*.

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder | Isi | Status |
|---|---|---|
| [01-proposal/](../01-proposal/) | Proposal riset dan template dasar. | Selesai |
| [02-literatur/](../02-literatur/) | Matriks dan referensi literatur. | Selesai |
| [03-teori/](../03-teori/) | Penjabaran teori SUS (Tidak dipakai). | Selesai |
| [04-data/](../04-data/) | Dataset observasi (`data_form.csv`) & Kamus Data. | Selesai |
| [05-kode/](../05-kode/) | Skrip algoritma analisis Python (`analisis_sus.py`). | Selesai |
| [06-output/](../06-output/) | Rekapitulasi hasil uji T-Test dan skor SUS. | Selesai |
| [07-manuskrip/](../07-manuskrip/) | Draf publikasi ilmiah lengkap 8 Bab siap *publish*. | Selesai |
| [08-laporan/](../08-laporan/) | Laporan akhir (dokumen ini). | Selesai |

**Cara Reproduksi Komputasi:**

```bash
# Tahap 3: Mengeksekusi pipeline analisis SUS
cd 05-kode
python analisis_sus.py
```
