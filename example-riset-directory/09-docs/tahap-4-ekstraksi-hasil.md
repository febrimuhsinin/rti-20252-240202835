# Tahap 4: Ekstraksi Hasil Skor SUS

## Tujuan
Menyimpan dan mengkonsolidasikan *output* komputasi Python (T-Test dan mean skor) ke dalam sebuah format dokumen yang mudah disalin ke dalam naskah publikasi.

## Langkah Implementasi
1. Menjalankan skrip `analisis_sus.py`.
2. Menangkap luaran (stdout) dari terminal yang mencakup metrik *Min*, *Max*, *Mean*, dan *P-Value* dari komparasi SUS.
3. Menulis ulang angka-angka tersebut secara rapi ke dalam dokumen ringkasan akhir (`06-output/hasil_analisis_sus.md`).

## Hasil / Output
Dokumen `hasil_analisis_sus.md` yang memuat bukti absolut penurunan skor kegunaan dari 60.56 (Shopee Reguler) menjadi 48.26 (Shopee Food) secara signifikan, membuktikan bahwa hipotesis awal mengenai *feature bloat* terbukti kebenarannya.
