class Node:
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor
        self.left = None
        self.right = None


class BSTKontak:
    def __init__(self):
        self.root = None

    # INSERT
    def insert_node(self, root, nama, nomor):

        if root is None:
            return Node(nama, nomor)

        if nama.lower() < root.nama.lower():
            root.left = self.insert_node(root.left, nama, nomor)

        elif nama.lower() > root.nama.lower():
            root.right = self.insert_node(root.right, nama, nomor)

        return root

    def insert(self, nama, nomor):
        self.root = self.insert_node(self.root, nama, nomor)

    # SEARCH
    def search_node(self, root, nama):

        if root is None:
            return None

        if root.nama.lower() == nama.lower():
            return root

        if nama.lower() < root.nama.lower():
            return self.search_node(root.left, nama)

        return self.search_node(root.right, nama)

    def search(self, nama):
        return self.search_node(self.root, nama)

    # INORDER
    def inorder(self, root):

        if root is None:
            return

        self.inorder(root.left)

        print(f"Nama: {root.nama} | Nomor: {root.nomor}")

        self.inorder(root.right)

    # PREORDER
    def preorder(self, root):

        if root is None:
            return

        print(f"Nama: {root.nama} | Nomor: {root.nomor}")

        self.preorder(root.left)
        self.preorder(root.right)

    # POSTORDER
    def postorder(self, root):

        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)

        print(f"Nama: {root.nama} | Nomor: {root.nomor}")

    # COUNT
    def count_nodes(self, root):

        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    # MIN
    def find_min(self, root):

        if root is None:
            return None

        current = root

        while current.left is not None:
            current = current.left

        return current

    # MAX
    def find_max(self, root):

        if root is None:
            return None

        current = root

        while current.right is not None:
            current = current.right

        return current


def main():

    bst = BSTKontak()

    pilih = 0

    while pilih != 8:

        print("\n=== BST Kontak HP ===")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan Kontak (Inorder)")
        print("4. Preorder")
        print("5. Postorder")
        print("6. Kontak Awal (Min)")
        print("7. Kontak Akhir (Max)")
        print("8. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        # TAMBAH KONTAK
        if pilih == 1:

            nama = input("Masukkan nama kontak: ")
            nomor = input("Masukkan nomor HP: ")

            bst.insert(nama, nomor)

            print("Kontak berhasil ditambahkan!")

        # CARI KONTAK
        elif pilih == 2:

            nama = input("Masukkan nama yang dicari: ")

            hasil = bst.search(nama)

            if hasil:
                print("\nKontak ditemukan")
                print(f"Nama  : {hasil.nama}")
                print(f"Nomor : {hasil.nomor}")

            else:
                print("Kontak tidak ditemukan")

        # INORDER
        elif pilih == 3:

            print("\nDaftar Kontak:")
            bst.inorder(bst.root)

        # PREORDER
        elif pilih == 4:

            print("\nPreorder:")
            bst.preorder(bst.root)

        # POSTORDER
        elif pilih == 5:

            print("\nPostorder:")
            bst.postorder(bst.root)

        # MIN
        elif pilih == 6:

            hasil = bst.find_min(bst.root)

            if hasil:
                print("\nKontak pertama:")
                print(f"Nama  : {hasil.nama}")
                print(f"Nomor : {hasil.nomor}")

            else:
                print("Data kosong")

        # MAX
        elif pilih == 7:

            hasil = bst.find_max(bst.root)

            if hasil:
                print("\nKontak terakhir:")
                print(f"Nama  : {hasil.nama}")
                print(f"Nomor : {hasil.nomor}")

            else:
                print("Data kosong")

        # KELUAR
        elif pilih == 8:

            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()