# MEMBUAT MODEL UNTUK MEMPREDIKSI STATUS KLAIM DALAM RANGKA MENGURANGI KERUGIAN AKIBAT SALAH PREDIKSI
Dalam Kasus ini akan melakukan
1. Laporan Pembuatan Model (.ipynb)
2. Model Terpilih (.Pikle)
3. Aplikasi Strimlit untuk Menerapkan Model Terpilih (Strimlit)
4. Video Presesntasi (Link Video)
5. Jurnal Pendukung (Link Jurnal)

** Note : Untuk menjalankan Strimlit, silahkan download kemudian run terminal dengan (Run Strimlit "FolderPath\Homepage.py"), atau bisa akses di link ini [Klick Disini]()


# Identifikasi Masalah
Perusahaan asuransi perjalanan sering menghadapi tantangan dalam memprediksi pemegang polis mana yang kemungkinan besar akan mengajukan klaim. Ketidakpastian ini menyebabkan alokasi sumber daya yang kurang efisien, baik dalam pengelolaan risiko maupun dalam penggunaan data pelanggan untuk kebutuhan strategis lainnya. Sebagai contoh, polis yang belum diklaim memiliki potensi besar untuk dimanfaatkan dalam strategi pemasaran produk tambahan, personalisasi layanan, atau penyesuaian premi yang lebih kompetitif. Namun, tanpa pemahaman yang tepat tentang profil pelanggan yang cenderung melakukan klaim, perusahaan kehilangan peluang untuk mengoptimalkan nilai dari setiap polis yang dimiliki.

0 : Pelanggan **Tidak melakukan Claim** Asuransi

1 : Pelanggan Melakukan **Claim** Asuransi

