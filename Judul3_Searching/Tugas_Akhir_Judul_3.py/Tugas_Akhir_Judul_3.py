def sequential_search(data, n, target):
    i = 0
    counter = 0

    while i < n:
        print(f"Mengecek nama: {data[i]}")

        if data[i] == target:
            counter += 1

        i += 1

    return counter


def main():
    data = [
        "Adel", "Bianca", "Caca", "Dina", "Adel" ,
        "Faris", "Devikha", "Adel", "Sania" , "Rizky"
    ]

    n = len(data)

    print(f"Daftar hadir: {data}")

    target = input("Masukkan nama yang ingin dicari: ")

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Nama {target} ditemukan sebanyak {counter} kali.")
    else:
        print(f"Nama {target} tidak ditemukan.")


if __name__ == "__main__":
    main()