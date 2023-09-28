import os

direktori = input("Masukkan path direktori: ")

if not os.path.isdir(direktori):
    print("Direktori tidak ditemukan.")
else:
    for nama_file in os.listdir(direktori):
        nama_baru_file = "." + nama_file
        os.rename(os.path.join(direktori, nama_file), os.path.join(direktori, nama_baru_file))
        print(f"[*] Menyembunyikan file '{nama_file}'")
    print("[+] Selesai.")
