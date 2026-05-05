Tugas Akhir Percobaan 2

Judul Program : Sistem Antrian Pasien Klinik

Program ini berfungsi sebagai sistem manajemen antrian pasien yang dirancang untuk memudahkan petugas klinik dalam mengatur urutan kedatangan pasien secara terstruktur dan efisien. Dengan menyediakan fitur utama seperti penambahan pasien ke dalam antrian, menampilkan daftar antrian yang sedang menunggu, memanggil pasien sesuai urutan kedatangan, serta menampilkan jumlah total pasien dalam antrian, program ini membantu meningkatkan ketertiban pelayanan di lingkungan klinik. Algoritma dan struktur data yang diterapkan dalam program ini adalah List satu dimensi (array dinamis), di mana setiap elemen pada list merepresentasikan nama pasien yang sedang berada dalam antrian. Sistem bekerja menggunakan konsep FIFO (First In First Out), yaitu pasien yang datang terlebih dahulu akan dipanggil lebih dulu. Implementasi ini memanfaatkan operasi append() untuk menambahkan pasien ke posisi terakhir antrian dan pop(0) untuk mengambil serta menghapus pasien pada posisi pertama. Selain itu, program menggunakan perulangan while sebagai kontrol utama agar sistem dapat berjalan terus sampai pengguna memilih keluar. Struktur percabangan if-elif-else digunakan untuk memproses pilihan menu sesuai kebutuhan pengguna. Program juga dilengkapi dengan error handling menggunakan try-except untuk mencegah kesalahan input ketika pengguna memasukkan data selain angka pada menu utama. Dengan kombinasi algoritma tersebut, program mampu memberikan sistem antrian sederhana yang sistematis, interaktif, dan mudah digunakan.

Source Code :

<img width="520" height="207" alt="Screenshot 2026-04-28 213332" src="https://github.com/user-attachments/assets/691f0409-a234-4169-b07a-ab552793f756" />

<img width="323" height="181" alt="Screenshot 2026-04-28 213413" src="https://github.com/user-attachments/assets/d4240aa6-d7ca-4bc8-87a4-e28fd1b34149" />

<img width="571" height="393" alt="Screenshot 2026-04-28 213516" src="https://github.com/user-attachments/assets/fc6611f9-c853-4959-9d63-8dfa27411284" />

<img width="710" height="289" alt="Screenshot 2026-04-28 213550" src="https://github.com/user-attachments/assets/c6b82cfd-ffdb-4354-b26c-a9c8db154825" />

<img width="835" height="340" alt="Screenshot 2026-04-28 213531" src="https://github.com/user-attachments/assets/255f17a4-5b24-4a24-8588-0f380405ec96" />

<img width="340" height="103" alt="Screenshot 2026-04-28 213556" src="https://github.com/user-attachments/assets/16483c00-7834-4b2e-aab7-d2c50fae3237" />


1. saya mendefinisikan fungsi tukar, fungsi ini digunakan untuk menukar posisi dua data dalam array.
2. 
3. Mencetak judul sistem ke layar dengan baris baru di awal (\n).

4. Mencetak opsi pertama menu yaitu menampilkan daftar antrian.

5. Mencetak opsi kedua menu yaitu menambah pasien ke antrian.

6. Mencetak opsi ketiga menu yaitu memanggil pasien.

7. Mencetak opsi keempat menu yaitu melihat jumlah antrian.

8. Mencetak opsi nol untuk menghentikan program.

9. Mendefinisikan fungsi utama program tempat seluruh logika inti berjalan.

10. Membuat list kosong bernama antrian untuk menyimpan nama pasien.

11. Membuat variabel running untuk menjaga agar perulangan program tetap berjalan.

12. Memulai perulangan utama selama variabel running bernilai True.

13. Memanggil fungsi menu yang sudah didefinisikan di awal untuk tampil ke layar.

14. Memulai blok penanganan error agar program tidak crash jika user salah input.

15. Mengambil input pilihan menu dari user dan mengubahnya menjadi bilangan bulat (integer).

16. Menangkap error jika user memasukkan sesuatu yang bukan angka (misal: huruf).

17. Menampilkan pesan peringatan jika terjadi ValueError.

18. Mengulang perulangan dari awal menu jika terjadi error input.

19. Mengecek jika user memilih menu nomor 1.

20. Mencetak judul daftar antrian pasien.

21. Mengecek apakah jumlah data pada list antrian sama dengan 0.

22. Jika kosong, menampilkan pesan bahwa antrian masih kosong.

23. Jika tidak kosong, melakukan perulangan untuk menampilkan seluruh pasien dalam antrian.

24. Menampilkan nomor urut pasien beserta nama pasien yang sedang menunggu.

25. Mengecek jika user memilih menu nomor 2.

26. Meminta user memasukkan nama pasien yang akan didaftarkan ke antrian.

27. Menambahkan nama pasien ke bagian belakang list menggunakan fungsi append().

28. Menampilkan pesan bahwa pasien berhasil ditambahkan ke antrian.

29. Mengecek jika user memilih menu nomor 3.

30. Mengecek apakah list antrian kosong.

31. Jika kosong, menampilkan pesan bahwa tidak ada pasien yang dapat dipanggil.

32. Jika tidak kosong, mengambil dan menghapus pasien paling depan menggunakan pop(0).

33. Menyimpan nama pasien yang dipanggil ke variabel panggil.

34. Menampilkan pesan agar pasien tersebut masuk ke ruang pemeriksaan.

35. Mengecek jika user memilih menu nomor 4.

36. Menghitung jumlah pasien dalam antrian menggunakan len(antrian).

37. Menampilkan total pasien yang sedang menunggu.

38. Mengecek jika user memilih menu nomor 0.

39. Mengubah variabel running menjadi False agar perulangan berhenti.

40. Menampilkan pesan Program ditutup. See you next time!

41. Jika user memasukkan angka yang tidak ada di menu.

42. Memberi tahu bahwa pilihan menu tidak tersedia.

43. Baris standar Python untuk memastikan fungsi main() hanya berjalan jika file ini dieksekusi langsung.

44. Memanggil fungsi utama untuk menjalankan seluruh program.
