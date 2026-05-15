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
| Variabel       | IV   | Task Scenario Module        | Toggle antara Skenario A (Belanja Reguler) dan Skenario B (Shopee Food).                      |
| Alur Transaksi | DV   | Digital Questionnaire (SUS) | Pengisian kuesioner otomatis setelah tugas selesai menggunakan alat survei digital.         |
| Skor Usability | CV   | User Screening Filter       | Penentuan kriteria responden (Gen Z, minimal 1 tahun penggunaan Shopee) di awal pendaftaran.|

4 Prinsip Desain:
  [x] Traceability — Setiap tugas dalam skenario dirancang untuk memicu instrumen penilaian SUS tertentu.
  [x] Variable Isolation — Perbedaan hanya terletak pada alur fitur; antarmuka dasar (navbar, header) tetap konstan.
  [x] Measurement Integration — Sistem survei merekam waktu penyelesaian tugas secara otomatis bersamaan dengan input SUS.
  [x] Reproducibility — Skenario tugas didokumentasikan dalam format teks yang bisa diulang oleh peneliti lain.

Experimental Setup:
  Input data     : 2 set skenario tugas (Belanja Barang vs Pesan Makan).
  Parameter      : Responden Gen Z (N=30+), Perangkat Mobile (iOS/Android).
  Output format  : Dataset CSV berisi Skor SUS per responden dan Time on Task.
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Bagaimana efisiensi alur transaksi Shopee Food dibandingkan dengan alur belanja reguler bagi pengguna yang sudah terbiasa dengan ekosistem Shopee?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| *Jenis Fitur* | *IV* | *Interactive Prototype (Figma) / Task Set* | *Mengarahkan user ke alur yang berbeda (Reguler ↔ Food).* |
| *Skor Usability* | *DV* | *SUS Matrix Collector* | *Kalkulasi otomatis dari 10 pertanyaan skala Likert.* |
| *Tingkat Kesalahan* | *DV2* | *Error Log Tracker* | *Mencatat berapa kali user salah menekan tombol (miss-click).* |
| *Jenis Koneksi* | *CV* | *Fixed Network Environment* | *Pengujian dilakukan pada jaringan Wi-Fi yang sama untuk semua user.* |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | *✅* | *Setiap tombol di prototipe terkait dengan success rate yang menjadi bagian dari efektivitas (aspek SUS).* |
| Modularity | *✅* | *Modul kuesioner terpisah dari modul skenario tugas; bisa diganti dengan kuesioner lain (misal: UEQ) tanpa mengubah tugas.* |
| Controllability | *✅* | *Pengguna tidak bisa berpindah alur secara bebas; sistem mengunci user pada satu skenario hingga selesai.* |
| Measurability | *✅* | *Data waktu terekam hingga satuan milidetik menggunakan perangkat lunak tracking.* |

**Prinsip mana yang paling sulit dipenuhi?** Controllability (Kontrol Variabel).
**Strategi untuk mengatasinya:**
> Memastikan lingkungan fisik (ruangan, pencahayaan) dan perangkat yang digunakan tetap sama untuk setiap responden guna menghindari faktor eksternal yang memengaruhi persepsi kemudahan.

---

## Latihan 3 — Ablation Study Planning

Dalam konteks UX, ablation study dilakukan dengan melepas atau mematikan fitur spesifik untuk melihat dampaknya terhadap skor usability.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | *✅ Aktif* | *✅ Aktif (Dark Pattern)* | *✅ Standart* | *Baseline kepuasan saat ini.* |
| – A | *❌ (Manual Input)* | *✅* | *✅* | *Mengukur dampak kemudahan voucher.* |
| – B | *✅* | *❌ (Clean Interface)* | *✅* | *Mengukur dampak dark patterns terhadap SUS.* |
| – C | *✅* | *✅* | *❌ (Hamburger Menu)* | *Mengukur efisiensi struktur navigasi.* |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen B (Pop-up Promosi).
**Mengapa?**
> Berdasarkan literatur, dark patterns seperti iklan pop-up yang sulit ditutup seringkali menurunkan skor "Kepuasan" (aspek afektif) pada instrumen SUS, meskipun alur teknisnya mudah digunakan.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko utama membangun sistem monolitik adalah kebingungan dalam mengisolasi variabel (Variable Confounding). Jika sistem memiliki terlalu banyak fitur yang saling bertumpuk, peneliti tidak akan tahu fitur mana yang sebenarnya menyebabkan kenaikan atau penurunan skor usability. Apakah karena warnanya? Apakah karena letak tombolnya? Atau karena alur datanya?

Pentingnya arsitektur modular:
Dalam riset, arsitektur modular memungkinkan peneliti untuk melakukan Variable Isolation. Peneliti dapat mengganti satu modul (misalnya mengganti metode pembayaran) tanpa merusak bagian sistem lainnya. Hal ini menjamin bahwa perbedaan hasil yang didapatkan memang benar-benar disebabkan oleh manipulasi pada variabel independen (IV), sehingga validitas internal penelitian tetap terjaga.
> ___________________________________________________
