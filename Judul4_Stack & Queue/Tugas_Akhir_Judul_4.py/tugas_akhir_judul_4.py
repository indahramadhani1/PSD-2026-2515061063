class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    # Mengecek apakah antrian kosong
    def is_empty(self):
        return self.front_idx == -1

    # Mengecek apakah antrian penuh
    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    # Menambahkan pemesan tiket
    def enqueue(self, pemesan):
        if self.is_full():
            print("Antrian pemesanan penuh!")
            return

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = pemesan
        print(f"Pemesanan tiket atas nama {pemesan['nama']} berhasil ditambahkan")

    # Melayani pemesan tiket
    def dequeue(self):
        if self.is_empty():
            print("Antrian pemesanan kosong!")
            return

        pemesan = self.q[self.front_idx]

        print("\n=== Pemesan Sedang Dilayani ===")
        print(f"Nama Pemesan : {pemesan['nama']}")
        print(f"Film         : {pemesan['film']}")
        print(f"Jumlah Tiket : {pemesan['jumlah_tiket']}")

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    # Melihat antrian paling depan
    def peek(self):
        if self.is_empty():
            print("Antrian kosong!")
            return

        pemesan = self.q[self.front_idx]

        print("\n=== Antrian Paling Depan ===")
        print(f"Nama Pemesan : {pemesan['nama']}")
        print(f"Film         : {pemesan['film']}")
        print(f"Jumlah Tiket : {pemesan['jumlah_tiket']}")

    # Menampilkan seluruh antrian
    def display(self):
        if self.is_empty():
            print("Antrian kosong!")
            return

        print("\n=== DAFTAR ANTRIAN PEMESANAN TIKET BIOSKOP ===")

        i = self.front_idx
        nomor = 1

        while True:
            pemesan = self.q[i]

            print(f"\nAntrian Ke-{nomor}")
            print(f"Nama Pemesan : {pemesan['nama']}")
            print(f"Film         : {pemesan['film']}")
            print(f"Jumlah Tiket : {pemesan['jumlah_tiket']}")

            if i == self.rear_idx:
                break

            i = (i + 1) % self.MAXN
            nomor += 1


def main():
    queue = QueueArray()
    pilih = 0

    while pilih != 5:
        print("\n=====================================")
        print(" SISTEM ANTRIAN TIKET BIOSKOP ONLINE ")
        print("=====================================")
        print("1. Tambah Pemesan")
        print("2. Layani Pemesan")
        print("3. Lihat Antrian Depan")
        print("4. Tampilkan Semua Antrian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih Menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            nama = input("Nama Pemesan : ")
            film = input("Judul Film   : ")

            try:
                jumlah = int(input("Jumlah Tiket : "))
            except ValueError:
                print("Jumlah tiket harus angka!")
                continue

            data_pemesan = {
                "nama": nama,
                "film": film,
                "jumlah_tiket": jumlah
            }

            queue.enqueue(data_pemesan)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()