- FP 
    1. ML memprediksi Claim, tapi faktanya bukan 
    2. Perusahaan merugi akibat jumlah cycle money yang akan dikelola tidak sesuai, sehingga dapat mengakibatkan kerugian sebesar 
        - Total Biaya Salah Prediksi = Frekuensi Kesalahan Prediksi × Nilai Rata-Rata Klaim
        - Terdapat 39 ribu data pelanggan (Non Duplicate)
        - Apabila rata-rata nilai Klaim setara Rp 45.925.000
        - Maka Kerugian yang dialami adalah sebesar :  **Rp 87.803.750.000**
            - Sumber Nominal [Klick Disini](https://www.ojk.go.id/id/kanal/iknb/data-dan-statistik/asuransi/Documents/Pages/Statistik-Perasuransian-2020/Statistik%20Perasuransian%20Indonesia%202020.pdf)

- FN
    1. ML memprediksi bukan, tapi faktanya Claim
    2. Perusahaan mengalami kerugian akibat tuntutan pemegang polis, serta kehilangan kepercayaan pada masyarakat
        - Total Biaya Salah Prediksi = Frekuensi Kesalahan Prediksi × Nilai Rata-Rata Klaim
        - Terdapat 39 ribu data pelanggan (Non Duplicate)
        - Apabila rata-rata nilai Klaim setara Rp 45.925.000
        - Maka Kerugian yang dialami adalah sebesar : **Rp 540.803.750.000**
            - Sumber Nominal [Klick Disini](https://www.ojk.go.id/id/kanal/iknb/data-dan-statistik/asuransi/Documents/Pages/Statistik-Perasuransian-2020/Statistik%20Perasuransian%20Indonesia%202020.pdf)

# Goals
Dengan memanfaatkan data historis dan analitik prediktif, perusahaan dapat membangun model yang mampu mengidentifikasi pola dan faktor risiko yang menentukan kemungkinan klaim. Hal ini tidak hanya membantu perusahaan mengelola klaim dengan lebih baik, tetapi juga memungkinkan mereka mengarahkan fokus pada pemegang polis yang belum melakukan klaim untuk penawaran layanan yang lebih proaktif. Solusi ini akan membuka peluang bagi perusahaan untuk meningkatkan efisiensi operasional, memaksimalkan profitabilitas polis, dan menciptakan pengalaman pelanggan yang lebih personal dan relevan, serta mengurangi kerugian perusahaan akibat pengeluaran biaya.

# Pendekatan Analytic
Berdasarkan beberapa poin yang telah dijabarkan diatas dapat disimpulkan bahwa ketika perusahaan memiliki jumlah 
1. FP (ML memprediksi Claim, tapi faktanya bukan)
    - Total Kerugian yang dialami adalah sebesar : **Rp 87.803.750.000**
2. FN (ML memprediksi bukan, tapi faktanya Claim) : 
    - Total Kerugian yang dialami adalah sebesar : **Rp Rp 540.803.750.000**

Sehingga **Evaluation Method Metrics Model** yang digunakan dalam kasus ini karena baik FP dan FN sama sama merugikan perusahaan sehingga perusahaan ingin menekan angka FP dan FN sehingga nilai kerugian bisa ditanggulangi namun tetap berat terhadap FN karena memiliki jumlah kerugian yang lebih besar dibandingkan FP dengan selisih **Rp 468 M** sehingga model akan menggunakan (**F2 Score**) 
- F2 Score = Dalam upaya menekan biaya pengeluaran yang terjadi pada metric FP dan FN, apabila ingin menekan kedua  metric namun karena salah satu metric memiliki jumlah kerugian lebih besar, sehingga perusahaan ingin menekan FP dan FN, namun juga ingin menekan jumlah FN dengan cukup signifikan, maka metode scoring yang dilakukan untuk menjadi landasan model dalam menentukan Claim/not Claim maka F2 Score menjadi pilihan terbaik, karena F2 Score berfokus pada 
    1. FP dan FN
    2. FN (1x bobot) sedangkan FP (2x bobot)

Dapat disimpulkan bahwa jumlah kerugian yang dialami perusahaan dapat menurun baik dari metric FP dan FN, namun untuk FN pengurangannya 2x secara signifikan dibandingkan FP.

# Proses Pengajuan Klaim Asuransi
- Proses A merupakan proses pengajuan oleh pemegang polis, adapun kegiatan yang dilakukan hanyalah menghubungi pihak travel insurance 
    1. Offline = Datang langsung ke kantor pihak asuransi, kemudian menghubungi pihak claim insurance
    2. Online = Mengunjungi website pihak asuransi kemudian login ke website tersebut

- Proses B merupakan proses pengisian biodata dan kebutuhan lainnya dalam memenuhi persayratan dalam pengajuan asuransi, adapun berkas yang diperlukan antara lain
    1. Fotocopy KTP,
    2. Mengisi Formulir pengajuan claim,
    3. Fotocopy KK,
    4. Surat keterangan Kepolisian (Cancelation Plans),
    5. Surat Bermaterai Kesepakatan Penyataan Claim,
    6. Foto Kwitansi pembayaran (Travel Plans)

- Proses C merupakan proses seleksi oleh perusahaan asuransi, dimana dari berkas pemegang polis yang telah di berikan untuk pengajuan Claim, perusahaan akan memilih bedasarkan kriteria pengajuan, data pengisian akan di analisis dengan data historis untuk mengetahui adanya pengajuan Fraud/dll, apabila memenuhi persayaratan maka perusahaan akan meloloskan pengajuan oleh pemegang polis, apabila tidak, maka perusahaan akan menolak pengajuan tersebut. Adapun beberapa ketentuan yang diterapkan dalam pengesahan klaim adalah sebagai berikut :
    1. First Notification setelah pengajuan claim oleh pemegang polis adalah maksimum 30 hari kerja dari tanggal pengajuan
       dengan memberikan informasi tambahan berupa No.Polis asuransi, Nama pengaju, Keterangan pengajuan
    2. Keputusan klaim dilakukan setelah First Notification diterima oleh pemegang polis paling lama 14 hari kerja

- Proses D meruapakan proses akhir dan hanya terjadi apabila pemegang polis lolos seleksi pada Proses C, kemudian pemegang polis akan langsung menerima uang asuransi yang telah dibayarkan dan proses dinyatakan SELESAI

- # Penerapan Model
- Dengan memanfaatkan data historis dan analitik prediktif, perusahaan dapat membangun model yang mampu mengidentifikasi pola dan faktor risiko yang menentukan kemungkinan klaim. Hal ini tidak hanya membantu perusahaan mengelola klaim dengan lebih baik, tetapi juga memungkinkan mereka mengarahkan fokus pada pemegang polis yang belum melakukan klaim untuk penawaran layanan yang lebih proaktif. Solusi ini akan membuka peluang bagi perusahaan untuk meningkatkan efisiensi operasional, memaksimalkan profitabilitas polis, dan menciptakan pengalaman pelanggan yang lebih personal dan relevan.

Sehingga dari penjelasan diatas, model akan diterapkan pada **Proses C**, dimana pada proses tersebut akan dilakukan 
1. Penentuan Claim/Not Claim
2. Penentuan apakah Pemegang Polis Dinyatakan lolos atau tidak dari status FP/FN

Kemudian langkah berikutnya adalah menganalisis data untuk menemukan pola yang membedakan kandidat pemegang polis yang mau melakukan Claim atau tidak.

Kemudian kita akan membangun **model klasifikasi** yang akan membantu perusahaan untuk dapat memprediksi probabilitas seorang kandidat akan/ingin melakukan Claim di perusahaan tersebut atau tidak.

Dengan menggunakan metric scorer **F2 Score** karena ingin menekan biaya pengeluaran/biaya kerugian FP dan FN, namun karena jumlah pengeluaran FN jauh lebih besar maka pembobotan pengurangan FN menjadi 2x pembobotan sedangkan FN 1x
