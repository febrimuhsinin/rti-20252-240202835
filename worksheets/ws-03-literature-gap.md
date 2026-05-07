# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Analisis Usability dan Pengaruh Dark Patterns pada Aplikasi Shopee Menggunakan Metode System Usability Scale (SUS)
Database   : Google Scholar, IJOINT, MALCOM, Jurnal Simkom, JAIC
Query      : ("System Usability Scale" OR "SUS") AND "Shopee" AND ("Dark Patterns" OR "User Experience")
Tahun      : 2021 – 2026
Hasil awal : 10 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
|   Lim et al.    |   2025    |    SUS (Comparative)    |   411 Gen Z (Batam)   |    90.06 (Best Imaginable)    |      Identifikasi dark patterns (pop-up) masih bersifat kualitatif.      |
|   Aisyah S. et al.    |   2025    |   SUS + UTAUT2     |   190 Mahasiswa (Unhas)   |    68.58 (Marginal High)    |      Faktor pengaruh sosial memiliki persentase terendah (73.26%).      |
|   Sagala & Pakaja   |    2024   |    UT + SUS    |  30 Active Users    |   70 (Acceptable/Good)     |      Kebingungan user pada fitur voucher dan metode pembayaran.      |
|   Huda et al.    |    2023   |    SUS    |   10 Users   |    76 (Good/Acceptable)       |      Sampel sangat kecil dan terbatas pada fitur belanja dasar.      |
|   Sembodo et al.   |    2021   |    SUS    |   30 Users   |    67.08 (OK)    |     Fokus pada platform website, bukan mobile.       |

Pola yang ditemukan:
  Metode dominan     : Penggunaan kuesioner SUS
  Dataset umum       : Responden didominasi oleh Generasi Z dan Mahasiswa.
  Limitasi berulang  : Analisis seringkali bersifat deskriptif umum tanpa mengaitkan elemen desain spesifik (seperti dark patterns) terhadap skor kepuasan secara kuantitatif.

GAP IDENTIFICATION

Gap 1: [Jenis: performance / method / data / context]
  Deskripsi    : Belum adanya integrasi pengukuran dampak manipulatif dark patterns (seperti forced continuity atau urgency) terhadap fluktuasi skor SUS.
  Bukti        : Lim et al. (2025) menyebutkan pop-up yang mengganggu sebagai isu, namun tidak mengukur korelasi spesifiknya terhadap skor 90.06 yang dihasilkan.
  Signifikansi : Penting untuk mengetahui apakah kemudahan penggunaan (usability) tinggi justru "dipaksakan" oleh desain yang manipulatif.

Gap 2: [Jenis: Performance Gap]
  Deskripsi    : Ketidakkonsistenan performa pada alur transaksi kritis (pembayaran dan voucher) dibandingkan navigasi belanja umum.
  Bukti        : Sagala & Pakaja (2024) mencatat user merasa tersesat/bingung saat mengganti metode pembayaran meskipun skor total masuk kategori "Good".
  Signifikansi : Perbaikan pada aspek teknis fitur pembayaran dapat secara signifikan meningkatkan retensi user.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
|    Skor SUS Shopee Gen Z (2025)      |     Menunjukkan performa terbaru pada target demografi Gen Z.      |       Sampel besar (411 responden).        |    Lim et al., 2025    |
|    Skor SUS Shopee Nasional (2023)      |     Mewakili penggunaan umum e-commerce di Indonesia.      |       Menjadi rujukan kategori "OK" ke "Good".        |   Huda et al., 2023     |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Analisis Usability dan Pengaruh Dark Patterns pada Shopee.
**Query pencarian:** ("SUS") AND "Shopee" AND "Dark Patterns"
**Database:** IJOINT, MALCOM, Jurnal Simkom.

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | *Lim et al.* | *2025* | *SUS* | *411 Gen Z* | *90.06* | *Mengabaikan faktor finansial user.* |
| 2 | *Aisyah S. et al.* | *2025* | *UTAUT2* | *190 Mahasiswa* | *Habit 87%* | *Pengaruh sosial belum kuat.* |
| 3 | *Sagala & Pakaja* | *2024* | *UT+SUS* | *30 User* | *70 (OK)* | *Isu navigasi pembayaran.* |
| 4 | *Huda et al.* | *2023* | *SUS* | *10 User* | *76* | *Sampel tidak representatif.* |
| 5 | *Sembodo et al.* | *2021* | *SUS* | *30 User* | *67.08* | *Belum menguji versi aplikasi.* |

**Pola yang terlihat — Metode dominan:** Kuesioner SUS yang sering dikombinasikan dengan metode kualitatif seperti wawancara atau Usability Testing (UT).
**Limitasi yang berulang:** Studi terfokus pada kemudahan belajar (learnability), namun sering mengabaikan aspek kenyamanan visual jangka panjang akibat iklan berlebihan.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | *Alur voucher yang tidak intuitif memperlambat efisiensi user hingga 22.8% error rate.* |
| Method Gap | [x] Ya / [ ] Tidak | *Kurangnya penggunaan metrik Dark Pattern yang terukur bersamaan dengan SUS.* |
| Data Gap | [ ] Ya / [ ] Tidak | *Data responden mahasiswa sudah cukup solid.* |
| Context Gap | [x] Ya / [ ] Tidak | *Penelitian fokus di kota besar/universitas, belum menyentuh user di daerah pelosok.* |

**Gap utama yang dipilih:** Pengaruh elemen Dark Patterns (seperti iklan pop-up berulang) terhadap persepsi kepuasan (SUS) pada segmen pengguna dengan frekuensi penggunaan tinggi.
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Gap ini penting karena skor SUS yang tinggi bisa menutupi masalah etika desain. Jika user merasa aplikasi "mudah" tapi "menjebak", kepuasan yang terukur melalui SUS mungkin bias oleh faktor kebiasaan (habit). Memahami hubungan ini akan membantu desainer menciptakan UI yang tidak hanya fungsional tapi juga etis.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | *SUS Score 90.06* | *Objek sama (Shopee) dan target Gen Z.* | *Sampel terbesar di antara literatur.* | *Ya (2025)* | *Lim et al.* |
| 2 | *SUS Score 70.0* | *Fokus pada layanan spesifik (Shopee Food).* | *Menggunakan kombinasi kualitatif (UT) & kuantitatif (SUS).* | *Ya (2024)* | *Sagala & Pakaja   * |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Baseline yang dipilih adalah penelitian terbaru (2024-2025) dengan metodologi yang ketat dan sampel yang representatif, bukan membandingkan dengan sistem yang sengaja dibuat buruk.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Perbedaan antara klaim tanpa bukti dengan research gap yang valid terletak pada dokumen bukti pencarian. Klaim "belum ada yang meneliti" seringkali hanya asumsi, sementara research gap yang valid didasarkan pada analisis matriks literatur yang menunjukkan bahwa meskipun topik A sudah diteliti, namun aspek B atau metode C belum pernah dikombinasikan.
> Cara membuktikannya adalah dengan menyajikan tabel concept-centric seperti di atas, yang menunjukkan limitasi berulang dari para peneliti sebelumnya secara eksplisit. Bukti pencarian Boolean query yang didokumentasikan juga memperkuat bahwa gap tersebut benar-benar ada secara ilmiah.
