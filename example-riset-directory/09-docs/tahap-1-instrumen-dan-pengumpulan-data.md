# Tahap 1: Persiapan Instrumen dan Pengumpulan Data

## Tujuan
Mengumpulkan tanggapan dari responden Generasi Z terkait pengalaman antarmuka Shopee Reguler dan Shopee Food menggunakan kuesioner kuantitatif baku.

## Langkah Implementasi
1. Pembuatan form kuesioner *System Usability Scale* (SUS) berisi 10 poin pertanyaan *Likert*.
2. Pembagian kuesioner secara digital (*Google Form*).
3. Pengumpulan 36 responden (*purposive sampling*) yang menggunakan aplikasi Shopee dalam kesehariannya.

## Struktur Data Mentah
Dataset dikumpulkan di `04-data/data_form.csv`. Format tabel meliputi:
- `Timestamp`
- `Umur` (Wajib rentang 18-25 tahun)
- 10 Butir SUS Shopee Reguler (Q1 - Q10)
- 9 Butir SUS Shopee Food (Q1, Q3 - Q10) -> *Catatan: Butir Q2 secara struktural hilang akibat kesalahan sistem form saat distribusi.*

## Hasil / Output
- Berkas primer `data_form.csv` tersimpan.
- Berkas `Kamus_Data.md` disusun untuk memetakan nama kolom agar mudah di-*parsing* oleh *Pandas* di tahap selanjutnya.
