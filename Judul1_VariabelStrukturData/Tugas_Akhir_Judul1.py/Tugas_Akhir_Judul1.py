def menu():
    print("\nSISTEM ANTRIAN PASIEN KLINIK")
    print("1. Tampilkan Daftar Antrian")
    print("2. Tambah Pasien ke Antrian")
    print("3. Panggil Pasien")
    print("4. Lihat Jumlah Antrian")
    print("0. Keluar")

def main():
    antrian = []

    running = True
    while running:
        menu()

        try:
            choice = int(input("Pilih menu : "))
        except ValueError:
            print("Masukkan angka yang ada di menu.")
            continue

        if choice == 1:
            print("\nDAFTAR ANTRIAN PASIEN")
            if len(antrian) == 0:
                print("Antrian masih kosong.")
            else:
                for i in range(len(antrian)):
                    print(f"{i+1}. {antrian[i]}")

        elif choice == 2:
            nama = input("Masukkan nama pasien : ")
            antrian.append(nama)
            print(f"{nama} berhasil ditambahkan ke antrian.")

        elif choice == 3:
            if len(antrian) == 0:
                print("Antrian kosong, tidak ada pasien dipanggil.")
            else:
                panggil = antrian.pop(0)
                print(f"Pasien {panggil} silakan masuk ke ruang pemeriksaan.")

        elif choice == 4:
            print(f"Jumlah pasien dalam antrian : {len(antrian)}")

        elif choice == 0:
            running = False
            print("Program ditutup.")

        else:
            print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    main() 