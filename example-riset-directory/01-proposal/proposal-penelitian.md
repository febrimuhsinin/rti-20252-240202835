# PROPOSAL PENELITIAN

**Judul:** Evaluasi Dampak Usability Integrasi Layanan Pesan-Antar Makanan pada Super-App E-Commerce: Studi Kasus Perbandingan Shopee Reguler dan Shopee Food
**Peneliti:** Febri Muhsinin (240202835)

---

## BAB I PENDAHULUAN

### 1.1 Latar Belakang
Dalam beberapa tahun terakhir, ekosistem digital di Asia Tenggara mengalami tren transisi yang masif dari aplikasi fungsi tunggal (seperti e-commerce konvensional) menjadi Super-App (aplikasi serba guna). Shopee, yang pada awalnya berfokus sebagai *marketplace* barang fisik, kini telah mengintegrasikan berbagai layanan pihak ketiga ke dalam satu platform antarmuka, salah satunya adalah Shopee Food.

Penambahan turunan layanan ini ditujukan untuk meretensi pengguna dan memusatkan transaksi finansial ke dalam satu ekosistem (*ShopeePay*). Namun, dari kacamata *User Experience* (UX) dan *Human-Computer Interaction* (HCI), penjejalan terlalu banyak fitur yang berbeda konteks ke dalam satu aplikasi berisiko memunculkan *Cognitive Overload* (beban kognitif berlebih) pada pengguna. Pengguna yang sekadar ingin membeli barang bisa saja kebingungan karena banyaknya opsi, ikon, dan navigasi yang saling tumpang tindih. Jika tingkat kemudahan penggunaan (*usability*) pada layanan sekunder (Shopee Food) ternyata sangat rendah akibat kerumitan UI-nya, maka hal ini dapat berbalik merugikan nilai kompetitif Shopee di mata kompetitor yang mengadopsi desain yang lebih bersih.

Oleh karena itu, evaluasi eksperimental diperlukan untuk mengukur secara objektif apakah ada perbedaan tingkat kemudahan dan kepuasan pengguna saat menggunakan alur belanja normal (Reguler) dibandingkan dengan alur pemesanan makanan (Shopee Food) pada aplikasi yang sama.

### 1.2 Rumusan Masalah
Berdasarkan latar belakang tersebut, maka rumusan masalah penelitian ini adalah: 
"Apakah terdapat perbedaan tingkat *usability* (skor kemudahan dan kepuasan) yang signifikan antara antarmuka alur belanja Shopee Reguler dibandingkan dengan antarmuka Shopee Food di kalangan pengguna Generasi Z?"

### 1.3 Tujuan Penelitian
1. Mengukur dan mendapatkan skor System Usability Scale (SUS) dari alur transaksi belanja Shopee Reguler.
2. Mengukur dan mendapatkan skor System Usability Scale (SUS) dari alur transaksi Shopee Food.
3. Menguji secara empiris dan statistik apakah desain antarmuka *Super-app* memicu *cognitive overload* yang menyebabkan degradasi *usability* pada fitur turunannya.

### 1.4 Manfaat Penelitian
- **Secara Teoritis:** Berkontribusi pada literatur HCI mengenai fenomena *Super-app UI* dan dampak buruk *feature bloat* (penumpukan fitur) terhadap beban kognitif pengguna usia muda.
- **Secara Praktis:** Memberikan panduan evaluasi berbasis data kepada desainer UI/UX *(Product Team)* Shopee agar dapat menyederhanakan arsitektur informasi pada halaman Shopee Food agar tidak menyulitkan pengguna.

---

## BAB II TINJAUAN PUSTAKA

### 2.1 Super-App dan Feature Bloat
Super-app merujuk pada sebuah aplikasi payung ( *umbrella app*) yang menyediakan banyak layanan sekaligus, mulai dari pembayaran, belanja, pesan-antar, hingga *gaming*. Namun, fenomena *feature bloat* sering kali terjadi ketika perusahaan terus menambahkan fitur baru tanpa menyadari bahwa hal tersebut mengorbankan ruang navigasi pengguna.

