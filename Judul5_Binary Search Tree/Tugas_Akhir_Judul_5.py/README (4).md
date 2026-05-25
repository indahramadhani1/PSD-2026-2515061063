Tugas Akhir Percobaan 5

Judul Program : Sistem Kontak HP Menggunakan Binary Search Tree (BST)

Program ini merupakan simulasi sistem sederhana untuk mengelola daftar kontak HP menggunakan struktur data Binary Search Tree (BST). Pengguna dapat menambahkan data kontak, mencari kontak berdasarkan nama, menampilkan seluruh daftar kontak secara terurut, melihat kontak dengan nama paling awal maupun paling akhir, serta menghitung jumlah seluruh kontak yang tersimpan. Setiap data kontak terdiri dari nama kontak dan nomor HP. Hasil akhir program berupa informasi data kontak yang berhasil disimpan, hasil pencarian kontak, serta daftar seluruh kontak yang ditampilkan secara alfabetis. Program ini menggunakan struktur data Binary Search Tree (BST), yaitu struktur data pohon biner yang memiliki aturan bahwa data pada subtree kiri lebih kecil dari root dan data pada subtree kanan lebih besar dari root. Implementasi BST dilakukan menggunakan class Node untuk menyimpan data kontak dan pointer ke child kiri maupun kanan, serta class BSTKontak untuk mengatur proses insert, search, traversal, dan operasi lainnya. Traversal inorder digunakan untuk menampilkan daftar kontak secara urut berdasarkan nama. Pendekatan ini sederhana, efisien, dan cocok digunakan untuk sistem pencarian data seperti daftar kontak HP karena mampu mempercepat proses pencarian dan pengelompokan data secara terstruktur.


Source Code :

<img width="1113" height="981" alt="Screenshot 2026-05-25 231339" src="https://github.com/user-attachments/assets/f7ce8097-8e73-47f9-9ea3-79ed13b6e2fa" />


<img width="960" height="892" alt="Screenshot 2026-05-25 231400" src="https://github.com/user-attachments/assets/72ec8db2-3c77-4897-8d26-3e61cbb22247" />


<img width="1119" height="941" alt="Screenshot 2026-05-25 231415" src="https://github.com/user-attachments/assets/a268e782-1fc9-466b-bc0b-165867b95bb9" />


<img width="867" height="977" alt="Screenshot 2026-05-25 231430" src="https://github.com/user-attachments/assets/9bbd5732-c559-4542-be6f-5a375013f511" />


<img width="882" height="992" alt="Screenshot 2026-05-25 231446" src="https://github.com/user-attachments/assets/de9b135b-039c-4eb7-867a-1b7711afe16a" />


<img width="889" height="999" alt="Screenshot 2026-05-25 231504" src="https://github.com/user-attachments/assets/486e5302-e3bf-48ba-a8c8-ab61a33e6775" />


<img width="863" height="993" alt="Screenshot 2026-05-25 231518" src="https://github.com/user-attachments/assets/e3e20040-693a-43f4-b58f-bec2a4fedc41" />





Mendefinisikan class bernama Node yang digunakan untuk menyimpan data kontak HP pada struktur data Binary Search Tree (BST).

Mendefinisikan method __init__ pada class Node untuk menginisialisasi nama kontak, nomor HP, serta pointer child kiri (left) dan child kanan (right).

Menyimpan data nama kontak ke dalam variabel nama.

Menyimpan data nomor HP ke dalam variabel nomor.

Memberikan nilai awal None pada child kiri dan child kanan sebagai penanda bahwa node belum memiliki cabang.

Mendefinisikan class bernama BSTKontak yang digunakan untuk mengelola sistem kontak HP menggunakan struktur data Binary Search Tree.

Mendefinisikan method __init__ untuk menginisialisasi root BST.

Memberikan nilai awal None pada variabel root sebagai penanda bahwa BST masih kosong.

Mendefinisikan fungsi insert_node() untuk menambahkan data kontak baru ke dalam BST.

Melakukan pengecekan apakah node root masih kosong.

Membuat node baru menggunakan class Node jika posisi node masih kosong.

Membandingkan nama kontak baru dengan nama pada node root menggunakan metode lower() agar pencarian tidak membedakan huruf besar dan kecil.

Menambahkan data kontak ke subtree kiri jika nama kontak lebih kecil dari root.

Menambahkan data kontak ke subtree kanan jika nama kontak lebih besar dari root.

Mengembalikan node root setelah proses insert selesai dilakukan.

Mendefinisikan fungsi insert() untuk memanggil fungsi insert_node() dari root utama BST.

Menyimpan hasil insert ke variabel root.

Mendefinisikan fungsi search_node() untuk mencari data kontak berdasarkan nama.

Melakukan pengecekan apakah node yang dicari kosong.

Mengembalikan nilai None jika data kontak tidak ditemukan.

Membandingkan nama kontak yang dicari dengan nama pada node root.

Mengembalikan node jika nama kontak ditemukan.

Melakukan pencarian ke subtree kiri jika nama kontak lebih kecil dari root.

Melakukan pencarian ke subtree kanan jika nama kontak lebih besar dari root.

Mendefinisikan fungsi search() untuk memanggil fungsi search_node() dari root BST.

Mengembalikan hasil pencarian kontak kepada pengguna.

Mendefinisikan fungsi inorder() untuk menampilkan seluruh data kontak secara urut alfabet.

