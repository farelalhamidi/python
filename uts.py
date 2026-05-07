class Farel:
    def __init__(self, norek79, nama_nasabah79, alamat_nasabah79, jenis_transaksi79, nominal_transaksi79):
      
        self.norek79 = norek79
        self.nama_nasabah79 = nama_nasabah79
        self.alamat_nasabah79 = alamat_nasabah79
        self.jenis_transaksi79 = jenis_transaksi79
        self.nominal_transaksi79 = nominal_transaksi79
        
        self.next = None
        self.prev = None
  
class BankSistem:
    def __init__(self):
        self.head = None
        self.antrian = []
        self.riwayat = []

 
    def tambah_data(self):
        print("\n--- Tambah Data Nasabah ---")
        norek = input("Nomor Rekening: ")
        nama = input("Nama Nasabah: ")
        alamat = input("Alamat Nasabah: ")
        jenis = input("Jenis Transaksi (misal: Setor Tunai/Tarik Tunai): ")
        nominal = input("Nominal Transaksi: ")

        new_node = Farel(norek, nama, alamat, jenis, nominal)

        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f"Data Nasabah {nama} berhasil ditambahkan.")

    def hapus_data(self, norek_target):
        temp = self.head
        while temp:
            if temp.norek79 == norek_target:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                print(f"Data Nasabah dengan Rekening {norek_target} berhasil dihapus.")
                return
            temp = temp.next
        print("Data Nasabah tidak ditemukan.")

    def tampil_data(self):
        if not self.head:
            print("\nData nasabah masih kosong.")
            return

        print("\n=== DAFTAR DATA NASABAH ===")
        temp = self.head
        while temp:
            print(f"Nomor Rekening  : {temp.norek79}")
            print(f"Nama Nasabah    : {temp.nama_nasabah79}")
            print(f"Alamat Nasabah  : {temp.alamat_nasabah79}")
            print(f"Jenis Transaksi : {temp.jenis_transaksi79}")
            print(f"Nominal         : Rp {temp.nominal_transaksi79}")
            print("-" * 30)
            temp = temp.next

    def ambil_antrian(self):
        if not self.head:
            print("\nData nasabah kosong! Tambahkan data nasabah terlebih dahulu ke sistem.")
            return

        norek_cari = input("Masukkan Nomor Rekening untuk ambil antrian: ")
        temp = self.head
        found = False

        while temp:
            if temp.norek79 == norek_cari:
                self.antrian.append({
                    'norek': temp.norek79,
                    'nama': temp.nama_nasabah79,
                    'jenis': temp.jenis_transaksi79
                })
                print(f"Nasabah {temp.nama_nasabah79} berhasil mengambil antrian.")
                found = True
                break
            temp = temp.next

        if not found:
            print("Nomor Rekening tidak terdaftar. Silahkan tambah data di Menu 1.")

    # 5. Proses Antrian (Queue Dequeue -> Stack Push)
    def proses_antrian(self):
        if len(self.antrian) == 0:
            print("\nTidak ada antrian saat ini.")
        else:
            # Dequeue: Mengeluarkan antrean paling depan (First In First Out)
            diproses = self.antrian.pop(0)
            print(f"\nMemproses transaksi {diproses['jenis']} untuk nasabah {diproses['nama']}...")
            
            # Push: Memasukkan data transaksi yang selesai ke riwayat (Stack)
            self.riwayat.append(diproses)
            print("Transaksi selesai dan telah masuk ke riwayat!")

    # 6. Tampilkan Antrian (Display Queue)
    def tampil_antrian(self):
        if len(self.antrian) == 0:
            print("\nAntrian saat ini kosong.")
        else:
            print("\n=== DAFTAR ANTRIAN SAAT INI ===")
            for i, data in enumerate(self.antrian):
                print(f"Antrian ke-{i + 1}: {data['nama']} (Rek: {data['norek']}) - {data['jenis']}")

    # 7. Riwayat Antrian (Display Stack - LIFO)
    def tampil_riwayat(self):
        if len(self.riwayat) == 0:
            print("\nRiwayat transaksi kosong.")
        else:
            print("\n=== RIWAYAT TRANSAKSI (Terbaru di atas) ===")
            for i in range(len(self.riwayat) - 1, -1, -1):
                data = self.riwayat[i]
                print(f"- {data['nama']} selesai melakukan {data['jenis']} (Rek: {data['norek']})")

    def hapus_riwayat(self):
        if len(self.riwayat) == 0:
            print("\nRiwayat transaksi sudah kosong.")
        else:
            # Pop: Menghapus data riwayat yang paling atas / terakhir kali masuk
            dihapus = self.riwayat.pop()
            print(f"\nRiwayat transaksi terbaru atas nama {dihapus['nama']} berhasil dihapus.")


bank = BankSistem()

while True:
    print("\n=== SISTEM LAYANAN TRANSAKSI BANK ===")
    print("1. Tambah Data Nasabah")
    print("2. Hapus Data Nasabah")
    print("3. Tampilkan Data Nasabah")
    print("4. Ambil Antrian Nasabah")
    print("5. Proses Antrian")
    print("6. Tampilkan Antrian")
    print("7. Riwayat Antrian")
    print("8. Hapus Riwayat")
    print("0. Keluar")

    pilihan = input("Input Pilihan: ")

    if pilihan == "1":
        bank.tambah_data()
    elif pilihan == "2":
        norek_hapus = input("Masukkan Nomor Rekening yang akan dihapus: ")
        bank.hapus_data(norek_hapus)
    elif pilihan == "3":
        bank.tampil_data()
    elif pilihan == "4":
        bank.ambil_antrian()
    elif pilihan == "5":
        bank.proses_antrian()
    elif pilihan == "6":
        bank.tampil_antrian()
    elif pilihan == "7":
        bank.tampil_riwayat()
    elif pilihan == "8":
        bank.hapus_riwayat()
    elif pilihan == "0":
        print("Sistem ditutup. Terima kasih!")
        break
    else:
        print("Pilihan tidak tersedia. Silahkan input kembali.")