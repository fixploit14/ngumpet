import os

print("[0] Tentang program")
print("[1] Sembunyikan file")
print("[2] Tampilkan file")
print("[3] Keluar program")

menu = input("Menu: ")

if menu == "0":
    print("Sedang dalam pengembangan.")

elif menu == "1":
    direktori = input("Masukkan direktori yang akan disembunyikan filenya: ")

    if not os.path.isdir(direktori):
        print("Direktori tidak ditemukan.")
    else:
        for nama_file in os.listdir(direktori):
            nama_baru_file = "." + nama_file
            os.rename(os.path.join(direktori, nama_file), os.path.join(direktori, nama_baru_file))
            print(f"[*] Menyembunyikan file '{nama_file}'")
        print("[+] Selesai.")

elif menu == "2":
    direktori = input("Masukkan direktori yang akan ditampilkan filenya: ")

    if not os.path.isdir(direktori):
        print("Direktori tidak ditemukan.")
    else:
        for nama_file in os.listdir(direktori):
            if nama_file.startswith("."):
                nama_baru_file = nama_file[1:] 
                os.rename(os.path.join(direktori, nama_file), os.path.join(direktori, nama_baru_file))
                print(f"[*] Menampilkan file '{nama_file}'")
        print("[+] Selesai.")

elif menu == "3":
    exit(0)
