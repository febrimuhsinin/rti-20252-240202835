# Tahap 3: Komputasi Analisis Statistik

**Status:** Selesai

---

## 1. Konversi Skor SUS

Data Likert (1-5) tidak dapat langsung dijumlahkan menjadi skala persentase. Kalkulasi System Usability Scale (SUS) membutuhkan konversi matematis berdasarkan sifat pernyataannya (positif atau negatif).

### Aturan Konversi (Brooke, 1996):
- **Untuk Pernyataan Positif (Ganjil - Q1, Q3, Q5, Q7, Q9):**
  Skor = Jawaban Responden - 1
- **Untuk Pernyataan Negatif (Genap - Q2, Q4, Q6, Q8, Q10):**
  Skor = 5 - Jawaban Responden

Setelah dikonversi, nilai kontribusi tiap butir pertanyaan akan berada di rentang `0` hingga `4`.

### Kalkulasi Skor Akhir:
Total jumlah skor konversi dari ke-10 butir pertanyaan (maksimal 40) dikalikan dengan konstanta **2.5**. Hasil akhir akan berupa angka absolut dengan rentang **0 hingga 100**.

Diimplementasikan di Python:
```python
def calculate_sus(row):
    score = 0
    for i in range(1, 11):
        val = row[f'Q{i}']
        if i % 2 != 0:  # Ganjil (Positif)
            score += (val - 1)
        else:           # Genap (Negatif)
            score += (5 - val)
    return score * 2.5
```

## 2. Pengujian Hipotesis

Karena penelitian ini menggunakan desain *Within-Subjects* (36 orang yang sama mengevaluasi Shopee Reguler lalu Shopee Food), maka uji statistik yang paling tepat digunakan adalah **Paired Sample T-Test**.

### Rumusan Hipotesis:
- **H0:** Tidak ada perbedaan signifikansi *usability* antara Shopee Reguler dan Shopee Food.
- **H1:** Terdapat penurunan *usability* yang signifikan akibat integrasi Shopee Food.

### Level Signifikansi (Alpha):
Nilai alpha ($\alpha$) ditetapkan sebesar **0.05**. Jika *P-Value* < 0.05, maka H0 ditolak secara mutlak.

### Eksekusi di Python:
Pengujian ini otomatis dihitung oleh pustaka *SciPy*.
```python
from scipy import stats

t_stat, p_value = stats.ttest_rel(sus_reguler_scores, sus_food_scores)
```

## 3. Output Tahap 3

Skrip Python `analisis_sus.py` menggabungkan proses tahap 2 dan tahap 3 menjadi satu *pipeline* eksekusi yang *reproducible*. Ketika dijalankan, program akan menghasilkan metrik *Mean*, *Max*, *Min*, dan nilai *P-Value* ke terminal.
