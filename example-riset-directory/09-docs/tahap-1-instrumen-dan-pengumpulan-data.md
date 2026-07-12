# Tahap 1: Persiapan Instrumen dan Pengumpulan Data

**Status:** Selesai

---

## 1. Desain Instrumen Penelitian

Penelitian ini menggunakan instrumen baku **System Usability Scale (SUS)** yang dikembangkan oleh John Brooke (1996). Instrumen ini dipilih karena kemampuannya dalam memberikan evaluasi kegunaan (*usability*) secara cepat dan reliabel meskipun dengan ukuran sampel yang relatif kecil. 

Kuesioner disusun dalam Bahasa Indonesia agar mudah dipahami oleh responden lokal. Terdapat 10 pernyataan (5 positif, 5 negatif) yang harus dijawab menggunakan Skala Likert 1 hingga 5 (1 = Sangat Tidak Setuju, 5 = Sangat Setuju).

### Daftar 10 Pernyataan SUS:

1. Saya pikir saya akan menggunakan fitur/sistem ini lagi.
2. Saya merasa sistem ini terlalu rumit untuk digunakan. *(Pernyataan Negatif)*
3. Saya merasa sistem ini mudah digunakan.
4. Saya merasa saya membutuhkan bantuan dari orang teknis untuk dapat menggunakan sistem ini. *(Pernyataan Negatif)*
5. Saya menemukan bahwa berbagai fungsi dalam sistem ini terintegrasi dengan baik.
6. Saya merasa ada terlalu banyak ketidakkonsistenan dalam sistem ini. *(Pernyataan Negatif)*
7. Saya membayangkan bahwa kebanyakan orang akan belajar menggunakan sistem ini dengan sangat cepat.
8. Saya merasa sistem ini sangat canggung/merepotkan untuk digunakan. *(Pernyataan Negatif)*
9. Saya merasa sangat percaya diri menggunakan sistem ini.
10. Saya harus belajar banyak hal sebelum saya bisa menggunakan sistem ini. *(Pernyataan Negatif)*

Instrumen ini digunakan dua kali dalam satu sesi pengujian (*Within-Subjects Design*):
- **Sesi A:** Evaluasi usability aplikasi utama (Shopee Reguler).
- **Sesi B:** Evaluasi usability fitur tambahan (Shopee Food).

## 2. Kriteria dan Pemilihan Responden

Teknik pengambilan sampel yang digunakan adalah **Purposive Sampling** dengan kriteria inklusi spesifik:
- **Demografi:** Generasi Z (usia 18 - 25 tahun).
- **Pengalaman:** Aktif menggunakan aplikasi Shopee dan pernah melakukan transaksi di layanan Shopee Food minimal 1 kali dalam sebulan terakhir.
- **Ukuran Sampel:** 36 Responden. Jumlah ini dianggap cukup representatif untuk evaluasi SUS (Nielsen merekomendasikan N>12 untuk hasil kuantitatif yang solid pada studi UX).

## 3. Prosedur Pengumpulan Data

1. **Digitalisasi Form:** Kuesioner dipindahkan ke *platform* survei daring (Google Forms) untuk memudahkan penyebaran secara jarak jauh (*remote*).
2. **Informed Consent:** Pada halaman pertama form, responden diberikan penjelasan mengenai tujuan penelitian dan jaminan kerahasiaan data.
3. **Distribusi:** Tautan survei didistribusikan melalui grup komunikasi mahasiswa dan media sosial selama periode 1 minggu.
4. **Pengawasan Mutu:** Data yang masuk ditinjau untuk mendeteksi *straight-lining* (menjawab nilai yang sama terus-menerus tanpa membaca).

## 4. Kendala Pengumpulan (Insiden Hilangnya Q2)

Selama fase pengumpulan data, terjadi kendala teknis (kesalahan konfigurasi form) di mana pertanyaan ke-2 (Q2) untuk modul **Shopee Food** tidak tersimpan dalam *database* tanggapan, sehingga menghasilkan *missing values* pada satu kolom tersebut di seluruh baris responden.

Masalah ini dicatat secara resmi sebagai limitasi instrumen, dan penanganannya (imputasi data) akan didokumentasikan sepenuhnya pada **Tahap 2: Pra-pemrosesan Data dan Imputasi**.

## 5. Output Tahap 1

Hasil akhir dari tahap ini adalah dataset mentah berformat CSV yang disimpan di: `04-data/data_form.csv`. Dataset ini berisi *timestamp*, data usia responden, dan 19 kolom skor mentah Likert (10 untuk Reguler, 9 untuk Food).
