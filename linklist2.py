class Node:
    def __init__(self, no_kamar, nama_penghuni, jumlah_bayar):
        self.no_kamar = no_kamar
        self.nama_penghuni = nama_penghuni
        self.jumlah_bayar = jumlah_bayar
        self.next = None

class KostList:
    def __init__(self):
        self.head = None

    # Tambah pembayaran baru di urutan paling depan
    def insert_awal(self, no_kamar, nama_penghuni, jumlah_bayar):
        new_node = Node(no_kamar, nama_penghuni, jumlah_bayar)
        new_node.next = self.head
        self.head = new_node

    # Tambah pembayaran baru paling belakang
    def insert_akhir(self, no_kamar, nama_penghuni, jumlah_bayar):
        new_node = Node(no_kamar, nama_penghuni, jumlah_bayar)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Menampilkan semua riwayat
    def tampil(self):
        temp = self.head
        if not temp:
            print("Belum ada data pembayaran.")
            return
        
        print(f"{'Kamar':<8} | {'Nama Penghuni':<15} | {'Total Bayar'}")
        print("-" * 40)
        while temp:
            print(f"{temp.no_kamar:<8} | {temp.nama_penghuni:<15} | Rp{temp.jumlah_bayar:,}")
            temp = temp.next

    # Menghapus data 
    def delete(self, no_kamar):
        temp = self.head

        # Jika data yang dihapus ada di Head (awal)
        if temp and temp.no_kamar == no_kamar:
            self.head = temp.next
            print(f"Data Kamar {no_kamar} berhasil dihapus.")
            return

        prev = None
        while temp and temp.no_kamar != no_kamar:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Data Kamar {no_kamar} tidak ditemukan.")
            return

        prev.next = temp.next
        print(f"Data Kamar {no_kamar} berhasil dihapus.")


kost = KostList()

# input 
kost.insert_akhir("A01", "Andika", 800000)
kost.insert_akhir("A02", "Bagus", 750000)
kost.insert_akhir("B05", "Chandra", 1200000)
kost.insert_awal("VIP-1", "Deni", 2500000)

print("RIWAYAT PEMBAYARAN KOST:")
kost.tampil()

print("\n--- Menghapus Data Kamar A02 ---")
kost.delete("A02")

print("\nRIWAYAT PEMBAYARAN TERBARU:")
kost.tampil()