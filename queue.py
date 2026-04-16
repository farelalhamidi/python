class QueueMahasiswa:
    def __init__(self):
        self.data = []
    # ENQUEUE (tambah data)
    def enqueue(self, nobp, nama, alamat, nohp):
        mahasiswa = {
            "nobp": nobp,
            "nama": nama,
            "alamat": alamat,
            "nohp": nohp
        }
        self.data.append(mahasiswa)
    # DEQUEUE (hapus data depan)
    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        return "Queue kosong"
    # CEK KOSONG
    def is_empty(self):
        return len(self.data) == 0
    # TAMPIL DATA
    def tampil(self):
        if self.is_empty():
            print("Queue kosong")
            return
        print("=== Data Mahasiswa (Queue) ===")
        for mhs in self.data:
            print("NOBP   :", mhs["nobp"])
            print("Nama   :", mhs["nama"])
            print("Alamat :", mhs["alamat"])
            print("No HP  :", mhs["nohp"])
            print("-" * 30)
            
q = QueueMahasiswa()
q.enqueue("221001", "Andi", "Padang", "08123456789")
q.enqueue("221002", "Budi", "Bukittinggi", "08234567890")
q.enqueue("221003", "Citra", "Payakumbuh", "08345678901")
q.enqueue("221004", "Cinta", "Pessel", "08345678901")
q.tampil()
print("\nDequeue data:")
print(q.dequeue())
print("\nSetelah dequeue:")
q.tampil()