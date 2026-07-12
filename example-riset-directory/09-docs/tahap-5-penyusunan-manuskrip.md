# Tahap 5: Penyusunan Manuskrip Jurnal Ilmiah

**Status:** Selesai

---

## 1. Standar Format dan Target Publikasi

Untuk memaksimalkan validitas akademis, penyusunan manuskrip mengadopsi standar **IEEE (Institute of Electrical and Electronics Engineers)**. Standar ini mencakup format penulisan 2 kolom, tata cara sitasi bernomor kurung siku (e.g., [1]), dan hierarki *heading* yang baku.

**Target Publikasi:** Jurnal terindeks Sinta 2 (e.g., Jurnal RESTI atau Telematika).

## 2. Struktur Modul Naskah (IMRAD)

Pengerjaan manuskrip dipecah ke dalam beberapa *file* Markdown yang terpisah (`07-manuskrip/`) untuk kemudahan revisi dan konsistensi matriks (*Consistency Matrix*).

1. `01-abstrak.md`: Ringkasan 1 paragraf (± 250 kata) mencakup *Problem*, *Method*, *Result*, dan *Conclusion*.
2. `02-pendahuluan.md`: Memaparkan *Introduction*, latar belakang fenomena *Super-App* di Indonesia, dan *Research Question* (RQ).
3. `03-tinjauan-pustaka.md`: Mengkaji literatur terdahulu (*Related Works*) yang berfokus pada SUS, Hick's Law, dan evaluasi *e-commerce* lokal.
4. `04-metodologi.md`: Menjelaskan desain pengujian *Within-Subjects*, demografi partisipan, dan tahapan *Constant Imputation* untuk data *missing value*.
5. `05-hasil-analisis.md`: Melaporkan secara objektif hasil pengujian (T-Test) dan perbandingan mean (60.56 vs 48.26).
6. `06-kesimpulan.md`: Merangkum validasi hipotesis, memberikan rekomendasi desain *UI/UX*, dan menyebutkan *Future Works*.
7. `07-daftar-pustaka.md`: Berisi 15 sitasi primer dengan minimal 10 jurnal nasional/internasional mutakhir dari **Google Scholar**.

## 3. Integrasi dan Validasi Kualitas (*Scientific Writing*)

Manuskrip dievaluasi ulang berdasarkan *Writing Quality Triad*:
- **Clarity:** Tidak ada penggunaan jargon UX yang berlebihan tanpa penjelasan pendamping.
- **Precision:** Pelaporan P-Value tidak sekadar "signifikan", tetapi disertakan angka absolutnya (p < 0.05, spesifiknya 7.62e-09).
- **Conciseness:** Menghilangkan frasa redundan demi memaksimalkan kepadatan informasi.

## 4. Output Tahap 5

Sebuah berkas master **`naskah-jurnal.md`** yang telah merangkum ketujuh modul di atas. Dokumen ini dapat langsung disalin (*copy-paste*) ke dalam *template* Microsoft Word atau *LaTeX* milik penyelenggara jurnal/konferensi.
