
def header():
    print("SELAMAT DATANG DI PROGRAM CAESAR CIPHER")


def menu():
    while True:
        print()
        print("================")
        print("    MENU  ")
        print("================")
        print("1. ENKRIPSI ")
        print("2. DESKRIPSI")
        print("3. KELUAR")
        print("================")
        print()

        input_menu = int(input("Masukan Menu yang dipilih : "))
        if input_menu == 1:
            hasil = enk()
            print()
            print("Hasil Enkripsi: " + hasil)
            print("Menu Utama")
        elif input_menu == 2:
            dek()
            print()
            print("Hasil dekripsi bisa di lihat di atas")
            print("Menu Utama")
        elif input_menu == 3:
            break
        else:
            print("ERROR: Pastikan masukkan angka dengan benar !")


def dek():
    karakter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    input_encrypted = str(input("Masukan pesan yang akan di dekripsi :" ))

    for key in range(len(karakter)):
        translated = ""
        for symbol in input_encrypted:
            if symbol in karakter:
                num = karakter.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(karakter)
                translated = translated + karakter[num]
            else:
                translated = translated + symbol

        print('Hacking key #%s: %s' % (key, translated))

def enk():
    text = str(input("Masukan text yang sudah di enkripsi "))
    key = int(input("Masukan key yang digunakan ? "))
    total = ""    
    for i in range(len(text)):
        char = text[i]   
        if char.isupper():
            total += chr((ord(char) + key - 65) % 26 + 65)
        elif char == " ":
            total += " "
        else:
            total += chr((ord(char) + key - 97) % 26 + 97)

    return total



def main():
    header()
    menu()


if __name__ == '__main__':
    main()
