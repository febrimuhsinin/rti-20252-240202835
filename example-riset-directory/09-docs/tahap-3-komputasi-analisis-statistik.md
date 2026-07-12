# Tahap 3: Komputasi Analisis Statistik

## Tujuan
Menghitung nilai *usability* berstandar SUS untuk setiap skenario (*baseline* dan *intervensi*), kemudian memvalidasi signifikansi perbedaan antara keduanya secara objektif.

## Algoritma Komputasi (Python)
1. **Konversi Likert**: 
   - Untuk pernyataan Ganjil (Positif): Skor aktual dikurangi 1 `(X - 1)`.
   - Untuk pernyataan Genap (Negatif): 5 dikurangi skor aktual `(5 - X)`.
2. **Kalkulasi SUS**:
   - Jumlah dari seluruh 10 pernyataan (bernilai 0-40) dikalikan konstanta *2.5*.
   - Menghasilkan skala absolut (0-100).
3. **Uji Hipotesis (*Paired Sample T-Test*)**:
   - Digunakan library `scipy.stats.ttest_rel` karena sifat data yang *within-subjects* (satu populasi yang sama mengevaluasi dua layanan berurutan).

## Hasil / Output
Skrip utama `analisis_sus.py` di folder `05-kode/` yang mengotomatisasi seluruh alur ini, mulai dari *read CSV* hingga menampilkan metrik keluaran ke layar konsol terminal.
