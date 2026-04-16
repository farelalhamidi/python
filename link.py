class Node:
    def __init__(self, no_kamar, nama_penghuni, jumlah_bayar):
        self.no_kamar = no_kamar
        self.nama_penghuni = nama_penghuni
        self.jumlah_bayar = jumlah_bayar
        self.next = None
        self.prev = None

class KostDoubleList:
    def __init__(self):
        self.head = None

    def insert_akhir(self, no_kamar, nama_penghuni, jumlah_bayar):
        new_node = Node(no_kamar, nama_penghuni, jumlah_bayar)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def cetak_header(self, judul):
        print(f"\n{'='*55}")
        print(f"{judul.center(55)}")
        print(f"{'='*55}")
        print(f"{'NO. KAMAR':<12} | {'NAMA PENGHUNI':<20} | {'TOTAL BAYAR'}")
        print(f"{'-'*55}")

    def tampil_rapi(self):
        self.cetak_header("DAFTAR PEMBAYARAN KOST")
        temp = self.head
        if not temp:
            print(f"{'Data Kosong'.center(55)}")
        else:
            total_seluruh = 0
            while temp:
                print(f"{temp.no_kamar:<12} | {temp.nama_penghuni:<20} | Rp{temp.jumlah_bayar:>12,}")
                total_seluruh += temp.jumlah_bayar
                temp = temp.next
            print(f"{'-'*55}")
            print(f"{'TOTAL PENDAPATAN':<35} | Rp{total_seluruh:>12,}")
        print(f"{'='*55}")

    def delete(self, no_kamar):
        temp = self.head
        while temp:
            if temp.no_kamar == no_kamar:
                if temp == self.head:
                    self.head = temp.next
                    if self.head: self.head.prev = None
                else:
                    if temp.next: temp.next.prev = temp.prev
                    if temp.prev: temp.prev.next = temp.next
                print(f"\n[SISTEM] Sukses menghapus Kamar: {no_kamar}")
                return
            temp = temp.next
        print(f"\n[SISTEM] Data Kamar {no_kamar} tidak ditemukan.")

# --- Demo Tampilan Rapi ---
kost = KostDoubleList()

# Menambah Data
kost.insert_akhir("A-01", "Rizky Fauzi", 850000)
kost.insert_akhir("B-05", "Siti Aminah", 1200000)
kost.insert_akhir("VIP-2", "Budi Santoso", 2500000)
kost.insert_akhir("A-03", "Dewi Lestari", 850000)

# Menampilkan Tabel
kost.tampil_rapi()

# Menghapus satu data dan tampilkan lagi
kost.delete("B-05")
kost.tampil_rapi()