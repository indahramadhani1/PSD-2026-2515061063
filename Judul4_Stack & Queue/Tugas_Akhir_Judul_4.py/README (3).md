Tugas Akhir Percobaan 4

Judul Program : Sistem Antrian Pemesanan Tiket Bioskop Online

Program ini merupakan simulasi sistem sederhana untuk mengatur antrian pemesanan tiket bioskop secara online. Pengguna dapat menambahkan data pemesan tiket, melayani pemesan berdasarkan urutan antrian, melihat pemesan paling depan, serta menampilkan seluruh daftar antrian yang sedang menunggu. Setiap data pemesan terdiri dari nama pemesan, judul film, dan jumlah tiket yang dipesan. Hasil akhir program berupa informasi data pemesan yang berhasil masuk ke antrian, data pemesan yang sedang dilayani, serta daftar seluruh antrian pemesanan tiket bioskop. Program ini menggunakan struktur data Queue Array dengan konsep FIFO (First In First Out), yaitu data yang pertama masuk akan menjadi data pertama yang dilayani. Implementasi queue dilakukan menggunakan array melingkar (circular queue) dengan bantuan variabel front_idx dan rear_idx untuk mengatur posisi depan dan belakang antrian. Pendekatan ini sederhana, efisien, dan cocok digunakan untuk sistem antrian seperti pemesanan tiket bioskop online.


Source Code :
<img width="1115" height="988" alt="Screenshot 2026-05-19 224128" src="https://github.com/user-attachments/assets/7c8cbc90-8c6e-4985-9720-8f111a82b215" />

<img width="1062" height="863" alt="Screenshot 2026-05-19 224140" src="https://github.com/user-attachments/assets/c00e5d9d-1c9f-4ea3-87d5-2673781dbd78" />


<img width="862" height="896" alt="Screenshot 2026-05-19 224152" src="https://github.com/user-attachments/assets/2cc41eaa-14cd-4147-96cc-72fea11e21a5" />


<img width="752" height="926" alt="Screenshot 2026-05-19 224207" src="https://github.com/user-attachments/assets/43e79692-5b39-4a57-926f-bdbd3ff67315" />


<img width="755" height="865" alt="Screenshot 2026-05-19 224218" src="https://github.com/user-attachments/assets/0e124fc8-0e8d-4253-97f1-62f8e88989d6" />

![Uploading Screenshot 2026-05-19 224218.png…]()







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

   <img width="650" height="741" alt="Screenshot 2026-05-19 223944" src="https://github.com/user-attachments/assets/7568ed08-b25c-450d-9e5e-49e8940c86e7" />


   <img width="693" height="720" alt="Screenshot 2026-05-19 223957" src="https://github.com/user-attachments/assets/f6b2c066-c2ea-47c9-82da-103b01c14a9e" />


   <img width="651" height="751" alt="Screenshot 2026-05-19 224008" src="https://github.com/user-attachments/assets/5622d38d-5aa1-41ee-b58e-c2ccf0dc5ff2" />


   <img width="596" height="835" alt="Screenshot 2026-05-19 224022" src="https://github.com/user-attachments/assets/bae874c5-ea31-4f3a-a4ac-6e44f7278d1c" />


<img width="441" height="651" alt="Screenshot 2026-05-19 224037" src="https://github.com/user-attachments/assets/daf95b3c-7922-4a68-9b39-570a0eb107a0" />


<img width="456" height="790" alt="Screenshot 2026-05-19 224046" src="https://github.com/user-attachments/assets/d8f09ed8-9217-4fc7-b70a-bc295868b5c4" />


<img width="447" height="786" alt="Screenshot 2026-05-19 224056" src="https://github.com/user-attachments/assets/4a423e6d-a584-4726-a036-bcfb7b44b296" />


<img width="591" height="606" alt="Screenshot 2026-05-19 224103" src="https://github.com/user-attachments/assets/c8c5b857-ceba-4337-8081-6e0dbc7172a7" />
   
   
LINK : https://youtu.be/RMPhspUNklU?si=jmtTXCUQP3Wsbm-x
