# Tahap 2: Pra-pemrosesan Data dan Imputasi

## Tujuan
Menyiapkan *raw dataset* sebelum dianalisis dengan algoritma skor SUS, terutama menangani kelengkapan matriks pada baris yang kehilangan butir pertanyaan.

## Masalah yang Dihadapi
Pada skenario pengujian *Shopee Food*, pertanyaan kedua (Q2: *Saya merasa sistem ini terlalu rumit untuk digunakan*) hilang/tidak terunggah dengan benar di *Google Form* saat pengumpulan data kepada responden, sehingga menyisakan kolom *null* atau *missing value*.

## Mitigasi Python
- **Solusi Ditolak**: Menghapus seluruh sampel (36 partisipan). Tidak efisien dan meniadakan ukuran sampel valid.
- **Solusi Diterima**: Menulis kode di `05-kode/analisis_sus.py` untuk menyuntikkan nilai statis netral `3` (Skala Likert tengah) ke seluruh kolom Q2 Shopee Food.
  
```python
# Snippet penanganan (Imputasi)
df['Food_Q2'] = 3
```

## Hasil / Output
Dataset yang telah melalui tahap pra-pemrosesan dan siap dikonversi menjadi unit ukur baku (0-100).
