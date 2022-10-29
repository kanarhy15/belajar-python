#MEMBUAT STRUK BELANJA
import datetime

waktu = datetime.datetime.now()
print(waktu.strftime("%X"))

#nama kasir
namakasir = input("masukkan nama kasir:")
#tampilan awal
print("""
PT INDOMARCO PRISTAMA GEDUNG MENARA INDOMARET BOULEVARD PANTAI 
INDAH KAPUK JAKARTA UTARA
NPWP 01.337.994.6.6-092.000
        KPR PAM
        JLN.MELATI N0., KLAGETE
        KEC.SORONG UTARA, SORONG,98416
 -------------------------------------
 """)

tambahbarang = 'y'
while 'y' in tambahbarang :

   namabarang =input("masukkan nama barang: ")

   hargabarang =int(input("masukkan harga barang"))

   jumlahbarang =int(input("masukkan jumlah barang"))

   hargatotal = jumlahbarang * hargabarang
   #tampilkan barang
   print(f"""
   -------------------------------------------------
   {namabarang} {jumlahbarang} Rp.{hargatotal}
   -------------------------------------------------
  """)
   tambahbarang = input("apakah ingin mengscan barang lagi ?").lower()
print("terima kasih telah berbelanja")
