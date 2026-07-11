# 05-kode

*Source code* implementasi pengolahan data riil dan uji statistik komparatif System Usability Scale (SUS).

## Struktur Skrip Python (`.py`)

```
05-kode/
├── analisis_sus.py             # Skrip UTAMA: Kalkulasi SUS riil, uji statistik Paired T-Test, dan ekspor markdown.
├── generate_dummy.py           # Skrip simulasi awal (menghasilkan CSV dummy sebelum pengumpulan data asli)
├── process_real.py             # Skrip purwarupa pengolahan data riil (sebelum anomali Q2 ditemukan)
└── process_real_corrected.py   # Skrip koreksi yang mengimplementasikan "Constant Imputation" (= 3) untuk mengatasi Missing Q2 Shopee Food.
```

## Deskripsi Modul Utama

**`analisis_sus.py`**: Merupakan otomasi utuh yang membaca dataset dari `04-data`, menghitung bobot nilai pertanyaan ganjil `(X-1)` dan genap `(5-X)`, lalu mengalikannya dengan `2.5`. Modul ini menggunakan *library* `scipy.stats.ttest_rel` untuk mengeluarkan P-Value yang memastikan perbedaan skor UX Shopee Reguler dan Shopee Food adalah signifikan secara statistik.
