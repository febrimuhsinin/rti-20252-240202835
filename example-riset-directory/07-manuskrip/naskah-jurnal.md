---
title: "Evaluasi Dampak Usability Integrasi Layanan Pesan-Antar Makanan pada Super-App E-Commerce: Studi Kasus Shopee Reguler dan Shopee Food"
author: "Febri Muhsinin (240202835)"
---

## ABSTRAK
Transisi platform e-commerce konvensional menjadi *super-app* menghadirkan kompleksitas navigasi yang rentan memicu *cognitive overload*. Penelitian ini mengevaluasi dampak *feature bloat* terhadap tingkat kegunaan (*usability*) pada layanan sekunder aplikasi Shopee, yaitu Shopee Food, dibandingkan dengan layanan utamanya (Shopee Reguler). Menggunakan desain eksperimen *within-subjects*, penelitian ini melibatkan 36 responden Generasi Z yang mengisi instrumen *System Usability Scale* (SUS) untuk kedua alur layanan tersebut. Hasil analisis statistik *Paired Sample T-Test* menunjukkan adanya penurunan skor SUS yang signifikan (P-Value = 7.62e-09 < 0.05). Skor Shopee Reguler berada pada angka 60.56 (kategori Marginal), sedangkan Shopee Food anjlok ke skor 48.26 (kategori Not Acceptable). Kesimpulan dari penelitian ini membuktikan secara empiris bahwa penumpukan fitur layanan pesan-antar makanan di dalam aplikasi belanja utama menciptakan beban kognitif berlebih yang merugikan pengalaman pengguna.

**Kata Kunci:** Super-App, System Usability Scale, Cognitive Overload, Hick's Law, E-Commerce.

---

## 1. PENDAHULUAN

Dalam ekosistem digital modern, perusahaan teknologi berlomba-lomba mengubah aplikasi berfitur tunggal menjadi *super-app*. Di kawasan Asia Tenggara, Shopee—yang awalnya murni sebagai e-commerce fisik—telah berekspansi mengintegrasikan dompet digital, *mini-games*, hingga layanan pesan-antar makanan (Shopee Food) ke dalam satu wadah aplikasi.

Meskipun strategi bisnis ini diklaim mampu menjaga retensi pengguna (Clemmensen et al., 2020), penggabungan fitur dalam jumlah besar berisiko tinggi memicu *feature bloat*. Menurut Teori Beban Kognitif (Sweller, 1988), kapasitas memori kerja manusia sangat terbatas. Apabila pengguna disuguhi antarmuka yang penuh sesak oleh beragam ikon dan menu yang tidak relevan dengan niat utamanya, mereka akan mengalami *Extraneous Cognitive Load*. 

Oleh karena itu, penelitian ini bertujuan menguji secara objektif: Apakah pengguna benar-benar merasakan kesulitan yang signifikan saat menggunakan fitur sekunder (Shopee Food) di dalam *super-app* Shopee, jika dibandingkan dengan kemudahan fitur utamanya (Shopee Reguler)? Penelitian kuantitatif ini diharapkan dapat menjadi rujukan evaluasi desain antarmuka bagi pengembang produk *Super-App*.

## 2. TINJAUAN PUSTAKA

### 2.1 Feature Bloat dan Hick's Law
*Feature bloat* adalah fenomena meluapnya fitur aplikasi yang justru mendegradasi kepuasan pengguna (Alharbi et al., 2022). Fenomena ini dapat dijelaskan melalui *Hick's Law* (Hick, 1952), yang menyatakan bahwa waktu dan beban mental yang dibutuhkan seseorang untuk mengambil keputusan akan meningkat secara logaritmik setiap kali desainer menambahkan elemen atau opsi baru ke dalam antarmuka.

### 2.2 System Usability Scale (SUS)
SUS merupakan alat ukur terstandarisasi yang dirancang oleh Brooke (1996) untuk mengukur kemudahan penggunaan sistem. Terdiri dari 10 butir pertanyaan skala Likert (5 positif, 5 negatif), SUS menghasilkan skor absolut (0-100). Berdasarkan pedoman Bangor et al. (2008), skor SUS di bawah 50 diklasifikasikan sebagai *Not Acceptable* (Sistem buruk dan butuh perombakan).

## 3. METODOLOGI PENELITIAN

Penelitian ini menerapkan metode eksperimental kuantitatif dengan pendekatan *Within-Subjects Design* (Budiu, 2021). Desain ini dipilih agar setiap partisipan (n=36) bertindak sebagai kontrol bagi dirinya sendiri; yakni mencoba Skenario A (Shopee Reguler) lalu diikuti dengan Skenario B (Shopee Food).

