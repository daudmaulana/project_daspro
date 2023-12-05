from colorama import Fore, Style, init
import module as m
import os

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
banner = f"""{Fore.YELLOW}{Style.BRIGHT}
 ____  __.     .__                                __     ________  
|    |/ _|____ |  |   ____   _____ ______   ____ |  | __ \_____  \ 
|      <_/ __ \|  |  /  _ \ /     \\____ \ /  _ \|  |/ /  /  ____/ 
|    |  \  ___/|  |_(  <_> )  Y Y  \  |_> >  <_> )    <  /       \ 
|____|__ \___  >____/\____/|__|_|  /   __/ \____/|__|_ \ \_______ \\
        \/   \/                  \/|__|               \/         \/
"""
print(banner)

banner = f'''{Fore.YELLOW}{Style.BRIGHT}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{Fore.YELLOW}{Style.BRIGHT}┃{Fore.MAGENTA}[💎] {Fore.GREEN}[Dev. By Salman Daud Maulana]                    {Fore.YELLOW}┃
{Fore.YELLOW}{Style.BRIGHT}┃{Fore.MAGENTA}[💎] {Fore.CYAN}[Sup. By Bagus Willy Pratama                     {Fore.YELLOW}┃
{Fore.YELLOW}{Style.BRIGHT}┃{Fore.MAGENTA}[💎] {Fore.CYAN}         Nayla Dwi Septiana]                     {Fore.YELLOW}┃
{Fore.YELLOW}{Style.BRIGHT}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{Fore.YELLOW}{Style.BRIGHT}┃{Fore.MAGENTA}[🤖] {Fore.RED}[PROGRAM PENGELOLAAN PERPUSTAKAAN] {Fore.RED}🔥            {Fore.YELLOW}┃
{Fore.YELLOW}{Style.BRIGHT}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''
print(banner)

    
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
        m.tambahBuku()
    elif pilih == '2':
        if not m.daftar_buku:
            teks = 'Tidak Ada Buku yang Tersedia'
            m.animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            m.lihatBuku()
    elif pilih == '3':
        if not m.daftar_buku:
            teks = 'Buku Tidak Tersedia'
            m.animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            m.lihatBuku()
            judul = input(f'{Fore.YELLOW}[+] Masukkan judul Buku yang Ingin Dihapus : {Fore.RESET}').capitalize()
            m.hapusBuku(judul)
    elif pilih == '4':
        if not m.daftar_buku:
            teks = 'Tidak Ada Buku yang Tersedia'
            m.animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            m.lihatBuku()
            nama = input(f'{Fore.YELLOW}[+] Masukkan Nama Penyewa : {Fore.RESET}').capitalize()
            judul = input(f'{Fore.YELLOW}[+] Masukkan Judul Buku yang Ingin Disewa : {Fore.RESET}').capitalize()
            tenggat = int(input(f'{Fore.YELLOW}[+] Masukkan Berapa Hari Tenggat Pengembalian : {Fore.RESET}'))
            m.sewaBuku(judul, nama, tenggat)
    elif pilih == '5':
        if not m.sewa:
            teks = f'Saat Ini Tidak Ada Penyewa Buku'
            m.animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            m.daftarSewa()
    elif pilih == '6':
        if not m.sewa:
            teks = f'Saat Ini Tidak Ada Penyewa Buku'
            m.animasi(teks, 0.03, Fore.RED, Style.BRIGHT)
        else:
            m.daftarSewa()
            judul = input(f'{Fore.YELLOW}[+] Masukkan Judul Buku : {Fore.RESET}').capitalize()
            m.pengembalianSewa(judul)
    elif pilih == '7':
        teks = f'Keluar dari Program'
        m.animasi(teks, 0.03, Fore.BLUE, Style.BRIGHT)
        break
    else:
        teks = 'Silahkan Pilih Menu yang Ada di Daftar'
        m.animasi(teks, 0.03, Fore.RED, Style.BRIGHT)

