# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah terdapat perbedaan skor System Usability Scale (SUS) yang signifikan antara alur transaksi belanja umum dengan alur transaksi pada fitur Shopee Food bagi pengguna Generasi Z?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Variabel       | IV   | Instruksi Skenario Tugas    | Mengarahkan user ke alur yang berbeda via teks instruksi (Reguler ↔ Food), dibuat 2 versi (Form A & Form B).                      |
| Alur Transaksi | DV   | SUS Likert Scale Section |Kalkulasi otomatis matriks dari 10 pertanyaan skala Likert 1-5 yang diisi sesaat setelah tugas selesai.         |
| Skor Usability | CV   | Screening & Persetujuan Awal     | Pertanyaan wajib di awal form untuk menyaring usia Gen Z, memvalidasi koneksi stabil, & kondusivitas ruang.|

4 Prinsip Desain:
  [x] Traceability — Setiap skor SUS yang masuk bisa ditelusuri dari bagian skenario mana ia dikerjakan.
  [x] Variable Isolation — IV (Alur Shopee/Food) dipisah per halaman (section) tanpa mencampuradukkan CV.
  [x] Measurement Integration — Perekaman data Likert otomatis masuk ke spreadsheet.
  [x] Reproducibility — Form pengujian, skenario, dan syarat responden didokumentasikan sehingga bisa diulang siapapun.

Experimental Setup:
  Input data     : 2 set panduan skenario tugas (Skenario Belanja Reguler vs Skenario Shopee Food).
  Parameter      : Responden Generasi Z (N=36+), Pengalaman > 1 tahun, Mahasiswa aktif, Koneksi Internet Stabil.
  Output format  : Dataset Spreadsheet (Excel/CSV) berisi profil screening responden dan raw data Skor SUS.
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Bagaimana efisiensi alur transaksi Shopee Food dibandingkan dengan alur belanja reguler bagi pengguna yang sudah terbiasa dengan ekosistem Shopee?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| *Jenis Fitur* | *IV* | *Instruksi Skenario (Google Form Section)* | *Mengarahkan responden untuk simulasi Reguler vs Food (Counterbalancing).* |
| *Skor Usability* | *DV* | *SUS Matrix Collector* | *Perhitungan matematis dari jawaban 10 item kuesioner skala Likert (1-5).* |
| *Profil & Lingkungan* | *CV* | *Halaman Screening Kualifikasi* | *Mengunci kriteria responden (Gen Z) dan mewajibkan centang konfirmasi jaringan/perangkat.* |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | *✅* | *Respons SUS Sesi 1 secara pasti merekam kepuasan Alur Reguler, dan SUS Sesi 2 merekam Alur Food.* |
| Modularity | *✅* | *Urutan section Skenario Reguler dan Skenario Food bisa ditukar (Form A & Form B) tanpa mengubah pertanyaan SUS-nya.* |
| Controllability | *✅* | *Meskipun remote testing, responden dikunci oleh pertanyaan "Wajib Isi" terkait kesesuaian perangkat dan lingkungan sebelum mulai.* |
| Measurability | *✅* | *Data kuantitatif (skor 1-5) otomatis terkumpul di Google Sheets untuk langsung dihitung dengan formula baku SUS.* |

**Prinsip mana yang paling sulit dipenuhi?** Controllability (Kontrol Variabel).
**Strategi untuk mengatasinya:**
> Karena menggunakan Remote Testing, kontrol dilakukan secara Self-Reported. Responden diwajibkan menyetujui syarat kelayakan perangkat dan mengonfirmasi bahwa mereka menggunakan jaringan internet yang stabil di halaman pertama kuesioner sebelum diizinkan membaca instruksi tugas.

---

## Latihan 3 — Ablation Study Planning

Dalam konteks UX, ablation study dilakukan dengan melepas atau mematikan fitur spesifik untuk melihat dampaknya terhadap skor usability.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Alur Skenario | Hasil yang Diharapkan |
|---------|---------------|----------------------|
| Control | *✅ Alur Belanja Reguler* | *Skor SUS tinggi (baseline) karena partisipan sudah sangat terbiasa dengan alur utama ini.* |
| Treatment | *✅ Alur Shopee Food* | *Skor SUS lebih rendah akibat kompleksitas navigasi tambahan pada sub-fitur.* |
| – | *-* | *-* |
| – | *-* | *-* |

*(Catatan: Riset ini dikunci pada desain Uji Komparatif/Comparison, sehingga tabel dimodifikasi dari format standar Ablation).*

**Komponen mana yang diprediksi paling berkontribusi?** Kompleksitas Navigasi (Information Overload).
**Mengapa?**
> Karena penambahan fitur baru seperti Shopee Food di dalam aplikasi yang sama seringkali menumpuk antarmuka secara berlebihan. Hal ini meningkatkan beban kognitif pengguna saat melakukan transisi dari kebiasaan belanja reguler menuju pemesanan makanan.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko utamanya adalah kebingungan dalam mengisolasi variabel (Variable Confounding). Jika responden hanya diinstruksikan secara bebas "Coba pakai aplikasi Shopee secara keseluruhan lalu nilai", peneliti tidak akan pernah tahu fitur spesifik mana yang sebenarnya menyebabkan kenaikan atau penurunan skor usability. Apakah karena alur pembayarannya yang rumit, warnanya, atau karena dark patterns di Shopee Food?

Arsitektur yang modular (memecah tugas menjadi Skenario Belanja Reguler vs Skenario Shopee Food secara terpisah di dalam instrumen pengujian) sangat penting untuk melakukan Variable Isolation. Hal ini memastikan bahwa penurunan skor yang terjadi memang benar-benar disebabkan oleh manipulasi arsitektur antarmuka (dark patterns) pada sub-fitur tersebut, bukan karena kelelahan atau gangguan lain, sehingga validitas internal eksperimen tetap terjaga.
> ___________________________________________________
