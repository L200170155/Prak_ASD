Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

        
>>> c0 = MhsTif("Ika", 10, "Sukoharjo", 240000)
>>> c1 = MhsTif("Budi", 51, "Sragen", 230000)
>>> c2 = MhsTif("Ahmad", 2, "Surakarta", 250000)
>>> c3 = MhsTif("Chandra", 18, "Surakarta", 235000)
>>> c4 = MhsTif("Eka", 4, "Boyolali", 240000)
>>> c5 = MhsTif("Fandi", 31, "Salatiga", 250000)
>>> c6 = MhsTif("Deni", 13, "Klaten", 245000)
>>> c7 = MhsTif("Galuh", 5, "Wonogiri", 245000)
>>> c8 = MhsTif("Janto", 23, "Klaten", 245000)
>>> c9 = MhsTif("Hasan", 64, "Karanganyar", 270000)
>>> c10 = MhsTif("Khalid", 29, "Purwodadi", 265000)
>>> 
>>> Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
>>> 
>>> #----------------------------------- NOMER 1 ------------------------------#
>>> 
>>> def cariKotaTinggal(list, target):
    a = []
    for i in list :
        if i.kotaTinggal == target:
            a.append(list.index(i))
    return a

>>> a = cariKotaTinggal(Daftar, "Klaten")
>>> print(a)
[6, 8]
>>> 
>>> #----------------------------------- NOMER 2 ------------------------------#
>>> 
>>> def cariUangSakuTerkecil(list):
    temp = list[0].uangSaku
    for i in list[1:]:
        if i.uangSaku < temp:
            temp = i.uangSaku
    return temp

>>> a = cariUangSakuTerkecil(Daftar)
>>> print(a)
230000
>>> 
>>> #----------------------------------- NOMER 3 ------------------------------#
>>> 
>>> def cariUangSakuTerkecilObject(list):
    temp = [list[0]]
    for i in list[1:]:
        if i.uangSaku < temp[0].uangSaku:
            temp = [i]
        elif i.uangSaku == temp[0].uangSaku:
            temp.append(i)
    return temp

>>> a = cariUangSakuTerkecilObject(Daftar)
>>> print(a)
[<__main__.MhsTif object at 0x064639F0>]
>>> 
>>> #----------------------------------- NOMER 4 ------------------------------#
>>> 
>>> def cariUangSakuKurang250k(list):
    temp = []
    for i in list:
        if i.uangSaku < 250000:
            temp.append(i)
    return temp

>>> a = cariUangSakuKurang250k(Daftar)
>>> for i in a:
    print(i.nama)

    
Ika
Budi
Chandra
Eka
Deni
Galuh
Janto
>>> 
>>> #----------------------------------- NOMER 5 ------------------------------#
>>> 
>>> def cariLinkedList(head, target):
    temp = head
    while temp.data != None:
        if temp.data == target:
            return temp
    return -1

>>> #----------------------------------- NOMER 6 ------------------------------#
>>> 
>>> def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

>>> kumpulan = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
>>> print(binSe(kumpulan, 5))
2
>>> 
>>> #----------------------------------- NOMER 7 -----------------------------#
>>> 
>>> def binSeMass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

>>> kumpulan = [2, 4, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
>>> print(binSeMass(kumpulan, 6))
[3, 4, 5]
>>> 
>>> 
