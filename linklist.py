class Node:
    def __init__(self, nobp, nama, alamat):
        self.nobp = nobp
        self.nama = nama
        self.alamat = alamat
        self.next = None


class MahasiswaList:
    def __init__(self):
        self.head = None

    def insert_awal(self, nobp, nama, alamat):
        new_node = Node(nobp, nama, alamat)

        new_node.next = self.head
        self.head = new_node

    def insert_akhir(self, nobp, nama, alamat):
        new_node = Node(nobp, nama, alamat)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
  
    def tampil(self):
        temp = self.head

        while temp:
            print("NOBP   :", temp.nobp)
            print("Nama   :", temp.nama)
            print("Alamat :", temp.alamat)
            print("-" * 20)

            temp = temp.next


    def delete(self, nobp):

        temp = self.head

        if temp and temp.nobp == nobp:
            self.head = temp.next
            return

        prev = None

        while temp and temp.nobp != nobp:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Data tidak ditemukan")
            return

        prev.next = temp.next

mhs = MahasiswaList()


mhs.insert_awal("22001", "Andi", "Padang")

mhs.insert_akhir("22002", "Budi", "Bukittinggi")
mhs.insert_akhir("22003", "Citra", "Solok")
mhs.insert_akhir("22004", "Habib", "Padang Panjang")

print("Data Mahasiswa:")
mhs.tampil()

print("\nSetelah delete data Citra")

mhs.delete("22003")

mhs.tampil()