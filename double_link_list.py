class Node:
    def __init__(self, nobp, nama, alamat, nohp):
        self.nobp = nobp
        self.nama = nama
        self.alamat = alamat
        self.nohp = nohp
        #DoubleLinkList(Maju dan Mundur)
        self.prev = None
        self.next = None



class DoubleMahasiswaList:

    def __init__(self):
        self.head = None


    # 3. Insert di Depan
    def insert_depan(self, nobp, nama, alamat, nohp):

        new_node = Node(nobp, nama, alamat, nohp)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node


    def insert_belakang(self, nobp, nama, alamat, nohp):

        new_node = Node(nobp, nama, alamat, nohp)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp


    def tampil_maju(self):

        if self.head is None:
            print("Data kosong")
            return

        temp = self.head

        while temp:
            print("NOBP   :", temp.nobp)
            print("Nama   :", temp.nama)
            print("Alamat :", temp.alamat)
            print("No HP  :", temp.nohp)
            print("-" * 30)

            temp = temp.next


    def tampil_mundur(self):

        if self.head is None:
            print("Data kosong")
            return

        temp = self.head

        # menuju node terakhir
        while temp.next:
            temp = temp.next

        # traversal mundur
        while temp:
            print("NOBP   :", temp.nobp)
            print("Nama   :", temp.nama)
            print("Alamat :", temp.alamat)
            print("No HP  :", temp.nohp)
            print("-" * 30)

            temp = temp.prev


    def delete(self, nobp):

        if self.head is None:
            print("Data kosong")
            return

        temp = self.head

        while temp:
            if temp.nobp == nobp:

                # jika node pertama (head)
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None

                # jika node di tengah atau akhir
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev

                print("Data berhasil dihapus")
                return

            temp = temp.next

        print("Data tidak ditemukan")


# =========================================
# PROGRAM UTAMA
# =========================================

mhs = DoubleMahasiswaList()


mhs.insert_depan("221001", "Andi", "Padang", "08123456789")
mhs.insert_depan("221002", "Budi", "Bukittinggi", "08234567890")
mhs.insert_belakang("221003", "Citra", "Payakumbuh", "08345678901")
mhs.insert_belakang("221004", "Dina", "Solok", "08456789012")

print("=== Data Mahasiswa (Maju) ===")
mhs.tampil_maju()

print("\nMenghapus data NOBP 221003\n")
mhs.delete("221003")

print("\n=== Data Setelah Dihapus ===")
mhs.tampil_maju()

print("\n=== Data Mahasiswa (Mundur) ===")
mhs.tampil_mundur()