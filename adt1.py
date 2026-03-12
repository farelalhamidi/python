class Mobil:
    def __init__(self,merk,produk,warna,harga,):
        self.merk = merk
        self.produk = produk
        self.warna = warna
        self.harga = harga
        self.next = None

    def tampilkan (self):
        print ("Tampilkan Merk   :" , self.merk)
        print ("Tampilkan Produk :" , self.produk)
        print ("Tampilkan Warna  :" , self.warna)
        print ("Tampilkan Harga  :" , self.harga)

mobil1 = Mobil ("Innova","Toyota","Hitam",4000000)
mobil2 = Mobil ("Canter","Mitsubishi","Kuning",650000)
mobil3 = Mobil ("avanza","Toyota","Hitam",2000000)
mobil4 = Mobil ("Hilux","Toyata","Putih",650000)

mobil1.next=mobil2
mobil2.next=mobil3
mobil3.next=mobil4

mobil1.tampilkan()
print("\nTampilkan Mobil berikutnya")
mobil1.next.tampilkan()
print("\nTampilkan Mobil berikutnya lagi")
mobil2.next.tampilkan()
print("\nTampilkan Mobil berikutnya lagi")
mobil3.next.tampilkan()