Tugas Akhir Percobaan 2

Judul Program : Sistem Ranking Skor Game

Program ini merupakan simulasi sistem sederhana untuk mengelola dan menampilkan ranking skor pemain dalam sebuah game. Pengguna dapat memasukkan data berupa nama pemain dan skor yang diperoleh, kemudian sistem akan mengurutkan data tersebut dari skor tertinggi ke terendah. Hasil akhir berupa daftar pemain yang sudah terurut sehingga mudah untuk melihat siapa yang memiliki skor paling tinggi. Program ini menggunakan algoritma Exchange Sort, yaitu metode pengurutan dengan cara membandingkan setiap elemen dengan elemen lainnya, lalu menukar posisi jika urutannya tidak sesuai. Pendekatan ini cukup sederhana dan mudah dipahami, sehingga cocok digunakan untuk kasus skala kecil seperti data skor pemain.

Source Code :

<img width="697" height="399" alt="Screenshot 2026-05-05 221504" src="https://github.com/user-attachments/assets/fc4cd9d4-f16a-43fd-b5cf-d71dd24caa3a" />


<img width="786" height="629" alt="Screenshot 2026-05-05 221535" src="https://github.com/user-attachments/assets/3d1e83e7-d42f-44c0-ad55-fa76962c50c1" />


<img width="768" height="375" alt="Screenshot 2026-05-05 221547" src="https://github.com/user-attachments/assets/9f56cade-ccae-4a20-a186-971ab5171bfc" />


Mendefinisikan fungsi bernama tukar yang digunakan untuk menukar posisi dua data dalam array.

Menyimpan data pada indeks ke- i ke dalam variabel sementara temp agar tidak hilang saat proses penukaran.

Memindahkan data pada indeks ke-j ke posisi indeks ke-i.

Memasukkan kembali data yang disimpan di temp ke posisi indeks ke-j sehingga proses pertukaran selesai dengan benar.

Mendefinisikan fungsi bernama exchange_sort yang digunakan untuk mengurutkan data pemain berdasarkan skor dari tertinggi ke terendah.

Membuat perulangan pertama untuk menentukan posisi data yang akan dibandingkan.

Membuat perulangan kedua untuk membandingkan data dengan elemen setelahnya.

Melakukan pengecekan apakah skor pemain lebih kecil dibandingkan pemain lain agar bisa disusun dari nilai terbesar ke terkecil.

Memanggil fungsi tukar jika kondisi terpenuhi untuk menukar posisi data.

Mengulangi proses perbandingan dan penukaran sampai seluruh data tersusun dengan benar.

Mendefinisikan fungsi utama bernama main sebagai pusat jalannya program.

Memulai proses input jumlah pemain dengan menggunakan penanganan error agar input harus berupa angka.

Menampilkan pesan kesalahan jika input tidak valid dan menghentikan program.

Membuat list kosong bernama arr untuk menyimpan data pemain.

Menampilkan instruksi kepada pengguna untuk memasukkan data pemain.

Memulai perulangan untuk menginput data pemain sesuai jumlah yang dimasukkan.

Meminta pengguna memasukkan nama pemain.

Memulai proses input skor dengan validasi menggunakan try-except agar hanya menerima angka.

Menampilkan pesan error jika skor yang dimasukkan tidak valid.

Menyimpan data pemain ke dalam list dalam bentuk dictionary yang berisi nama dan skor.

Menampilkan data pemain sebelum dilakukan proses pengurutan sebagai pembanding.

Melakukan perulangan untuk menampilkan seluruh data pemain yang telah dimasukkan.

Memanggil fungsi exchange_sort untuk mengurutkan data berdasarkan skor tertinggi.

Menampilkan hasil data setelah diurutkan.

Melakukan perulangan kembali untuk menampilkan data yang sudah dalam kondisi terurut dari skor tertinggi ke terendah.

Menjalankan fungsi utama menggunakan blok standar Python agar program dapat dieksekusi.

Memastikan fungsi main hanya berjalan saat file dijalankan secara langsung.


    OUTPUT PROGRAM


   <img width="536" height="822" alt="Screenshot 2026-05-05 222209" src="https://github.com/user-attachments/assets/0dd2ce35-d759-403b-8e5b-cb2d1545520c" />

   

LINK : https://youtu.be/tqywAAjCEJA?si=ASpw_FvoeyDqSego
