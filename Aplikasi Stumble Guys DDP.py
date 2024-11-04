from prettytable import PrettyTable

# Inisialisasi data awal
game_data = {
    "saldo": 0,
    "gems": 0,
    "Kostum": []
}

# Daftar item yang tersedia untuk dibeli (dengan harga dalam gems)
item_shop = {
    "kelinci": 50,
    "Para Smurf": 100,
    "Nerf": 30,
    "Pacman": 20
}

# Kurs konversi saldo ke gems
conversion_rate = 10  # 1 saldo = 10 gems

def tambah_saldo(jumlah):
    """Menambahkan saldo pemain dan mengonversinya ke gems."""
    game_data["saldo"] += jumlah
    gems_ditambah = jumlah * conversion_rate
    game_data["gems"] += gems_ditambah
    print(f"\nSaldo berhasil ditambahkan: {jumlah}.")
    print(f"Gems yang diperoleh dari saldo: {gems_ditambah} gems.")

def tukar_saldo():
    rate = 5  # 1 saldo = 5 gems
    jumlah_saldo = int(input("Masukkan jumlah saldo yang ingin ditukar: "))
    if jumlah_saldo > game_data["saldo"]:
        print("Saldo tidak mencukupi!")
    else:
        game_data["saldo"] -= jumlah_saldo
        game_data["gems"] += jumlah_saldo * rate
        print(f"{jumlah_saldo} saldo berhasil ditukar menjadi {jumlah_saldo * rate} gems.")

def beli_kostum(item):
    """Melakukan pembelian item menggunakan gems."""
    if item in item_shop:
        harga = item_shop[item]
        if game_data["gems"] >= harga:
            game_data["gems"] -= harga
            game_data["Kostum"].append(item)
            print(f"\nBerhasil membeli {item} seharga {harga} gems.")
        else:
            print("\nGems tidak mencukupi untuk membeli item ini.")
    else:
        print("\nItem tidak ditemukan di shop.")

def lihat_status():
    """Menampilkan saldo, gems, dan kostum pemain."""
    print("\n=== Status Pemain ===")
    print(f"Saldo: {game_data['saldo']}")
    print(f"Gems: {game_data['gems']}")
    print(f"Kostum: {', '.join(game_data['Kostum']) if game_data['Kostum'] else 'Kosong'}")

def tampilkan_shop():
    """Menampilkan daftar item yang tersedia di shop."""
    print("\n=== Shop ===")
    for item, harga in item_shop.items():
        print(f"{item}: {harga} gems")

# Program utama
while True:
    print("\n=== Selamat Datang Di Stumble Guys Menu ===")
    print("[1] Tambah Saldo")
    print("[2] Tukar Saldo")
    print("[3] Beli kostum")
    print("[4] Lihat Status")
    print("[5] Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        try:
            jumlah = int(input("\nMasukkan jumlah saldo yang ingin ditambahkan: "))
            if jumlah > 0:
                tambah_saldo(jumlah)
            else:
                print("Jumlah harus lebih besar dari nol.")
        except ValueError:
            print("Masukkan jumlah saldo yang valid.")
    elif pilihan == "2":
        tukar_saldo()
    elif pilihan == "3":
        tampilkan_shop()
        item = input("\nMasukkan nama kostum yang ingin dibeli: ")
        beli_kostum(item)
    elif pilihan == "4":
        lihat_status()
    elif pilihan == "5":
        print("\nTerima kasih telah bermain!")
        break
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")