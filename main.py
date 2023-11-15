import time
class TextColors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

print(f'{TextColors.RED}--------------------------------')
print('PROGRAM PENGELOLAAN PERPUSTAKAAN')
print(f'--------------------------------{TextColors.RESET}')

# Inisialisasi Variabel
daftar_buku = []
sewa = []
no = 1

# Inisialisasi Function
def animasi(teks, kecepatan):
    for karakter in teks:
        print(karakter, end='', flush=True)
        time.sleep(kecepatan)
    print()


def tambahBuku():
    global no

    judul = input('\nMasukkan Judul Buku : ').capitalize()
    penulis = input('Masukkan Penulis Buku : ').capitalize()
    terbit = input('Masukkan Tahun Terbit Buku : ')
        
    for i in daftar_buku:
            if i[1] == judul:
                teks = f'\nBuku Berjudul {judul} Sudah Ada di Daftar'
                animasi(teks, 0.03)
                return True

    else: 
        if not terbit.isdigit() or not (judul and penulis):
            teks = '\nMohon Masukkan Data Dengan Benar!'
            animasi(teks, 0.03)
            return True
        else:
            hasil = [no, judul, penulis, terbit]
            daftar_buku.append(hasil)
            no += 1
            teks = '\nBuku Telah Ditambahkan'
            animasi(teks, 0.03) 
    return True


def lihatBuku():
    print()
    for i in daftar_buku:
        no, judul, penulis, terbit = i
        teks = f'{no}. {judul}\n   Ditulis Oleh {penulis}. Diterbitkan Pada Tahun {terbit}.'
        animasi(teks, 0.03)
    return True


def hapusBuku(judul):
    global no
    
    for i in daftar_buku:
        if i[1] == judul:
            for j in daftar_buku:
                if j[0] > i[0]:
                    j[0] -= 1
                    
            daftar_buku.remove(i)
            no -= 1
            teks = '\nBuku Berhasil Dihapus'
            animasi(teks, 0.03)
        elif judul not in i[1]:
            teks = '\nBuku Tidak Ada Dalam Daftar'
            animasi(teks, 0.03)
    return True      

def sewaBuku(judul, nama, tenggat):
    ditemukan = False
    for i in sewa:
        if judul == i[0]:
            teks = f'\nBuku Berjudul {judul} Sudah Disewa Oleh {i[1]}'
            animasi(teks, 0.03)
            ditemukan = True
            break
        
    if not ditemukan:
        for i in daftar_buku:
            if judul not in i[1]:
                teks = f'\nBuku Tidak Ada Dalam Daftar'
                animasi(teks, 0.03)
                break
        else:
            sewa.append([judul,nama,tenggat])
            teks = f'\nBuku Berjudul {judul} Berhasil Disewa Oleh {nama} Dengan Tenggat {tenggat} Hari'
            animasi(teks, 0.03) 
    return True


def daftarSewa():
    print()
    for i in sewa:
        judul, nama, tenggat = i
        teks = f'Buku Berjudul {judul} Disewa Oleh {nama} Dengan Tenggat {tenggat} Hari. '
        animasi(teks, 0.03)
    return True
    
def pengembalianSewa(nama):
    for i in sewa:
        if i[1] == nama :
            pengembalian = int(input('Buku di Kembalikan Pada Hari Ke : '))
            if pengembalian > i[2]:
                denda = 1000 * (pengembalian - i[2])
                teks = f'Anda Dikenai Denda Rp.{denda} Karena Keterlambatan Pengembalian dalam {pengembalian - i[2]} Hari'
                animasi(teks, 0.03)
                
                ulangi = True
                while(ulangi):
                    bayar = int(input('\nMasukkan Bayar : '))
                    
                    if bayar < denda:
                        teks = '\nMaaf, Uang Kamu Kurang'
                        animasi(teks, 0.03)
                    elif bayar == denda:
                        teks = f'\nPembayaran Sudah Lunas. Buku Berhasil Dikembalikan'
                        animasi(teks, 0.03)
                        ulangi = False
                    elif bayar > denda:
                        total = bayar - denda
                        teks = f'\nPembayaran Sudah Lunas. Kembali Rp.{total}. Buku Berhasil Dikembalikan'
                        ulangi = False
                        animasi(teks, 0.03)
                    
                sewa.remove(i)
 

            else:
                teks = 'Buku Berhasil Dikembalikan'
                sewa.remove(i)
        else:
            teks = 'Nama Tidak Ada Dalam Daftar Penyewa'
            animasi(teks, 0.03)
    
# Input


def menu():
    while True:
        print(f'{TextColors.YELLOW}\nDaftar Menu :')
        print('--------------------')
        print('1. Tambah Buku')
        print('2. Lihat Buku')
        print('3. Hapus Buku')
        print('4. Sewa Buku')
        print('5. Daftar Penyewa')
        print('6. Pengembalian Buku')
        print('7. Keluar')
        print(f'--------------------{TextColors.RESET}')

        pilih = input('\nPilih Menu : ')

        if pilih == '1':
            tambahBuku()
        elif pilih == '2':
            if not daftar_buku:
                teks = '\nTidak Ada Buku yang Tersedia'
                animasi(teks, 0.03)
            else:
                lihatBuku()
        elif pilih == '3':
            if not daftar_buku:
                teks = f'\nBuku Tidak Tersedia'
                animasi(teks, 0.03)
            else:
                judul = input('\nMasukkan judul Buku yang Ingin Dihapus : ').capitalize()
                hapusBuku(judul)
        elif pilih == '4':
            if not daftar_buku:
                teks = f'\nTidak Ada Buku yang Tersedia'
                animasi(teks, 0.03)
            else:
                nama = input('\nMasukkan Nama Penyewa : ').capitalize()
                judul = input('Masukkan Judul Buku yang Ingin Disewa : ').capitalize()
                tenggat = int(input('Masukkan Berapa Hari Tenggat Pengembalian : '))
                sewaBuku(judul, nama, tenggat)
        elif pilih == '5':
            if not sewa:
                teks = f'\nSaat Ini Tidak Ada Penyewa Buku'
                animasi(teks, 0.03)
            else:
                daftarSewa()
        elif pilih == '6':
            if not sewa:
                teks = f'\nSaat Ini Tidak Ada Penyewa Buku'
                animasi(teks, 0.03)
            else:
                nama = input('Masukkan Nama Penyewa : ').capitalize()
                pengembalianSewa(nama)
        elif pilih == '7':
            teks = f'\nKamu Berhasil Keluar Program'
            animasi(teks, 0.03)
            return False
        else:
            teks = 'Silahkan Pilih Menu yang Ada di Daftar'
            animasi(teks, 0.03)

menu()
