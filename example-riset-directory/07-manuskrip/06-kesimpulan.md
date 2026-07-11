## 5. KESIMPULAN DAN SARAN

### 5.1 Kesimpulan
Strategi transformasi platform e-commerce konvensional menjadi ekosistem *super-app* yang serba ada terbukti memberikan kerugian fungsional yang signifikan pada sisi kebergunaan antarmuka (*Usability*). Penelitian ini berhasil mengonfirmasi secara empiris dan kuantitatif melalui instrumen baku *System Usability Scale* (SUS) bahwa tingkat kelayakan antarmuka layanan turunan—dalam kasus ini Shopee Food—berada di rentang skor 48.26. Skor ini jatuh pada kategori *Not Acceptable* (Tidak Dapat Diterima).

Angka tersebut secara substansial lebih rendah dan memburuk secara signifikan (*P-Value* < 0.05) jika dibandingkan dengan pengalaman pengguna saat mengoperasikan layanan inti berbelanja fisik di aplikasi yang sama (Shopee Reguler), yang masih mampu mencatatkan skor 60.56 (*Marginal*). Lebar kesenjangan UX ini secara akademis membuktikan bahwa penjejalan fitur yang agresif (*feature bloat*) secara langsung mengekskalasi beban memori kognitif pengguna. Kepadatan informasi ini memvalidasi *Hick's Law*: aplikasi menjadi terlalu rumit untuk dipelajari, navigasi antar-halaman menjadi tidak konsisten, dan pada titik kronis, kekacauan visual ini dapat mematahkan niat transaksi (*conversion rate*) pengguna.

### 5.2 Saran dan Rekomendasi
Berdasarkan konklusi statistik di atas, tim produk, perancang antarmuka (UI), dan perancang pengalaman (UX) aplikasi *super-app e-commerce* sangat disarankan untuk segera merombak ulang Arsitektur Informasi (*Information Architecture*) pada halaman layanan turunan mereka. 

Beberapa mitigasi taktis yang direkomendasikan meliputi:
1. **Separasi Platform:** Mempertimbangkan untuk memisahkan layanan berat seperti pesan-antar makanan menjadi aplikasi independen *(standalone app)*. Langkah ini terbukti sukses dilakukan oleh beberapa raksasa teknologi global untuk menjaga keringanan memori aplikasi utama.
2. **Progressive Disclosure:** Jika pemisahan aplikasi tidak memungkinkan secara bisnis, maka implementasikan desain *progressive disclosure* di mana elemen-elemen sekunder dan promosi disembunyikan dalam sub-menu yang rapi, bukan ditumpuk di halaman utama layar.
3. **Kustomisasi Beranda:** Memberikan kontrol penuh kepada pengguna (*user-centric design*) untuk menonaktifkan atau menyembunyikan ikon layanan (seperti *mini-games* atau Shopee Food) apabila pengguna tersebut sama sekali tidak pernah memiliki intensi untuk menggunakannya.

### 5.3 Limitasi dan Penelitian Lanjutan
Penelitian ini tidak luput dari batasan. Fokus studi ini secara eksklusif hanya menargetkan sampel Generasi Z yang notabene merupakan *digital natives*. Jika kelompok umur yang secara historis paling cepat beradaptasi dengan teknologi saja mengalami *cognitive overload*, maka populasi umur di atasnya diyakini akan mendapatkan skor SUS yang jauh lebih hancur.

Oleh karena itu, penelitian lanjutan sangat didorong untuk mengekspansi sampel ke demografi Milenial dan *Baby Boomers*. Selain itu, direkomendasikan agar studi berikutnya menggabungkan metrik SUS dengan teknologi analisis neurosains kognitif—seperti *Eye Tracking* (Pelacakan Mata) atau *Electroencephalography* (EEG)—untuk mengidentifikasi secara mikroskopis koordinat antarmuka mana yang paling banyak memicu titik buta visual dan lonjakan beban stres bagi pengguna.
