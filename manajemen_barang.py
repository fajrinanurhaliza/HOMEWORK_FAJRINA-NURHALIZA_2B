import modul

def main():
    while True:
        modul.menu()
        pilihan = input("Masukkan Pilihan : ")
        if pilihan == '1':
            modul.tambah()
        if pilihan == '2':
            modul.edit()
        if pilihan == '3':
            modul.delete()
        if pilihan == '4':
            modul.cari_data()
        if pilihan == '5':
            modul.tampilkan_data()
        if pilihan == '6':
            modul.tampilkan_jumlah_barang()
        if pilihan == '7':
            print("Terima kasih telah menggunakan program manajemen stok barang ini.")
if __name__ == "__main__":
    main()