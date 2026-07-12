# Tahap 2: Pra-pemrosesan Data dan Imputasi

**Status:** Selesai

---

## 1. Tinjauan Masalah (Missing Data)

Setelah data mentah diekspor dari Google Forms (`04-data/data_form.csv`), tinjauan awal menunjukkan ketiadaan nilai ( *null* / *missing value* ) pada kolom pertanyaan ke-2 (Q2) di set evaluasi **Shopee Food** akibat kesalahan konfigurasi form awal (seperti yang didokumentasikan di Tahap 1).

Pertanyaan Q2 adalah: *Saya merasa sistem ini terlalu rumit untuk digunakan.* (Pernyataan Negatif).
Karena instrumen SUS mengandalkan penjumlahan absolut dari 10 butir pertanyaan, kehilangan 1 butir akan mendistorsi skala total yang seharusnya berada di rentang 0-100.

## 2. Pemilihan Metode Mitigasi

Dalam proses *data cleaning*, terdapat beberapa opsi untuk mengatasi *missing values*:
1. **Listwise Deletion:** Menghapus semua sampel (baris responden) yang memiliki data tidak lengkap. 
   *Keputusan:* Ditolak. Karena semua responden tidak memiliki Q2 untuk Shopee Food, menghapus sampel berarti membatalkan seluruh penelitian (N menjadi 0).
2. **Mean Imputation:** Memasukkan nilai rata-rata dari responden lain.
   *Keputusan:* Ditolak. Karena data hilang secara terstruktur (semua responden tidak punya), tidak ada rata-rata aktual yang bisa dihitung untuk pertanyaan ini.
3. **Constant Imputation (Nilai Netral):** Mengganti *missing values* dengan nilai konstan *tengah* dari Skala Likert (yaitu **3**).
   *Keputusan:* **Diterima**. Mengimputasi skor netral 3 berarti responden dianggap "Ragu-ragu" atau netral terhadap kerumitan sistem. Meskipun hal ini menggeser *mean* distribusi secara statis, ini adalah metode kompromi terbaik agar 9 butir data asli lainnya tetap bisa diolah tanpa mendistorsi hasil eksperimen secara fluktuatif.

## 3. Implementasi Kode (Python)

Proses pra-pemrosesan diimplementasikan sepenuhnya menggunakan Python dengan pustaka `pandas`. 

Langkah-langkah yang dilakukan skrip `05-kode/analisis_sus.py`:
1. Membaca data mentah dari `data_form.csv`.
2. Melakukan *parsing* dan memisahkan set Reguler dan set Food.
3. Menyuntikkan kolom `Food_Q2` dengan nilai konstan `3` untuk seluruh baris.

```python
import pandas as pd

# Membaca data CSV
df = pd.read_csv('../04-data/data_form.csv')

# Melakukan Constant Imputation untuk butir yang hilang
df['Food_Q2'] = 3
```

## 4. Output Tahap 2

Hasil dari proses ini adalah *DataFrame* Pandas yang bersih, konsisten (keduanya memiliki 10 kolom skor Likert utuh), dan siap untuk diproses ke dalam tahap komputasi kalkulus SUS dan analisis komparatif uji hipotesis.