Melakukan traversal ke subtree kiri terlebih dahulu.

Menampilkan data kontak berupa nama dan nomor HP pada node saat ini.

Melakukan traversal ke subtree kanan setelah node ditampilkan.

Mendefinisikan fungsi preorder() untuk menampilkan data BST dengan urutan root, kiri, dan kanan.

Menampilkan data kontak pada node root terlebih dahulu.

Melakukan traversal ke subtree kiri.

Melakukan traversal ke subtree kanan.

Mendefinisikan fungsi postorder() untuk menampilkan data BST dengan urutan kiri, kanan, dan root.

Melakukan traversal ke subtree kiri terlebih dahulu.

Melakukan traversal ke subtree kanan.

Menampilkan data kontak pada node terakhir.

Mendefinisikan fungsi count_nodes() untuk menghitung jumlah seluruh kontak yang tersimpan pada BST.

Mengembalikan nilai 0 jika node kosong.

Menjumlahkan total node dari subtree kiri, subtree kanan, dan node saat ini.

Mendefinisikan fungsi find_min() untuk mencari kontak dengan nama paling awal secara alfabet.

Melakukan pengecekan apakah BST kosong.

Membuat variabel current untuk menelusuri node BST.

Melakukan perulangan menuju child kiri hingga mencapai node paling kiri.

Mengembalikan node paling kiri sebagai data minimum.

Mendefinisikan fungsi find_max() untuk mencari kontak dengan nama paling akhir secara alfabet.

Melakukan pengecekan apakah BST kosong.

Membuat variabel current untuk menelusuri node BST.

Melakukan perulangan menuju child kanan hingga mencapai node paling kanan.

Mengembalikan node paling kanan sebagai data maksimum.

Mendefinisikan fungsi main() sebagai pusat jalannya program.

Membuat objek bst dari class BSTKontak.

Membuat variabel pilih untuk menyimpan pilihan menu dari pengguna.

Menampilkan menu sistem kontak HP menggunakan Binary Search Tree kepada pengguna.

Meminta pengguna memilih menu seperti tambah kontak, cari kontak, menampilkan traversal, dan melihat kontak minimum maupun maksimum.

Menggunakan blok try-except untuk menangani kesalahan input agar program tidak error saat pengguna memasukkan data yang tidak sesuai.

Meminta pengguna memasukkan nama kontak dan nomor HP saat memilih menu tambah kontak.

Memanggil fungsi insert() untuk menambahkan data kontak ke BST.

Menampilkan pesan bahwa kontak berhasil ditambahkan.

Meminta pengguna memasukkan nama kontak saat memilih menu pencarian kontak.

Memanggil fungsi search() untuk mencari data kontak berdasarkan nama.

Menampilkan informasi nama dan nomor HP jika kontak ditemukan.

Menampilkan pesan “Kontak tidak ditemukan” jika data tidak tersedia pada BST.

Memanggil fungsi inorder() saat pengguna ingin melihat daftar kontak secara urut alfabet.

Memanggil fungsi preorder() saat pengguna memilih traversal preorder.

Memanggil fungsi postorder() saat pengguna memilih traversal postorder.

Memanggil fungsi find_min() saat pengguna ingin melihat kontak dengan nama paling awal.

Menampilkan data kontak minimum berupa nama dan nomor HP.

Memanggil fungsi find_max() saat pengguna ingin melihat kontak dengan nama paling akhir.

Menampilkan data kontak maksimum berupa nama dan nomor HP.

Menampilkan pesan “Program selesai.” saat pengguna memilih menu keluar.

Menggunakan blok standar Python if __name__ == "__main__" agar program dapat dijalankan langsung.

Memastikan fungsi main() hanya dijalankan saat file program dieksekusi secara langsung.


    OUTPUT PROGRAM :


<img width="607" height="800" alt="Screenshot 2026-05-25 231148" src="https://github.com/user-attachments/assets/9cefdb16-1ce4-4740-8039-9bc6642c8255" />


<img width="396" height="840" alt="Screenshot 2026-05-25 231203" src="https://github.com/user-attachments/assets/5f7e4643-a833-47b1-b644-c00ef6f54a4a" />


<img width="416" height="833" alt="Screenshot 2026-05-25 231216" src="https://github.com/user-attachments/assets/0c75c8fc-8faa-4283-a3a3-160127a7485e" />


<img width="437" height="835" alt="Screenshot 2026-05-25 231228" src="https://github.com/user-attachments/assets/38e1cb69-ea70-4c87-b795-1b4ab8fded9e" />



<img width="475" height="762" alt="Screenshot 2026-05-25 231238" src="https://github.com/user-attachments/assets/1b9cb2f8-3978-42cf-9395-ce0e78f48979" />


<img width="468" height="845" alt="Screenshot 2026-05-25 231249" src="https://github.com/user-attachments/assets/7cfcf946-1461-424d-b2b7-4031a15fc247" />



<img width="417" height="837" alt="Screenshot 2026-05-25 231303" src="https://github.com/user-attachments/assets/456ed943-1a37-43a1-8292-239d2cce1791" />


<img width="702" height="837" alt="Screenshot 2026-05-25 231314" src="https://github.com/user-attachments/assets/45611779-03d5-4c73-bb7f-42f58cecf01d" />


   
   
LINK : https://youtu.be/GDBdjOfbvcw?si=yd0-HUt0UeqT_nOd
