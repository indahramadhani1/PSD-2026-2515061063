Tugas Akhir Percobaan 1

Judul Program : Sistem Antrian Pasien Klinik

Program ini berfungsi sebagai sistem manajemen antrian pasien yang dirancang untuk memudahkan petugas klinik dalam mengatur urutan kedatangan pasien secara terstruktur dan efisien. Dengan menyediakan fitur utama seperti penambahan pasien ke dalam antrian, menampilkan daftar antrian yang sedang menunggu, memanggil pasien sesuai urutan kedatangan, serta menampilkan jumlah total pasien dalam antrian, program ini membantu meningkatkan ketertiban pelayanan di lingkungan klinik. Algoritma dan struktur data yang diterapkan dalam program ini adalah List satu dimensi (array dinamis), di mana setiap elemen pada list merepresentasikan nama pasien yang sedang berada dalam antrian. Sistem bekerja menggunakan konsep FIFO (First In First Out), yaitu pasien yang datang terlebih dahulu akan dipanggil lebih dulu. Implementasi ini memanfaatkan operasi append() untuk menambahkan pasien ke posisi terakhir antrian dan pop(0) untuk mengambil serta menghapus pasien pada posisi pertama. Selain itu, program menggunakan perulangan while sebagai kontrol utama agar sistem dapat berjalan terus sampai pengguna memilih keluar. Struktur percabangan if-elif-else digunakan untuk memproses pilihan menu sesuai kebutuhan pengguna. Program juga dilengkapi dengan error handling menggunakan try-except untuk mencegah kesalahan input ketika pengguna memasukkan data selain angka pada menu utama. Dengan kombinasi algoritma tersebut, program mampu memberikan sistem antrian sederhana yang sistematis, interaktif, dan mudah digunakan.

Source Code :

<img width="520" height="207" alt="Screenshot 2026-04-28 213332" src="https://github.com/user-attachments/assets/691f0409-a234-4169-b07a-ab552793f756" />

<img width="323" height="181" alt="Screenshot 2026-04-28 213413" src="https://github.com/user-attachments/assets/d4240aa6-d7ca-4bc8-87a4-e28fd1b34149" />

<img width="571" height="393" alt="Screenshot 2026-04-28 213516" src="https://github.com/user-attachments/assets/fc6611f9-c853-4959-9d63-8dfa27411284" />

<img width="710" height="289" alt="Screenshot 2026-04-28 213550" src="https://github.com/user-attachments/assets/c6b82cfd-ffdb-4354-b26c-a9c8db154825" />

<img width="835" height="340" alt="Screenshot 2026-04-28 213531" src="https://github.com/user-attachments/assets/255f17a4-5b24-4a24-8588-0f380405ec96" />

<img width="340" height="103" alt="Screenshot 2026-04-28 213556" src="https://github.com/user-attachments/assets/16483c00-7834-4b2e-aab7-d2c50fae3237" />


1. Mendefinisikan fungsi bernama menu untuk membungkus kode yang menampilkan daftar pilihan menu sistem antrian pasien.

2. Mencetak judul sistem ke layar dengan baris baru di awal (\n).

3. Mencetak opsi pertama menu yaitu menampilkan daftar antrian.

4. Mencetak opsi kedua menu yaitu menambah pasien ke antrian.

5. Mencetak opsi ketiga menu yaitu memanggil pasien.

6. Mencetak opsi keempat menu yaitu melihat jumlah antrian.

7. Mencetak opsi nol untuk menghentikan program.

8. Mendefinisikan fungsi utama program tempat seluruh logika inti berjalan.

9. Membuat list kosong bernama antrian untuk menyimpan nama pasien.

10. Membuat variabel running untuk menjaga agar perulangan program tetap berjalan.

11. Memulai perulangan utama selama variabel running bernilai True.

12. Memanggil fungsi menu yang sudah didefinisikan di awal untuk tampil ke layar.

13. Memulai blok penanganan error agar program tidak crash jika user salah input.

14. Mengambil input pilihan menu dari user dan mengubahnya menjadi bilangan bulat (integer).

15. Menangkap error jika user memasukkan sesuatu yang bukan angka (misal: huruf).

16. Menampilkan pesan peringatan jika terjadi ValueError.

17. Mengulang perulangan dari awal menu jika terjadi error input.

18. Mengecek jika user memilih menu nomor 1.

19. Mencetak judul daftar antrian pasien.

20. Mengecek apakah jumlah data pada list antrian sama dengan 0.

21. Jika kosong, menampilkan pesan bahwa antrian masih kosong.

22. Jika tidak kosong, melakukan perulangan untuk menampilkan seluruh pasien dalam antrian.

23. Menampilkan nomor urut pasien beserta nama pasien yang sedang menunggu.

24. Mengecek jika user memilih menu nomor 2.

25. Meminta user memasukkan nama pasien yang akan didaftarkan ke antrian.

26. Menambahkan nama pasien ke bagian belakang list menggunakan fungsi append().

27. Menampilkan pesan bahwa pasien berhasil ditambahkan ke antrian.

28. Mengecek jika user memilih menu nomor 3.

29. Mengecek apakah list antrian kosong.

30. Jika kosong, menampilkan pesan bahwa tidak ada pasien yang dapat dipanggil.

31. Jika tidak kosong, mengambil dan menghapus pasien paling depan menggunakan pop(0).

32. Menyimpan nama pasien yang dipanggil ke variabel panggil.

33. Menampilkan pesan agar pasien tersebut masuk ke ruang pemeriksaan.

34. Mengecek jika user memilih menu nomor 4.

35. Menghitung jumlah pasien dalam antrian menggunakan len(antrian).

36. Menampilkan total pasien yang sedang menunggu.

37. Mengecek jika user memilih menu nomor 0.

38. Mengubah variabel running menjadi False agar perulangan berhenti.

39. Menampilkan pesan Program ditutup. See you next time!

40. Jika user memasukkan angka yang tidak ada di menu.

41. Memberi tahu bahwa pilihan menu tidak tersedia.

42. Baris standar Python untuk memastikan fungsi main() hanya berjalan jika file ini dieksekusi langsung.

43. Memanggil fungsi utama untuk menjalankan seluruh program.

    OUTPUT PROGRAM

    <img width="432" height="873" alt="Screenshot 2026-04-28 234254" src="https://github.com/user-attachments/assets/29434a58-b079-41c8-8521-270cbe32a5e8" />

<img width="610" height="924" alt="Screenshot 2026-04-28 234314" src="https://github.com/user-attachments/assets/1c90c140-7806-47bf-8efd-e115d57cab50" />

<img width="513" height="738" alt="Screenshot 2026-04-28 234328" src="https://github.com/user-attachments/assets/60aaf750-12fd-4bb0-82d7-804e7fac8c1e" />

LINK : https://youtu.be/3xQpoYgUmAA?si=uHpEWyJJ1lyAR6Ga