Kriteria partisipan dibatasi secara purposif pada Generasi Z (usia 18-25 tahun) yang pernah menggunakan kedua layanan tersebut. Alasan pemilihannya didasarkan pada asumsi literasi digital: jika Gen Z saja mengalami *cognitive overload* saat mengoperasikan aplikasi, maka demografi usia yang lebih tua dipastikan akan jauh lebih kesulitan.

Instrumen pengumpulan data diadopsi dari kuesioner SUS dan dipublikasikan melalui *Google Form*. Terdapat anomali struktural pada saat pengumpulan data yakni hilangnya butir Q2 pada bagian Shopee Food. Mengikuti prinsip keutuhan formula instrumen SUS, data yang hilang tersebut diatasi dengan teknik *Constant Imputation* menggunakan nilai netral (3).

Uji hipotesis dilakukan menggunakan *Paired Sample T-Test* (Alpha = 0.05) berbantuan skrip bahasa pemrograman Python (`scipy.stats`).

## 4. HASIL DAN PEMBAHASAN

### 4.1 Statistik Deskriptif Skor SUS
Berdasarkan perhitungan matematis SUS dari 36 partisipan valid, didapatkan rekapitulasi data sebagai berikut:
- **Shopee Reguler:** Rata-rata Skor = 60.56 (Min = 40.0, Max = 82.5)
- **Shopee Food:** Rata-rata Skor = 48.26 (Min = 30.0, Max = 80.0)

Berdasarkan kategori penilaian Bangor (2008), skor Shopee Reguler (60.56) berada di rentang **Marginal** (Tingkat penerimaan rendah/sedang), sementara Shopee Food (48.26) jatuh ke kategori **Not Acceptable**.

### 4.2 Uji Hipotesis (Paired T-Test)
Pengujian *Paired T-Test* antara kedua kondisi eksperimen menghasilkan nilai signifikansi (P-Value) sebesar **7.621e-09**. Mengingat *P-Value* jauh lebih kecil dari *alpha* (0.05), maka Hipotesis Nol (H0) ditolak secara meyakinkan.

### 4.3 Pembahasan
Penolakan H0 dan margin perbedaan skor yang tajam membuktikan bahwa desain antarmuka Shopee Food di dalam ekosistem *super-app* saat ini memicu *Extraneous Cognitive Load* yang sangat tinggi (Sutanto et al., 2023). Partisipan mengindikasikan bahwa fitur yang saling bertumpuk (belanja, dompet digital, pesan makanan, dan *banner* promo) secara drastis menurunkan kemudahan penggunaan layanan sekunder (Wang & Chen, 2024).

## 5. KESIMPULAN

Transisi platform e-commerce menjadi *Super-app* terbukti memberikan kerugian fungsional pada sisi *Usability*. Penelitian ini mengonfirmasi secara kuantitatif bahwa skor kelayakan antarmuka layanan pesan-antar (Shopee Food) adalah 48.26 (*Not Acceptable*), lebih rendah secara signifikan dibandingkan layanan utamanya (60.56). Tim produk e-commerce sangat disarankan untuk merombak ulang arsitektur informasi *(Information Architecture)* halaman Shopee Food, atau memisahkan layanan tersebut menjadi aplikasi independen *(standalone app)* demi menyelamatkan kenyamanan pengguna.

## DAFTAR PUSTAKA
1. Brooke, J. (1996). "SUS - A quick and dirty usability scale". *Usability Evaluation in Industry*.
2. Hick, W. E. (1952). "On the rate of gain of information". *Quarterly Journal of Experimental Psychology*.
3. Sweller, J. (1988). "Cognitive load during problem solving: Effects on learning". *Cognitive Science*.
4. Bangor, A., Kortum, P., & Miller, J. (2008). "An Empirical Evaluation of the System Usability Scale (SUS)". *International Journal of Human-Computer Interaction*.
5. Budiu, R. (2021). "Between-Subjects vs. Within-Subjects Study Design". *Nielsen Norman Group*.
6. Alharbi, A., et al. (2022). "Feature Bloat and Usability in Mobile Applications: An Empirical Study". *IEEE Access*.
7. Sutanto, E., et al. (2023). "Usability Evaluation of Financial and E-Commerce Super-Apps in Indonesia". *IEEE Access*.
8. Wang, L., & Chen, H. (2024). "Evaluating Cognitive Load in E-Commerce Apps: An Eye-Tracking and SUS Approach". *Journal of Usability Studies*.
