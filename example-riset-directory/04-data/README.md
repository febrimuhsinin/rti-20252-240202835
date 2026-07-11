# 04-data

Data mentah hasil pengumpulan kuesioner eksperimen System Usability Scale (SUS) — Shopee Reguler vs Shopee Food.

## Isi yang Diharapkan / Tersedia

- **`data_form.csv`**: Kumpulan respons riil (raw data) dari 36 responden valid (Gen Z) yang telah dikumpulkan via Google Form.
- **`dummy_data_sus.csv`**: Data sintetis (dummy) yang sempat dibuat saat tahap simulasi/pengujian *pipeline* algoritma sebelum pengumpulan data asli dilakukan.
- **`Kamus_Data.md`**: Dokumen penjelasan (*Data Dictionary*) yang merincikan struktur kolom-kolom dataset dan keterangan anomali pengumpulan data (misal: Q2 Shopee Food yang hilang).

## Catatan

Data di folder ini bersifat mentah (*raw*). Hasil olahan (perhitungan skor akhir, statistik deksriptif, dan uji Paired T-Test) akan disimpan atau diacu dari *script* analisis `analisis_sus.py` pada root repositori, serta didokumentasikan di Worksheet 14.
