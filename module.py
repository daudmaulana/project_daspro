from colorama import Fore, Back, Style, init
import time

# Inisialisasi Variabel
daftar_buku = []
sewa = []
no = 1

# Inisialisasi Function
def animasi(teks, kecepatan, warna, style):
    for karakter in teks:
        print(f'{warna}{style}{karakter}', end='')
        time.sleep(kecepatan)
    print(Style.RESET_ALL)


def tambahBuku():
    global no

    judul = input(f'{Fore.YELLOW}[+] Masukkan Judul Buku : {Fore.RESET}').capitalize()
    penulis = input(f'{Fore.YELLOW}[+] Masukkan Penulis Buku : {Fore.RESET}').capitalize()
    terbit = input(f'{Fore.YELLOW}[+] Masukkan Tahun Terbit Buku : {Fore.RESET}')
        
    for i in daftar_buku:
            if i[1] == judul:
                teks = f'Buku Berjudul {judul} Sudah Ada di Daftar'
                animasi(teks, 0.03, Fore.RED, Style.BRIGHT) 
                return True

    else: 
        if not terbit.isdigit():
            teks = 'Mohon Masukkan Data Dengan Benar!'
            animasi(teks, 0.03, Fore.RED, Style.BRIGHT) 
            return True
        else:
            hasil = [no, judul, penulis, terbit]
            daftar_buku.append(hasil)
            no += 1
            teks = 'Buku Telah Ditambahkan'
            animasi(teks, 0.03, Fore.BLUE, Style.BRIGHT) 
    return True


def lihatBuku():
    for i in daftar_buku:
        no, judul, penulis, terbit = i
        teks = f'{no}. {judul}\n   Ditulis Oleh {penulis}. Diterbitkan Pada Tahun {terbit}.'
        animasi(teks, 0.03, Fore.BLUE, Style.BRIGHT)
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
            teks = 'Buku Berhasil Dihapus'
            animasi(teks, 0.03, Fore.BLUE, Style.BRIGHT)
        elif judul not in i[1]:
            teks = 'Buku Tidak Ada Dalam Daftar'
            animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
    return True      

def sewaBuku(judul, nama, tenggat):
    ditemukan = False
    for i in sewa:
        if judul == i[0]:
            teks = f'Buku Berjudul {judul} Sudah Disewa Oleh {i[1]}'
            animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
            ditemukan = True
            break
        
    if not ditemukan:
        for i in daftar_buku:
            if judul not in i[1]:
                teks = f'Buku Tidak Ada Dalam Daftar'
                animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
                break
        else:
            sewa.append([judul,nama,tenggat])
            teks = f'Buku Berjudul {judul} Berhasil Disewa Oleh {nama} Dengan Tenggat {tenggat} Hari'
            animasi(teks, 0.03, Fore.BLUE, Style.BRIGHT) 
    return True


def daftarSewa():
    for i in sewa:
        judul, nama, tenggat = i
        teks = f'Buku Berjudul {judul} Disewa Oleh {nama} Dengan Tenggat {tenggat} Hari. '
        animasi(teks, 0.03, Fore.BLUE, Style.BRIGHT)
    return True
    
def pengembalianSewa(judul):
    for i in sewa:
        if i[0] == judul :
            pengembalian = int(input(f'{Fore.YELLOW}[+] Buku di Kembalikan Pada Hari Ke : {Fore.RESET}'))
            if pengembalian > i[2]:
                denda = 1000 * (pengembalian - i[2])
                teks = f'Anda Dikenai Denda Rp.{denda} Karena Keterlambatan Pengembalian dalam {pengembalian - i[2]} Hari'
                animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
                
                ulangi = True
                while(ulangi):
                    bayar = int(input(f'{Fore.YELLOW}[+] Masukkan Bayar : {Fore.RESET}'))
                    
                    if bayar < denda:
                        teks = 'Maaf, Uang Kamu Kurang'
                        animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
                    elif bayar == denda:
                        kembali = 0
                        ulangi = False
                    elif bayar > denda:
                        kembali = bayar - denda
                        ulangi = False
                struk = f'''
{Fore.GREEN}Nama       : {i[1]}            
{Fore.GREEN}Judul Buku : {judul}
{Fore.GREEN}Bayar      : Rp.{bayar}
{Fore.GREEN}Kembali    : Rp.{kembali}
{Fore.YELLOW}Buku Berhasil Dikembalikan
'''

                print(struk)
                sewa.remove(i)
            else:
                teks = 'Buku Berhasil Dikembalikan'
                sewa.remove(i)
        else:
            teks = 'Judul Tidak Ada Dalam Daftar Sewa'
            animasi(teks, 0.03, Fore.BLUE, Style.BRIGHT)