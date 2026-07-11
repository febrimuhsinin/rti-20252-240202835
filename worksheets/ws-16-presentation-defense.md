# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : ____ (target: 10-12 konten + title/closing)
  Time per slide : ~2 min
  Total time     : ____ menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title       |        | 30s   |
| 2 | Problem     |        | 2min  |
| 3 | Gap + RQ    |        | 2min  |
| ..|             |        |       |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  |                     |               |
| Gap      |                     |               |
| Method   |                     |               |
| Results  |                     |               |
| Generalization |               |               |

Latihan:
  Latihan 1: [tanggal] — [catatan timing & feedback]
  Latihan 2: [tanggal] — [catatan timing & feedback]
  Latihan 3: [tanggal] — [catatan timing & feedback]
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Judul & Latar Belakang (Transisi E-Commerce ke Super-app) | Title slide, Screenshot UI Shopee yang penuh fitur | 1 min |
| 2 | Problem (Potensi *Cognitive Overload* pengguna) | Highlight fitur yang menumpuk di beranda | 2 min |
| 3 | RQ & Hipotesis (Apakah fitur Food lebih sulit dipakai?) | Teks ringkas RQ & H1 | 1 min |
| 4 | Metode Eksperimen (Within-subject SUS, N=36 Gen Z) | Diagram Alur (Reguler -> Food) & Tabel Demografi | 2 min |
| 5 | Hasil Statistik Utama (Skor rata-rata) | Tabel Skor SUS (60.56 vs 48.26) & P-Value | 2 min |
| 6 | Visualisasi Perbandingan Signifikansi | Bar Chart dengan *Error Bar* / Interval | 2 min |
| 7 | Interpretasi (Fitur Food *Not Acceptable*) | Insight/kesimpulan penurunan UX yang ekstrem | 2 min |
| 8 | Limitasi Penelitian (Hilangnya Butir Q2 Food) | Teks jujur tentang metode *Constant Imputation* (3) | 1 min |
| 9 | Kesimpulan & Saran (H1 Diterima, butuh Re-design) | Bullet points ringkas rekomendasi UX UI | 1 min |

**Total waktu estimasi:** 14 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | *Method* | Mengapa Anda menggunakan instrumen SUS, bukan Usability Testing *task-based* (mencatat waktu penyelesaian *task*)? | SUS adalah standar industri yang tervalidasi reliabel untuk evaluasi cepat | Literatur Brooke (1996) dan adopsi luas di industri UX | Riset ini berfokus pada persepsi subjektif (*satisfaction & ease of use*) yang dapat disebar secara *remote* dalam waktu sempit, bukan efisiensi motorik. |
| 2 | *Method (Limitasi)* | Mengapa ada Pertanyaan No.2 yang hilang di form Shopee Food? Apakah datanya cacat? | Data tetap valid karena telah dimitigasi dengan *Constant Imputation* | Jumlah responden (N=36) tetap utuh, dan skor netral (3) meminimalisir deviasi | Kesalahan teknis *human error* di Google Form diatasi secara matematis agar 10 butir pertanyaan tetap lengkap tanpa mendistorsi secara ekstrem arah nilai yang ada. |
| 3 | *Generalization* | Mengapa Anda HANYA fokus pada responden Gen-Z usia 18-25 tahun? | Untuk menjaga kontrol variabel (*internal validity*) | Mayoritas responden berstatus mahasiswa yang terbiasa menggunakan aplikasi e-commerce sehari-hari | Jika kelompok Gen-Z (yang notabene secara literasi digital sangat adaptif) saja merasa Shopee Food membingungkan, maka kelompok demografi yang lebih tua kemungkinan besar akan merasa jauh lebih bingung. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | Jika Shopee Food jelek (48.26), mengapa orang masih menggunakannya? | "Karena terikat oleh ekosistem promo (diskon ongkir) yang menyatu dengan saldo Shopeepay mereka, bukan karena kemudahan UI-nya." | [x] Direct [x] Data-based [x] Honest |
| 2 | Kenapa skor Reguler juga cukup rendah (60.56)? | "Karena beranda reguler Shopee saat ini sudah memuat terlalu banyak *mini-games* dan layanan sekunder, berbeda dengan desain aslinya dulu." | [x] Direct [x] Data-based [x] Honest |
| 3 | Apakah imputasi nilai 3 untuk Q2 Food tidak mengubah hasil statistik? | "Tentu sedikit mengubah *mean* absolut, namun tidak mengubah signifikansi tren P-Value, karena selisihnya sudah telak (>12 poin). Hal ini sudah diakui sebagai limitasi di laporan." | [x] Direct [x] Data-based [x] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Pertanyaan validitas instrumen terkait kuesioner yang cacat (hilangnya Q2) di Google Form, karena ini menyangkut kealpaan peneliti sendiri.

**Apa yang perlu disiapkan lebih baik:**
> Menghadapi dewan penguji dengan bersikap *Honest* (jujur) dan menyiapkan rujukan *paper* statistik yang melegitimasi penggunaan metode Imputasi Data untuk *missing values* struktural.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Menyadari bahwa riset ilmiah itu seperti rantai (*chain*). Satu kealpaan kecil di fase awal (salah seting Google Form di WS-10) akan berdampak sangat besar ke *preprocessing* (WS-13) dan memengaruhi derajat kepercayaan hasil akhir (WS-14). Namun, riset tidak menuntut kesempurnaan melainkan transparansi. Mengaku salah di bagian *Failure Analysis / Limitation* justru membuat laporan menjadi lebih kokoh dan akademis.

**Yang akan selalu diterapkan:**
> Melakukan **Pilot Testing** (uji coba kuesioner ke 2-3 orang) sebelum secara masif menyebarkannya ke grup publik. Hal ini guna memastikan struktur kolom dan logika formulir sudah benar 100%.
