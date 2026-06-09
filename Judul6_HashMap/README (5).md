Tugas Akhir Percobaan 6

Judul Program : Sistem Nilai Mahasiswa Menggunakan Hash Map Open Addressing

Program ini merupakan sistem sederhana untuk mengelola data nilai mahasiswa menggunakan struktur data Hash Map dengan metode Open Addressing (Linear Probing). Setiap data terdiri dari NPM sebagai *key* dan nilai mahasiswa sebagai *value*. Program dapat digunakan untuk menambahkan data mahasiswa, mencari nilai berdasarkan NPM, menghapus data, serta menampilkan seluruh data yang tersimpan dalam hash table. Implementasi program menggunakan class Entry untuk menyimpan pasangan key-value, class SlotState untuk menandai kondisi slot (EMPTY, OCCUPIED, dan DELETED), serta class HashMapOpenAddressing untuk mengelola operasi insert, search, remove, dan display. Collision ditangani menggunakan teknik Linear Probing, yaitu mencari slot kosong berikutnya ketika indeks hasil hash sudah terisi. Pendekatan ini sederhana, efisien, dan cocok digunakan untuk sistem pencarian data mahasiswa karena memungkinkan proses penyimpanan, pencarian, dan penghapusan data dilakukan dengan cepat.

Source Code :




<img width="491" height="484" alt="Screenshot 2026-06-09 201012" src="https://github.com/user-attachments/assets/6574f163-08cb-4048-b960-a2100e0e87be" />





<img width="578" height="497" alt="Screenshot 2026-06-09 201030" src="https://github.com/user-attachments/assets/6791b11d-65d9-4569-a20f-b734f93e2920" />





<img width="596" height="475" alt="Screenshot 2026-06-09 201101" src="https://github.com/user-attachments/assets/ea6b6a1a-46c5-4290-b97e-448b56802213" />




<img width="428" height="443" alt="Screenshot 2026-06-09 201111" src="https://github.com/user-attachments/assets/7a7ce1c0-7469-421b-b955-461cc73ef9f8" />





Mendefinisikan class bernama SlotState yang digunakan untuk menyimpan status setiap slot pada hash table.

Mendefinisikan konstanta EMPTY sebagai penanda bahwa slot masih kosong.

Mendefinisikan konstanta OCCUPIED sebagai penanda bahwa slot sedang digunakan untuk menyimpan data.

Mendefinisikan konstanta DELETED sebagai penanda bahwa data pada slot telah dihapus.

Mendefinisikan class bernama Entry yang digunakan untuk menyimpan pasangan data NPM dan nilai mahasiswa pada hash table.

Mendefinisikan method init pada class Entry untuk menginisialisasi key, value, dan state.

Memberikan nilai awal None pada variabel key sebagai penanda belum ada NPM yang tersimpan.

Memberikan nilai awal None pada variabel value sebagai penanda belum ada nilai mahasiswa yang tersimpan.

Memberikan nilai awal SlotState.EMPTY pada variabel state sebagai penanda slot masih kosong.

Mendefinisikan class bernama HashMapOpenAddressing yang digunakan untuk mengelola data nilai mahasiswa menggunakan Hash Map Open Addressing.

Mendefinisikan method init untuk menginisialisasi ukuran hash table.

Menyimpan ukuran hash table ke dalam variabel SIZE.

Membuat hash table berupa list yang berisi objek Entry sebanyak ukuran yang ditentukan.

Mendefinisikan fungsi hash_function() untuk menghitung indeks penyimpanan berdasarkan NPM mahasiswa.

Menggunakan operasi modulo (%) untuk menghasilkan indeks yang berada dalam rentang ukuran hash table.

Mendefinisikan fungsi insert() untuk menambahkan data nilai mahasiswa ke dalam hash table.

Menghitung indeks awal menggunakan fungsi hash_function().

Membuat variabel first_deleted untuk menyimpan lokasi slot yang berstatus DELETED.

Melakukan perulangan linear probing untuk mencari slot yang tersedia.

Melakukan pengecekan apakah slot sedang digunakan.

Memperbarui nilai jika NPM yang dimasukkan sudah ada pada hash table.

Menyimpan posisi slot DELETED jika ditemukan selama proses pencarian.

Menambahkan data NPM dan nilai mahasiswa ke slot kosong yang ditemukan.

Mengubah status slot menjadi OCCUPIED setelah data berhasil disimpan.

Mengembalikan nilai True jika proses insert berhasil dilakukan.

Mengembalikan nilai False jika hash table sudah penuh.

Mendefinisikan fungsi search() untuk mencari data mahasiswa berdasarkan NPM.

Menghitung indeks awal menggunakan fungsi hash_function().

Melakukan proses linear probing untuk mencari data.

Mengembalikan nilai None jika ditemukan slot EMPTY yang menandakan data tidak ada.

Mengembalikan objek Entry jika NPM ditemukan pada hash table.

Mendefinisikan fungsi remove_key() untuk menghapus data mahasiswa berdasarkan NPM.

Memanggil fungsi search() untuk mencari data yang akan dihapus.

Mengembalikan nilai False jika data tidak ditemukan.

Mengubah status slot menjadi DELETED jika data ditemukan.

Mengembalikan nilai True jika penghapusan berhasil dilakukan.

Mendefinisikan fungsi display() untuk menampilkan seluruh isi hash table.

Menampilkan indeks setiap slot pada hash table.

Menampilkan status EMPTY jika slot masih kosong.

Menampilkan status DELETED jika data pada slot telah dihapus.

Menampilkan pasangan NPM dan nilai mahasiswa jika slot berisi data.

Mendefinisikan fungsi main() sebagai pusat jalannya program.

Membuat objek hashmap dari class HashMapOpenAddressing.

Menambahkan beberapa data mahasiswa menggunakan fungsi insert().

Menampilkan seluruh isi hash table menggunakan fungsi display().

Memanggil fungsi search() untuk mencari data mahasiswa berdasarkan NPM.

Menampilkan nilai mahasiswa jika data ditemukan.

Menampilkan pesan bahwa data tidak ditemukan jika NPM tidak ada pada hash table.

Memanggil fungsi remove_key() untuk menghapus data mahasiswa berdasarkan NPM.

Menampilkan kembali isi hash table setelah proses penghapusan dilakukan.

Melakukan pencarian ulang untuk memastikan data mahasiswa lain masih tersimpan pada hash table.

Menggunakan blok standar Python if name == "main" agar program dapat dijalankan secara langsung.

Memastikan fungsi main() hanya dieksekusi ketika file program dijalankan sebagai program utama.

OUTPUT PROGRAM :

<img width="316" height="449" alt="Screenshot 2026-06-09 200843" src="https://github.com/user-attachments/assets/7e17aed0-8c6f-4344-9fdb-92748008fe7c" />


   
   
LINK : https://youtu.be/94L6wCCygEo?si=Pp9gVpic9J_64Qs6

