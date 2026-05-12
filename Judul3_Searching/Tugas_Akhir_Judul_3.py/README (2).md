Tugas Akhir Percobaan 3

Judul Program : Sistem Pengecekan Nama Siswa di Daftar Hadir

Program ini merupakan simulasi sistem sederhana untuk melakukan pengecekan nama siswa pada daftar hadir kelas. Pengguna dapat memasukkan nama siswa yang ingin dicari, kemudian sistem akan memeriksa apakah nama tersebut terdapat pada daftar hadir dan menghitung berapa kali nama muncul. Hasil akhir berupa informasi apakah nama ditemukan atau tidak, beserta jumlah kemunculannya di dalam daftar hadir. Program ini menggunakan algoritma Sequential Searching, yaitu metode pencarian dengan cara memeriksa data satu per satu secara berurutan mulai dari elemen pertama hingga elemen terakhir. Jika data yang dicari ditemukan, maka sistem akan menghitung jumlah kemunculannya. Pendekatan ini sederhana dan mudah dipahami, sehingga cocok digunakan untuk pencarian data dalam jumlah kecil seperti daftar hadir siswa.

Source Code :

<img width="822" height="668" alt="Screenshot 2026-05-12 230353" src="https://github.com/user-attachments/assets/1b745c7c-e7fa-403f-8122-691c6f00aed9" />


<img width="682" height="397" alt="Screenshot 2026-05-12 230331" src="https://github.com/user-attachments/assets/289f031c-78a2-46a5-ab73-02f73699555b" />

Mendefinisikan fungsi bernama sequential_search yang digunakan untuk mencari nama siswa pada daftar hadir menggunakan metode Sequential Searching.

Membuat variabel i dengan nilai awal 0 yang digunakan sebagai indeks untuk memulai pencarian dari data pertama.

Membuat variabel counter dengan nilai awal 0 untuk menghitung jumlah nama yang ditemukan.

Membuat perulangan while untuk memeriksa data satu per satu selama indeks masih kurang dari jumlah data.

Menampilkan nama yang sedang diperiksa agar pengguna dapat melihat proses pencarian berlangsung.

Melakukan pengecekan apakah nama pada daftar sama dengan nama yang dicari.

Menambahkan nilai counter sebanyak 1 jika nama ditemukan.

Menambahkan nilai indeks i agar proses berpindah ke data berikutnya.

Mengulangi proses pengecekan hingga seluruh data selesai diperiksa.

Mengembalikan nilai counter sebagai jumlah nama yang ditemukan pada daftar hadir.

Mendefinisikan fungsi utama bernama main sebagai pusat jalannya program.

Membuat list bernama data yang berisi daftar hadir siswa.

Menghitung jumlah data pada daftar hadir menggunakan fungsi len() lalu menyimpannya ke variabel n.

Menampilkan seluruh daftar hadir siswa kepada pengguna.

Meminta pengguna memasukkan nama yang ingin dicari pada daftar hadir.

Memanggil fungsi sequential_search untuk melakukan proses pencarian nama siswa.

Menyimpan hasil jumlah nama yang ditemukan ke dalam variabel counter.

Melakukan pengecekan apakah nilai counter lebih besar dari 0 untuk mengetahui apakah nama ditemukan.

Menampilkan pesan bahwa nama ditemukan beserta jumlah kemunculannya jika data ada pada daftar hadir.

Menampilkan pesan bahwa nama tidak ditemukan jika data tidak ada pada daftar hadir.

Menggunakan blok standar Python if __name__ == "__main__" agar program dapat dijalankan langsung.

Memastikan fungsi main() hanya dijalankan saat file program dieksekusi secara langsung.


    OUTPUT PROGRAM

    <img width="898" height="495" alt="Screenshot 2026-05-12 230316" src="https://github.com/user-attachments/assets/b57f4349-46f2-41df-8071-f1a3fb2dcda1" />

   
LINK : https://youtu.be/Jnrb_iqXSac?si=sJbA0FCTNVr2CkVZ
