from colorama import Fore, Back, Style, init
import time
import os

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
banner = f"""{Fore.RED}{Style.BRIGHT}
██╗░░██╗███████╗██╗░░░░░░█████╗░███╗░░░███╗██████╗░░█████╗░██╗░░██╗  ██████╗░
██║░██╔╝██╔════╝██║░░░░░██╔══██╗████╗░████║██╔══██╗██╔══██╗██║░██╔╝  ╚════██╗
█████═╝░█████╗░░██║░░░░░██║░░██║██╔████╔██║██████╔╝██║░░██║█████═╝░  ░█████╔╝
██╔═██╗░██╔══╝░░██║░░░░░██║░░██║██║╚██╔╝██║██╔═══╝░██║░░██║██╔═██╗░  ░╚═══██╗
██║░╚██╗███████╗███████╗╚█████╔╝██║░╚═╝░██║██║░░░░░╚█████╔╝██║░╚██╗  ██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░"""
print(banner)

banner = f'''{Fore.YELLOW}{Style.BRIGHT}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{Fore.YELLOW}{Style.BRIGHT}┃{Fore.MAGENTA}[💎] {Fore.GREEN}[Dev. By Salman Daud Maulana]                    {Fore.YELLOW}┃
{Fore.YELLOW}{Style.BRIGHT}┃{Fore.MAGENTA}[💎] {Fore.CYAN}[Sup. By Bagus Willy Pratama                     {Fore.YELLOW}┃
{Fore.YELLOW}{Style.BRIGHT}┃{Fore.MAGENTA}[💎] {Fore.CYAN}         Nayla Dwi Septiana]                     {Fore.YELLOW}┃
{Fore.YELLOW}{Style.BRIGHT}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{Fore.YELLOW}{Style.BRIGHT}┃{Fore.MAGENTA}[🤖] {Fore.RED}[PROGRAM PENGELOLAAN PERPUSTAKAAN] {Fore.RED}🔥            {Fore.YELLOW}┃
{Fore.YELLOW}{Style.BRIGHT}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''
print(banner)

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
{Fore.GREEN}Nama       : {nama}            
{Fore.GREEN}Judul Buku : {judul}          
{Fore.GREEN}Bayar      : {bayar}              
{Fore.GREEN}Kembali    : {kembali}      
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
    
banner = f'''\n{Fore.RED}{Style.BRIGHT}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{Fore.RED}{Style.BRIGHT}┃                 {Fore.BLUE}█▀▄▀█ █▀▀ █▄░█ █░█                   {Fore.RED}┃
┃                 {Fore.BLUE}█░▀░█ ██▄ █░▀█ █▄█                   {Fore.RED}┃
{Fore.RED}{Style.BRIGHT}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{Fore.RED}{Style.BRIGHT}┃{Fore.BLUE}[01] {Fore.LIGHTYELLOW_EX}Tambah Buku 📖                                   {Fore.RED}┃
{Fore.RED}{Style.BRIGHT}┃{Fore.BLUE}[02] {Fore.LIGHTYELLOW_EX}Lihat Buku 👁️                                    {Fore.RED}┃
{Fore.RED}{Style.BRIGHT}┃{Fore.BLUE}[03] {Fore.LIGHTGREEN_EX}Hapus Buku 🗑️                                    {Fore.RED}┃
{Fore.RED}{Style.BRIGHT}┃{Fore.BLUE}[04] {Fore.LIGHTGREEN_EX}Sewa Buku 🔥                                     {Fore.RED}┃
{Fore.RED}{Style.BRIGHT}┃{Fore.BLUE}[05] {Fore.LIGHTCYAN_EX}Daftar Penyewa 🔥                                {Fore.RED}┃
{Fore.RED}{Style.BRIGHT}┃{Fore.BLUE}[06] {Fore.LIGHTCYAN_EX}Pengembalian Buku 🔥                             {Fore.RED}┃
{Fore.RED}{Style.BRIGHT}┃{Fore.BLUE}[07] {Fore.LIGHTMAGENTA_EX}Keluar 📤                                        {Fore.RED}┃
{Fore.RED}{Style.BRIGHT}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''
              
print(banner)
# Input
while True:

    pilih = input(f'{Fore.YELLOW}[#] Pilih Opsi : {Fore.RESET}')

    if pilih == '1':
        tambahBuku()
    elif pilih == '2':
        if not daftar_buku:
            teks = 'Tidak Ada Buku yang Tersedia'
            animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            lihatBuku()
    elif pilih == '3':
        if not daftar_buku:
            teks = 'Buku Tidak Tersedia'
            animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            judul = input(f'{Fore.YELLOW}[+] Masukkan judul Buku yang Ingin Dihapus : {Fore.RESET}').capitalize()
            hapusBuku(judul)
    elif pilih == '4':
        if not daftar_buku:
            teks = 'Tidak Ada Buku yang Tersedia'
            animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            nama = input(f'{Fore.YELLOW}[+] Masukkan Nama Penyewa : {Fore.RESET}').capitalize()
            judul = input(f'{Fore.YELLOW}[+] Masukkan Judul Buku yang Ingin Disewa : {Fore.RESET}').capitalize()
            tenggat = int(input(f'{Fore.YELLOW}[+] Masukkan Berapa Hari Tenggat Pengembalian : {Fore.RESET}'))
            sewaBuku(judul, nama, tenggat)
    elif pilih == '5':
        if not sewa:
            teks = f'Saat Ini Tidak Ada Penyewa Buku'
            animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            daftarSewa()
    elif pilih == '6':
        if not sewa:
            teks = f'Saat Ini Tidak Ada Penyewa Buku'
            animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            judul = input(f'{Fore.YELLOW}[+] Masukkan Judul Buku : {Fore.RESET}').capitalize()
            pengembalianSewa(judul)
    elif pilih == '7':
        teks = f'Keluar dari Program'
        animasi(teks, 0.03, Fore.BLUE, Style.BRIGHT)
        break
    else:
        teks = 'Silahkan Pilih Menu yang Ada di Daftar'
        animasi(teks, 0.03, Fore.RED, Style.BRIGHT)

