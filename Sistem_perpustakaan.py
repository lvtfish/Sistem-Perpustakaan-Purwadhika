from os import system
system('clear') 

ListBuku = {'Kutu Loncat Pohon': ['Yoda Yodiw', 2019], 'Menduakan Hidup': ['Yoshi Ino', 2020],
        'Data Analyst 101': ['Dion Wiyoko', 2021],
        'Mengejar Matahari': ['Enzy Naga', 2015], 'The Second You Sleep': ['Matt Skiba', 2017]}

BukuDiPinjam = {}

def TampilBuku():

    print('\n----------------------------------------------- Daftar Buku -----------------------------------------------------')
    print('Index \t| Judul  \t\t\t| Penulis  \t\t\t| Tahun Terbit')

    for index, i in enumerate(ListBuku):
        print(f"{index}\t| {i}\t\t| {ListBuku[i][0]}\t\t\t|{ListBuku[i][1]}")

def MenyumbangBuku():
    while True:
        inputjudul = input('Masukkan judul buku: ').split()
        inputpenulis = input('Masukkan nama penulis: ').split()
        inputtahunterbit = int(input('Masukkan tahun terbit: '))

        judulbaru = []
        penulisbaru = []

        for i in inputjudul:
            i = i.capitalize()
            judulbaru.append(i)
        judulbaru = ' '.join(judulbaru)

        for i in inputpenulis:
            i = i.capitalize()
            penulisbaru.append(i)
        penulisbaru = ' '.join(penulisbaru)

        ListBuku.update({judulbaru:[penulisbaru, inputtahunterbit]})

        TampilBuku()
        break
    MenuAwal()

def MeminjamBuku():
    TampilBuku()
    z = True
    while z == True:
        pinjambukubaru = []
        pinjambuku = input('\nMasukkan judul buku yang ada di daftar: ').split()
        for i in pinjambuku:
            i = i.capitalize()
            pinjambukubaru.append(i)
        pinjambukubaru = ' '.join(pinjambukubaru)

        x = 0
        for i in ListBuku:
            x = x+1
            if i == pinjambukubaru:
                inputkonfirmasi = (input('Apakah anda ingin meminjam buku (Y/N)? '))
                if inputkonfirmasi == 'Y':
                    BukuDiPinjam.update({pinjambukubaru:ListBuku[pinjambukubaru]})
                    del ListBuku[pinjambukubaru]
                    print('\nBuku yang sedang dipinjam:\n')
                    for i in BukuDiPinjam:
                        print(f"{i}, {BukuDiPinjam[i][0]}, {BukuDiPinjam[i][1]}")
                    z = False
                    break
                elif inputkonfirmasi == 'N':
                    print ("Silahkan ulangi proses")
                    break
                else:
                    print ("Input tidak sesuai")
                    break
            if x == len(ListBuku):
                print ('Buku tersebut tidak ada')
                continue
            continue
        continue
            
def MenghapusBuku():
    TampilBuku()
    while True:    
        HapusBukuHilang = []
        HapusBuku = input('Masukkan judul buku yang hilang: ').split()
        for i in HapusBuku:
            i = i.capitalize()
            HapusBukuHilang.append(i)
        HapusBukuHilang = ' '.join(HapusBukuHilang)
            
        KonfirmasiBukuHilang = input('Apakah kamu yakin ingin menghapus daftar buku ini (Y/N)? ')
        if KonfirmasiBukuHilang == 'Y':
            del ListBuku[HapusBukuHilang]                    
            TampilBuku()           
            break 
        elif KonfirmasiBukuHilang == 'N':
            print ("\nSilahkan ulangi proses")
                
def MenuAwal():
    while True:
        Menu = int(input('''
                              Selamat Datang di Perpustakaan LUTFI MAHATIR           
                        ------------------------------------------------------
                        1. Untuk Tampilkan Buku
                        2. Untuk Menyumbang Buku
                        3. Untuk Meminjam Buku  
                        4. Untuk Menghapus Buku
                        5. Untuk Keluar
                        
                        Silahkan pilih menu 1-5: '''))
        
        print()
        if(Menu==1):
            TampilBuku()
        elif(Menu==2):
            MenyumbangBuku()
        elif(Menu==3):
            MeminjamBuku()
        elif(Menu==4):
            MenghapusBuku()
        elif(Menu==5):
            print('Terimakasih sudah berkunjung. Datang kembali untuk meminjam buku di perpustakaan LUTFI MAHATIR') 
            break
MenuAwal()