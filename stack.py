class StackMahasiswa:
    def __init__(self):
        self.data = []
    
    def push(self, nobp, nama, alamat, nohp):
        mahasiswa = {
            "nobp": nobp,
            "nama": nama,
            "alamat": alamat,
            "nohp": nohp
        }
        self.data.append(mahasiswa)
    # POP (hapus data terakhir)
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return "Stack kosong"
    # CEK KOSONG
    def is_empty(self):
        return len(self.data) == 0
    # TAMPIL DATA
    def tampil(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print("=== Data Mahasiswa (Stack) ===")
        for mhs in reversed(self.data):
            print("NOBP   :", mhs["nobp"])
            print("Nama   :", mhs["nama"])
            print("Alamat :", mhs["alamat"])
            print("No HP  :", mhs["nohp"])
            print("-" * 30)
            
s = StackMahasiswa()
s.push("221001", "Andi", "Padang", "08123456789")
s.push("221002", "Budi", "Bukittinggi", "08234567890")
s.push("221003", "Citra", "Payakumbuh", "08345678901")
s.push("221004", "Cinta", "Pessel", "08345678902")
s.tampil()
print("\nPop data:")
print(s.pop())
print("\nSetelah pop:")
s.tampil()