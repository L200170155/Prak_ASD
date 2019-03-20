Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [[1,2],[3,4]]
>>> b = [[5,6],[7,8]]
>>> c = [[12,3,"x","y"],[12,33,4]]
>>> d = [[3,4],[2,4],[1,5]]
>>> e = [[5,6,7],[7,8,9]]
>>> f = [[1,2,3],[4,5,6],[7,8,9]]
>>> def cekKonsis(n):
    x = len(n[0])
    z = 0
    for i in range(len(n)):
        if (len(n[i]) == x):
           z+=1
    if(z == len(n)):
        print("matriks konsisten")
    else:
        print("matrik tidak konsisten")

        
>>> cekKonsis(a)
matriks konsisten
>>> cekKonsis(b)
matriks konsisten
>>> cekKonsis(c)
matrik tidak konsisten
>>> 
>>> def cekInt(n):
    x = 0
    y = 0
    for i in n:
        for j in i:
            y+=1
            if (str(j).isdigit()==False):
                print("tidak semua isi matriks adalah angka")
                break
            else:
                x+=1
    if(x==y):
        print("semua isi matriks adalah angka")

        
>>> cekInt(a)
semua isi matriks adalah angka
>>> cekInt(b)
semua isi matriks adalah angka
>>> cekInt(c)
tidak semua isi matriks adalah angka
>>> 
>>> def ordo(n):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    print("mempunyai ordo "+str(x)+"x"+str(y))

    
>>> ordo(a)
mempunyai ordo 2x2
>>> ordo(b)
mempunyai ordo 2x2
>>> ordo(c)
mempunyai ordo 2x3
>>> ordo(d)
mempunyai ordo 3x2
>>> ordo(e)
mempunyai ordo 2x3
>>> 
>>> def jumlah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("ukuran beda")

        
>>> jumlah(a,b)
ukuran sama
[[6, 8], [10, 12]]
>>> jumlah(a,d)
ukuran beda
>>> 
>>> def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("bisa dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("tidak memenuhi syarat")

        
>>> zz = [[1,2,3],[1,2,3]]
>>> zx = [[1],[2],[3]]
>>> kali(zz,zx)
bisa dikalikan
[[14], [14]]
>>> kali(a,b)
bisa dikalikan
[[19, 22], [43, 50]]
>>> kali(a,e)
bisa dikalikan
[[19, 22, 25], [43, 50, 57]]
>>> kali(a,zx)

tidak memenuhi syarat
>>> 
>>> def determHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total

>>> z = [[3,1],[2,5]]
>>> x = [[1,2,1],[3,3,1],[2,1,2]]
>>> v = [[1,-2,0,0],[3,2,-3,1],[4,0,5,1],[2,3,-1,4]]
>>> r = [[10,23,45,12,13],[1,2,3,4,5],[1,2,3,4,6],[4,2,3,4,8],[1,4,5,6,10]]
>>> print(determHitung(z))
13
>>> print(determHitung(x))
-6
>>> print(determHitung(v))
200
>>> print(determHitung(r))
330
>>> print(determHitung(d))
tidak bisa dihitung determinan, bukan matrix bujursangkar
>>> print(determHitung(e))
tidak bisa dihitung determinan, bukan matrix bujursangkar
>>> 
>>> def buatNol(n,m=None):
    if(m==None):
        m=n
    print("membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])

buatNol(2,4)
buatNol(3)

def buatIden(n):
    print("membuat matriks identitas dengan ordo"+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])
    
SyntaxError: invalid syntax
>>> 
>>> def buatNol(n,m=None):
    if(m==None):
        m=n
    print("membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])

    
>>> buatNol(2,4)
membuat matriks 0 dengan ordo 2x4
[[0, 0, 0, 0], [0, 0, 0, 0]]
>>> buatNol(3)
membuat matriks 0 dengan ordo 3x3
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> 
>>> def buatIden(n):
    print("membuat matriks identitas dengan ordo"+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])

    
>>> buatIden(4)
membuat matriks identitas dengan ordo4x4
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
>>> buatIden(2)
membuat matriks identitas dengan ordo2x2
[[1, 0], [0, 1]]
>>> 
>>> class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    def pushAk(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def deleteNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next
        temp.next = None
        temp.next = next 
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
            
SyntaxError: invalid syntax
>>> 
>>> class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
    class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    def pushAk(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def deleteNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next
        temp.next = None
        temp.next = next 
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
            
SyntaxError: expected an indented block
>>> class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

        
>>> class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    def pushAk(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def deleteNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next
        temp.next = None
        temp.next = next 
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

            
>>> llist = LinkedList()
>>> llist.pushAw(21)
>>> llist.pushAw(22)
>>> llist.pushAw(12)
>>> llist.pushAw(14)
>>> llist.pushAw(2)
>>> llist.pushAw(19)
>>> llist.pushAk(9)
<__main__.Node object at 0x06211250>
>>> llist.deleteNode(0)
>>> llist.insert(1,6)
<__main__.Node object at 0x06204D50>
>>> print(llist.search(21))
True
>>> print(llist.search(29))
False
>>> llist.display()

2 14 12 22 21 1 9 
>>> 
>>> class Node: 
    def __init__(self, data): 
        self.data = data 
        self.prev = None

        
>>> class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
    def awal(self, new_data):
        print("menambah pada awal", new_data)
        new_node = Node(new_data) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node 
    def akhir(self, new_data):
        print("menambah pada akhir", new_data)
        new_node = Node(new_data) 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        last = self.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 
        return
    def printList(self, node): 
        print("\nDari Depan :")
        while(node is not None): 
            print(" % d" %(node.data))
            last = node 
            node = node.next
        print("\nDari Belakang :")
        while(last is not None): 
            print(" % d" %(last.data)) 
            last = last.prev

            
>>> llist = DoublyLinkedList()
>>> llist.awal(7)
menambah pada awal 7
>>> llist.awal(1)
menambah pada awal 1
>>> llist.akhir(6)
menambah pada akhir 6
>>> llist.akhir(4)
menambah pada akhir 4
>>> llist.printList(llist.head)

Dari Depan :
  1
  7
  6
  4

Dari Belakang :
  4
  6
  7
  1
>>> 
