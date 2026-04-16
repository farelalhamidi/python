
class Farel:
    def __init__(self, id_pengunjung79, nama79, no_hp79, fakultas79, prodi79):
        self.id_pengunjung = str(id_pengunjung79) + " 02" 
        self.nama = nama79
        self.no_hp = no_hp79
        self.fakultas = fakultas79
        self.prodi = prodi79
        self.next = None    
        self.prev = None

class Perpustakaan:
    def __init__(self):
        self.head = None

    def input_data(self):
        print("\n--- Input Data Pengunjung ---")
        id_input = input("ID Pengunjung (2 digit awal): ")
        nama = input("Nama Pengunjung: ")
        no_hp = input("No HP: ")
        fakultas = input("Fakultas: ")
        prodi = input("Prodi: ")
        
        new_node = Farel(id_input, nama, no_hp, fakultas, prodi)
        
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f"Data {nama} berhasil ditambahkan dengan ID: {new_node.id_pengunjung}")

    def tampil_data(self):
        if not self.head:
            print("\nData pengunjung kosong.")
            return
        
        print("\n=== DAFTAR PENGUNJUNG PERPUSTAKAAN ===")
        temp = self.head
        while temp:
            print(f"ID       : {temp.id_pengunjung}")
            print(f"Nama     : {temp.nama}")
            print(f"No HP    : {temp.no_hp}")
            print(f"Fakultas : {temp.fakultas}")
            print(f"Prodi    : {temp.prodi}")
            print("-" * 30)
            temp = temp.next

    def hapus_data(self, id_target):
        temp = self.head
        while temp:
            if temp.id_pengunjung == id_target:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                
                if temp.next:
                    temp.next.prev = temp.prev
                
                print(f"Data dengan ID {id_target} berhasil dihapus.")
                return
            temp = temp.next
        print("Data tidak ditemukan.")


perpus = Perpustakaan()

while True:
    print("\n= Menu Pengunjung Pustaka =")
    print("1. Input Data Pengunjung")
    print("2. Tampil Data Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")
    
    pilihan = input("Input Pilihan: ")

    if pilihan == "1":
        perpus.input_data()
    elif pilihan == "2":
        perpus.tampil_data()    
    elif pilihan == "3":
        id_hapus = input("Masukkan ID Pengunjung yang akan dihapus: ")
        perpus.hapus_data(id_hapus)
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak tersedia.")