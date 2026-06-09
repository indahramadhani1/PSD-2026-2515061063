class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True

            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True

        return False

    def search(self, key):
        idx = self.hash_function(key)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]

        return None

    def remove_key(self, key):
        entry = self.search(key)

        if entry is None:
            return False

        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nData Nilai Mahasiswa:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")

            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")

            else:
                print(f"NPM: {self.table[i].key}, Nilai: {self.table[i].value}")


def main():
    nilai_mahasiswa = HashMapOpenAddressing()

    nilai_mahasiswa.insert(2515051065, 85)
    nilai_mahasiswa.insert(2515051075, 90)
    nilai_mahasiswa.insert(2515051085, 78)
    nilai_mahasiswa.insert(2515051095, 88)

    nilai_mahasiswa.display()

    hasil = nilai_mahasiswa.search(2515051075)

    if hasil is not None:
        print(f"\nNPM {hasil.key} ditemukan")
        print(f"Nilai = {hasil.value}")
    else:
        print("\nData mahasiswa tidak ditemukan")

    nilai_mahasiswa.remove_key(2515051075)

    print("\nSetelah data mahasiswa dihapus:")
    nilai_mahasiswa.display()

    hasil = nilai_mahasiswa.search(2515051085)

    if hasil is not None:
        print(f"\nNPM {hasil.key} masih ditemukan")
        print(f"Nilai = {hasil.value}")
    else:
        print("\nData mahasiswa tidak ditemukan")


if __name__ == "__main__":
    main()