Tugas Akhir Percobaan 2

Judul Program : Sistem Antrian Pasien Klinik

Program ini merupakan simulasi sistem sederhana untuk mengelola dan menampilkan ranking skor pemain dalam sebuah game. Pengguna dapat memasukkan data berupa nama pemain dan skor yang diperoleh, kemudian sistem akan mengurutkan data tersebut dari skor tertinggi ke terendah. Hasil akhir berupa daftar pemain yang sudah terurut sehingga mudah untuk melihat siapa yang memiliki skor paling tinggi. Program ini menggunakan algoritma Exchange Sort, yaitu metode pengurutan dengan cara membandingkan setiap elemen dengan elemen lainnya, lalu menukar posisi jika urutannya tidak sesuai. Pendekatan ini cukup sederhana dan mudah dipahami, sehingga cocok digunakan untuk kasus skala kecil seperti data skor pemain.

Source Code :

<img width="697" height="399" alt="Screenshot 2026-05-05 221504" src="https://github.com/user-attachments/assets/fc4cd9d4-f16a-43fd-b5cf-d71dd24caa3a" />


<img width="786" height="629" alt="Screenshot 2026-05-05 221535" src="https://github.com/user-attachments/assets/3d1e83e7-d42f-44c0-ad55-fa76962c50c1" />


<img width="768" height="375" alt="Screenshot 2026-05-05 221547" src="https://github.com/user-attachments/assets/9f56cade-ccae-4a20-a186-971ab5171bfc" />


<img width="480" height="821" alt="Screenshot 2026-05-05 221438" src="https://github.com/user-attachments/assets/dc5626c3-9cb0-4879-80be-ff8e17ab6914" />








1. saya mendefinisikan fungsi tukar, fungsi ini digunakan untuk menukar posisi dua data dalam array.

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
