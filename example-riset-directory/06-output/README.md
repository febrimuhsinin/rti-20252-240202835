# 06-output

Hasil olahan data dan statistik komparatif dari instrumen kuesioner **System Usability Scale (SUS)**.

Data di sini dihasilkan dan ditulis secara otomatis oleh *script* `05-kode/analisis_sus.py` setelah memproses data riil dari `04-data/data_form.csv`.

## Berkas Output Tersedia

| File | Isi |
|---|---|
| `hasil_analisis_sus.md` | Laporan akhir komprehensif yang berisi statistik deskriptif skor SUS (Mean, Min, Max) untuk Shopee Reguler dan Shopee Food, serta hasil P-Value dari Paired Sample T-Test. |

## Kesimpulan Eksekutif Output

Berdasarkan output dari pengujian statistik (*Paired T-Test*):
- **Skor Rata-Rata SUS Shopee Reguler:** 60.56 (Kategori: *Marginal* / Sedang)
- **Skor Rata-Rata SUS Shopee Food:** 48.26 (Kategori: *Not Acceptable* / Buruk)
- **P-Value (T-Test):** 7.621e-09

Karena P-Value jauh lebih kecil daripada tingkat signifikansi alpha (0.05), maka Hipotesis Nol (H0) ditolak. Hal ini membuktikan secara empiris bahwa ada **penurunan tingkat kegunaan (*usability*) yang signifikan secara statistik** saat pengguna Gen-Z menggunakan antarmuka Shopee Food dibandingkan alur belanja regulernya.
