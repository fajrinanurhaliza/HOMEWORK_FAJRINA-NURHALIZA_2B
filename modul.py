barang = []

def menu():
    print("Selamat datang di Program Manajemen Stok Barang!")
    print("Pilihan : ")
    print("1. Tambah Barang")
    print("2. Edit Barang")
    print("3. Hapus Barang")
    print("4. Cari Barang")
    print("5. Tampilkan data Barang")
    print("6. Tampilkan Jumlah Barang")
    print("7. Keluar")
    print(25*'=')

def tambah():
    nama = str(input("Masukkan Nama Barang : "))
    stok = int(input("Masukkan Stok Barang : "))

    barang_new = {'name' : nama, 'stok' : stok}
    barang.append(barang_new)
    print("Barang berhasil ditambahkan.")
    print(25*'=')

def edit():
    nama_barang = str(input("Masukkan Nama Barang yang ingin diedit: "))
    for i in barang:
        if nama_barang.lower() == i['name'].lower():
            new_stok = int(input(f"Masukkan Jumlah Stok baru untuk {nama_barang}: "))
            i['stok'] = new_stok
            print(f"Stok Barang {nama_barang} berhasil diubah.")
            return
    print("Maaf, Barang tidak ditemukan.")
    print(25*'=')

def delete():
    hapus=int(input("Masukkan index : "))
    barang.pop(hapus)
    print("Barang berhasil dihapus.")
    print(25*'=')

def cari_data():
    if barang:
        kata = str(input("Cari Nama Barang: "))
        ditemukan = False
        for i in barang:
            if kata.lower() in i['name'].lower():
                print("==== HASIL PENCARIAN ====")
                print(f"- {i['name']} stock {i['stok']}")
                ditemukan = True
        if not ditemukan:
            print("Maaf, Barang tidak ditemukan.")
    else:
        print("Maaf, Barang tidak ditemukan.")
        print(25*'=')

def tampilkan_data():
    print("==== TAMPILAN DATA BARANG ====")
    for i in barang:
        print('-',i['name'], i['stok'])
        print(25*'=')

def tampilkan_jumlah_barang():
    print("==== JUMLAH BARANG ====")
    total_stok = 0
    for i in barang:
        print(f"{i['name']}: {i['stok']}")
        total_stok += i['stok']
    print(f"\nTotal jumlah barang: {len(barang)}")
    print(f"Total stok barang: {total_stok}")
