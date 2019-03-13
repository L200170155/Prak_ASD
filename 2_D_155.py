Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakKapital(self):
        print(str.upper(self.teks))
    def cetakKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlah(self):
        print("Kalimatku mempunyai: ",len(self.teks),"karakter")
    def perbarui(self, strBaru):
        self.teks = strBaru

    def apaTerkandung(self, isi):
        if str(isi) in self.teks:
            print("true")
        else:
            print("false")
    def hitungV(self):
        v = "aiueoAIUEO"
        n = 0
        for i in self.teks:
            if i in v:
                n+=1
        return n

    def hitungK(self):
        v = "aiueoAIUEO"
        n = 0
        for i in self.teks:
            if i not in v:
                n+=1
        return n

>>> kataku = Pesan("Salatiga")
>>> kataku.apaTerkandung("apa")
false
>>> kataku.apaTerkandung("iga")
true
>>> print(kataku.hitungV())
4
>>> print(kataku.hitungK())
4
>>> 
>>> class Manusia(object):
    """Class manusia dengan inisiasi 'nama'"""
    keadaan='lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapSalam(self):
        print("halo namaku: ", self.nama)
    def makan(self,s):
        print("saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olah(self,k):
        print('saya baru saja latihan', k)
        self.keadaan='lapar'
    def kali(self,n):
        return n*2

>>> from nomor2 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n
        
SyntaxError: multiple statements found while compiling a single statement
>>> 
= RESTART: C:/Users/TYA/AppData/Local/Programs/Python/Python36-32/nomor2.py =
>>> from nomor2 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n
        
SyntaxError: multiple statements found while compiling a single statement
>>> 
= RESTART: C:/Users/TYA/AppData/Local/Programs/Python/Python36-32/nomor2.py =
>>> from nomor2 import Manusia
    class Mahasiswa(Manusia):
	    """Class Mahasiswa yang dibangun dai class Manusia"""
	    def __init__(self,nama,NIM,kota,us):
		self.nama=nama
		self.NIM=NIM
		self.kota=kota
		self.uang=us
	    def __str__(self):
		s=self.nama+',NIM '+str(self.NIM)\
		   +'. tinggal di '+self.kota\
		   +'. uang saku Rp '+str(self.uang)\
		   +'. tiap bulan'
		return s
	    def ambilNama(self):
		return self.nama
	    def ambilNIM(self):
		return self.NIM
	    def ambilUang(self):
		return self.uang
	    def makan(self,s):
		print ("saya baru saja makan",s,"sambil belajar")
		self.keadaan='kenyang'
	    def ambilKota(self):
		return self.kota
	    def perbaruiKota(self,k):
		self.kota=k
	    def tambahUang(self,n):
		self.uang+=n
		
SyntaxError: multiple statements found while compiling a single statement
>>> 
= RESTART: C:/Users/TYA/AppData/Local/Programs/Python/Python36-32/nomor2.py =
>>> class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n

        
>>> ms1=Mahasiswa('Sengkuni',420,'Solo',420000)
>>> print(ms1.ambilKota())
Solo
>>> ms1.perbaruiKota('Jogja')
>>> print(ms1.ambilKota())
Jogja
>>> print(ms1.ambilUang())
420000
>>> ms1.tambahUang(420)
>>> print(ms1.ambilUang())
420420
>>> 
>>> class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n

        
>>> nama = input("Masukkan Nama Anda      : ")
Masukkan Nama Anda      : Yarin Nanditya A
>>> NIM  = input("Masukkan NIM Anda       :")
Masukkan NIM Anda       :L200170155
>>> kota = input("Masukkan Kota Asal Anda :")
Masukkan Kota Asal Anda :Madiun
>>> us   = input("Masukkan Uang Saku Anda :")
Masukkan Uang Saku Anda :1000000
>>> 
>>> ms2 = Mahasiswa(nama,NIM,kota,us)
>>> 
>>> class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    matkul=[]
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n
    def ambilMK(self, mk):
        self.matkul.append(mk)
    def listKuliah(self):
        print(self.matkul)

        
>>> mh3 = Mahasiswa("aa","aa","aa","aa")
>>> mh3.ambilMK("cek")
>>> mh3.listKuliah()
['cek']
>>> mh3.ambilMK("cek2")
>>> mh3.listKuliah()
['cek', 'cek2']
>>> 
>>> class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    matkul=[]
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n
    def ambilMK(self, mk):
        return self.matkul.append(mk)
    def listKuliah(self):
        print(self.matkul)
    def hapusKuliah(self, mk):
        return self.matkul.remove(mk)

>>> mh3 = Mahasiswa("aa","aa","aa","aa")
mh3.ambilMK("cek")
mh3.listKuliah()
SyntaxError: multiple statements found while compiling a single statement
>>> mh3 = Mahasiswa("aa","aa","aa","aa")
>>> mh3.ambilMK("cek")
>>> mh3.listKuliah()
['cek']
>>> mh3.ambilMK("cek2")
>>> mh3.listKuliah()
['cek', 'cek2']
>>> mh3.hapusKuliah("cek")
>>> mh3.listKuliah()
['cek2']
>>> 
>>> class SiswaSMA(Manusia):
    jurusan = "Belum Ditentukan"
    univ = "Belum Ditentukan"
    def __init__(self, nama, nisn, sma):
        self.nama = nama
        self.nisn = nisn
        self.sma = sma
    def __str__(self):
        return "\n\nData Diri\n"\
               +"Nama   : "+self.nama\
               +"\nNISN   : "+str(self.nisn)\
               +"\nSMA    : "+self.sma\
               +"\nUniv Pilihan : "+self.univ\
               +"\nJurusan Pilihan : "+self.jurusan
    def ambil(self):
        print("\n\nUpdate Data Universitas Pilihan...")
        self.univ = input("Pilih Univ : ")
        self.jurusan = input("Ambil Jurusan : ")

        
>>> sis = SiswaSMA("a","a","aa")
>>> print(sis)


Data Diri
Nama   : a
NISN   : a
SMA    : aa
Univ Pilihan : Belum Ditentukan
Jurusan Pilihan : Belum Ditentukan
>>> sis.ambil()


Update Data Universitas Pilihan...
Pilih Univ : Universitas Muhammadiyah Surakarta
Ambil Jurusan : Informatika
>>> print(sis)


Data Diri
Nama   : a
NISN   : a
SMA    : aa
Univ Pilihan : Universitas Muhammadiyah Surakarta
Jurusan Pilihan : Informatika
>>> 