### 2.2 Cognitive Overload (Hick's Law)
Dalam teori desain antarmuka, *Hick's Law* menyatakan bahwa waktu dan usaha mental yang diperlukan untuk mengambil sebuah keputusan akan meningkat secara logaritmik sejalan dengan bertambahnya jumlah pilihan. Antarmuka Shopee Food yang disatukan di dalam Shopee Reguler sering kali dipenuhi *banner* promo, kategori makanan, dan ikon-ikon kecil, sehingga melampaui kapasitas *Working Memory* pengguna.

### 2.3 System Usability Scale (SUS)
SUS adalah instrumen pengujian kebergunaan yang diciptakan oleh John Brooke (1996). Terdiri dari 10 pernyataan skala Likert (1-5), SUS terbukti sangat reliabel untuk menghasilkan skor tunggal 0-100 yang memotret persepsi kebergunaan (*usability*) secara utuh dan cepat tanpa mengharuskan peneliti merekam waktu per detik dari pengguna.

---

## BAB III METODOLOGI PENELITIAN

### 3.1 Desain Penelitian
Penelitian ini merupakan penelitian kuantitatif eksperimental dengan desain **Within-Subjects**. Setiap responden (sebagai satu subjek) akan mencoba dan memberikan evaluasi pada kedua kondisi eksperimen (Shopee Reguler dan Shopee Food). Hal ini dipilih agar variansi *baseline* demografi antar subjek dapat terkontrol dengan sempurna.

### 3.2 Variabel Penelitian
- **Variabel Independen (Bebas):** Tipe alur antarmuka yang dievaluasi (Skenario A: Belanja Shopee Reguler; Skenario B: Pesan-antar Shopee Food).
- **Variabel Dependen (Terikat):** Skor akhir System Usability Scale (SUS) dengan rentang 0-100.
- **Variabel Kontrol:** Usia responden (Gen Z: 18-25 tahun), tingkat literasi digital (mahasiswa/pekerja muda), dan *platform* OS (*smartphone*).

### 3.3 Hipotesis
- **H0 (Hipotesis Nol):** Tidak ada perbedaan skor SUS yang signifikan antara alur belanja Shopee Reguler dengan alur Shopee Food.
- **H1 (Hipotesis Alternatif):** Terdapat perbedaan skor SUS yang signifikan, di mana alur Shopee Food dinilai memiliki tingkat *usability* yang jauh lebih membingungkan (skor lebih rendah) dibandingkan alur Shopee Reguler.

### 3.4 Partisipan dan Sampel
Sampel yang digunakan adalah 36 responden valid. Target demografi dikontrol ketat pada Generasi Z (usia 18-25 tahun). Pemilihan Generasi Z didasarkan pada asumsi literasi digital: jika kelompok demografi yang paling familier dengan teknologi saja merasa kebingungan dengan antarmuka tersebut, maka *usability problem* tersebut berstatus *severe* (kritis) bagi kelompok demografi yang lebih tua.

### 3.5 Prosedur dan Analisis Data
1. **Persiapan:** Kuesioner SUS diadopsi ke dalam Google Form untuk mengukur skor metrik dari responden setelah membayangkan/melakukan skenario transaksi.
2. **Pengumpulan Data:** Data dikumpulkan secara daring. Responden mengisi bagian form Shopee Reguler lalu dilanjutkan ke Shopee Food (terdapat *missing value* Q2 Food secara struktural akibat limitasi teknis form).
3. **Preprocessing:** Data form mentah dikonversi sesuai pedoman pembobotan instrumen SUS (Skala 0-100). Imputasi nilai Netral (3) digunakan untuk bagian Q2 Shopee Food agar menjaga formula baku.
4. **Uji Statistik:** Karena membandingkan dua nilai dari subjek yang sama dan berdistribusi relatif normal (Central Limit Theorem untuk n=36), maka akan digunakan uji parametrik **Paired Sample T-Test** dengan tingkat signifikansi alpha = 0.05.

