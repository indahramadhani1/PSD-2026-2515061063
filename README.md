Tugas Akhir Percobaan 5

Judul Program : Sistem Kontak HP Menggunakan Binary Search Tree (BST)

Program ini merupakan simulasi sistem sederhana untuk mengelola daftar kontak HP menggunakan struktur data Binary Search Tree (BST). Pengguna dapat menambahkan data kontak, mencari kontak berdasarkan nama, menampilkan seluruh daftar kontak secara terurut, melihat kontak dengan nama paling awal maupun paling akhir, serta menghitung jumlah seluruh kontak yang tersimpan. Setiap data kontak terdiri dari nama kontak dan nomor HP. Hasil akhir program berupa informasi data kontak yang berhasil disimpan, hasil pencarian kontak, serta daftar seluruh kontak yang ditampilkan secara alfabetis. Program ini menggunakan struktur data Binary Search Tree (BST), yaitu struktur data pohon biner yang memiliki aturan bahwa data pada subtree kiri lebih kecil dari root dan data pada subtree kanan lebih besar dari root. Implementasi BST dilakukan menggunakan class Node untuk menyimpan data kontak dan pointer ke child kiri maupun kanan, serta class BSTKontak untuk mengatur proses insert, search, traversal, dan operasi lainnya. Traversal inorder digunakan untuk menampilkan daftar kontak secara urut berdasarkan nama. Pendekatan ini sederhana, efisien, dan cocok digunakan untuk sistem pencarian data seperti daftar kontak HP karena mampu mempercepat proses pencarian dan pengelompokan data secara terstruktur.


Source Code :



Mendefinisikan class bernama QueueArray yang digunakan untuk membuat sistem antrian pemesanan tiket bioskop online menggunakan struktur data queue array.

Mendefinisikan method __init__ untuk menginisialisasi ukuran maksimum queue, array penyimpanan data, serta posisi depan (front_idx) dan belakang (rear_idx) antrian.

Membuat variabel MAXN sebagai kapasitas maksimum antrian pemesanan tiket.

Membuat array q menggunakan list Python untuk menyimpan data pemesan tiket bioskop.

Memberikan nilai awal -1 pada front_idx dan rear_idx sebagai penanda bahwa antrian masih kosong.

Mendefinisikan fungsi is_empty() untuk memeriksa apakah antrian kosong.

Mengembalikan nilai True jika front_idx bernilai -1, yang berarti belum ada data pemesan pada antrian.

Mendefinisikan fungsi is_full() untuk memeriksa apakah kapasitas antrian sudah penuh.

Menggunakan konsep circular queue dengan operasi modulo % untuk menentukan apakah posisi belakang antrian sudah kembali ke posisi depan.

Mendefinisikan fungsi enqueue() untuk menambahkan data pemesan tiket ke dalam antrian.

Melakukan pengecekan terlebih dahulu apakah antrian penuh menggunakan fungsi is_full().

Menampilkan pesan “Antrian pemesanan penuh!” jika kapasitas queue sudah tidak tersedia.

Melakukan pengecekan apakah antrian masih kosong menggunakan fungsi is_empty().

Mengatur nilai front_idx dan rear_idx menjadi 0 jika data pertama dimasukkan ke antrian.

Menggeser posisi rear_idx ke belakang menggunakan operasi modulo jika antrian sudah memiliki data sebelumnya.

Menyimpan data pemesan tiket ke dalam array queue pada posisi rear_idx.

Menampilkan pesan bahwa data pemesanan tiket berhasil ditambahkan ke antrian.

Mendefinisikan fungsi dequeue() untuk melayani atau menghapus pemesan tiket dari bagian depan antrian.

Melakukan pengecekan apakah antrian kosong sebelum melayani pemesan.

Menampilkan pesan “Antrian pemesanan kosong!” jika tidak ada data pada queue.

Mengambil data pemesan pada posisi paling depan antrian menggunakan front_idx.

Menampilkan informasi pemesan yang sedang dilayani berupa nama pemesan, judul film, dan jumlah tiket.

Mengatur kembali front_idx dan rear_idx menjadi -1 jika setelah dequeue antrian menjadi kosong.

Menggeser posisi front_idx ke data berikutnya menggunakan operasi modulo jika masih terdapat data pada queue.

Mendefinisikan fungsi peek() untuk melihat data pemesan paling depan tanpa menghapus data dari antrian.

Melakukan pengecekan apakah queue kosong sebelum menampilkan data.

Mengambil data pemesan pada posisi paling depan menggunakan front_idx.

Menampilkan data pemesan paling depan berupa nama pemesan, judul film, dan jumlah tiket.

Mendefinisikan fungsi display() untuk menampilkan seluruh data pemesan tiket pada antrian.

Melakukan pengecekan apakah antrian kosong sebelum menampilkan data.

Membuat variabel i sebagai indeks awal dari posisi depan queue.

Membuat variabel nomor untuk memberikan nomor urutan antrian.

Menggunakan perulangan while True untuk menampilkan seluruh data queue dari depan hingga belakang.

Menampilkan informasi setiap pemesan berupa nama pemesan, judul film, dan jumlah tiket.

Menghentikan perulangan jika indeks sudah mencapai posisi rear_idx.

Menggeser indeks menggunakan operasi modulo agar circular queue tetap berjalan dengan benar.

Mendefinisikan fungsi main() sebagai pusat jalannya program.

Membuat objek queue dari class QueueArray.

Membuat variabel pilih untuk menyimpan pilihan menu dari pengguna.

Menampilkan menu sistem antrian tiket bioskop online kepada pengguna.

Meminta pengguna memilih menu yang tersedia seperti tambah pemesan, layani pemesan, melihat antrian depan, dan menampilkan seluruh antrian.

Menggunakan blok try-except untuk menangani kesalahan input agar program tidak error saat pengguna memasukkan data yang tidak sesuai.

Meminta pengguna memasukkan nama pemesan, judul film, dan jumlah tiket saat memilih menu tambah pemesan.

Menyimpan data pemesan ke dalam dictionary Python sebelum dimasukkan ke queue.

Memanggil fungsi enqueue() untuk menambahkan data pemesan ke antrian.

Memanggil fungsi dequeue() saat pengguna memilih menu melayani pemesan.

Memanggil fungsi peek() saat pengguna ingin melihat antrian paling depan.

Memanggil fungsi display() saat pengguna ingin melihat seluruh daftar antrian.

Menampilkan pesan “Program selesai.” saat pengguna memilih menu keluar.

Menggunakan blok standar Python if __name__ == "__main__" agar program dapat dijalankan langsung.

Memastikan fungsi main() hanya dijalankan saat file program dieksekusi secara langsung.


    OUTPUT PROGRAM

   
   
LINK : 
