# PROJECT UAS PENGANTAR PEMROGRAMAN
# KELOMPOK 7 KELAS A-2
# ANGGOTA: Fadli Muhammad, Shiba Salsabilla, Haryo Bismo Wicaksono, Ahmad Zulfikar Al Ghiffari, Dhiwa Abqariyyah, Olga Kabsyah Ramadhani
# TEMA: BUDGETING UANG BULANAN

import os

class Budgeting():
    def __init__(self):
        #Tampilan Main Menu
        os.system('cls')
        print('---------SELAMAT DATANG DI PROGRAM BUDGETING PENGELUARAN UANG---------\n')
        while True:
            try:
                tampilan_utama = int(input('Program ini akan menghitung budget pengeluaran uang pengguna\n1) Menghitung budget anda\n2) Exit\n'))
                if tampilan_utama == 1:
                    self.pertanyaan()
                else:
                    exit
                    break
            except:
                exit
                break

    def pertanyaan(self):
        #Tampilan Pertanyaan
        os.system('cls')
        print('---------JAWAB BEBERAPA PERTANYAAN DI BAWAH INI---------\n')
        income = int(input('Berapa uang bulanan anda?\n'))
        while True:
            try:
                kos = int(input('\nApakah uang bulanan yang anda input sudah dikurangi dengan biaya anda membayar kos?\n1) Yes\n2) No\n'))
                if kos == 1:
                    self.total_income = income
                    break
                elif kos == 2:
                    harga_kos = float(input('\nBerapa harga kos anda?\n'))
                    self.total_income = income - harga_kos
                    break
                elif kos <= 0 or kos > 2:
                    print('Input tidak ada dalam pilihan, Silahkan pilih 1 atau 2')
            except:
                print('Input tidak ada dalam pilihan, Silahkan pilih 1 atau 2')
        os.system('pause')
        self.calculator()

    def calculator(self):
        #Tampilan Penghitungan Budget Rules 
        os.system('cls')
        print('Calculator ini menggunakan sistem 50/30/20 budget rules\n50% untuk keperluan\n30% untuk lifestyle\n20% untuk saving\n')
        self.keperluan = self.total_income * 0.5
        self.lifestyle = self.total_income * 0.3
        self.saving = self.total_income * 0.2
        print('Uang bulanan anda : {}\n'.format(self.total_income))
        print('Buduget keperluan : {}\nBudget lifestyle : {}\nBudget Saving : {}'.format(self.keperluan, self.lifestyle, self.saving))
        while True:
            try:
                detail = int(input('\nPilih opsi berikut ini:\n1) Detail dari keperluan\n2) Detail dari lifestyle\n3) Saving\n'))
                if detail == 1:
                    os.system('cls')
                    self.detail_keperluan()
                elif detail <= 0 or detail > 3:
                    print('Input tidak ada dalam pilihan, Silahkan pilih 1, 2 atau 3')
                    break
                elif detail == 2:
                    self.detail_lifestyle()   
                elif detail == 3:
                    os.system('cls')
                    print('Bulan ini anda perlu menyisihkan {} untuk di tabung\n'.format(self.saving))
                    while True:
                        try:
                            opsi = int(input('Pilih opsi berikut ini:\n1) Kembali ke Main menu\n2) Kembali melihat budget anda\n'))
                            if opsi == 1:
                                self.__init__()
                                break
                            elif opsi == 2:
                                self.calculator()   
                        except:
                            print('\nInput tidak ada dalam pilihan, Silahkan pilih 1, 2 atau 3')
                    break
            except:
                print('Input tidak ada dalam pilihan, Silahkan pilih 1, 2 atau 3')
                continue
            break
     
    def detail_keperluan(self):
        print('-------------CATEGORY-------------\n')
        category = ['Makan', 'Transportasi', 'Token Listrik','Pulsa','Laundry']
        print("Pilih opsi berikut ini(Ketik SELESAI jika sudah cukup):")
        for i in range(len(category)):
            print(f"{i+1}) {category[i]}")
        pilihan = []
        while True:
            try:
                choice = input("Your choice: ")
                if choice == 'SELESAI':
                    print(pilihan)
                    break
                elif choice == '0' or int(choice) > len(category):
                    print('Input tidak ada dalam pilihan')
                else:
                    if category[int(choice)-1] not in pilihan:
                        pilihan.append(category[int(choice)-1])
                        print('\nAnda telah memilih : {}'.format(pilihan))
                    else:
                        print('Kamu sudah memilih nomor itu.')
                        continue
            except:
                print('Input tidak ada dalam pilihan')
                
        os.system('cls')
        print('------------DETAIL KEPERLUAN------------\n')
        print('Pilihan category anda:')
        def pilihan_anda():
            for i in range(len(pilihan)):
                print(f'{i+1}) {pilihan[i]}')
        pilihan_anda()
        while True:
            try:
                hapus = int(input('\nApakah anda ingin menghapus salah satu category?\n1) Yes\n2) No\n'))
                if hapus == 1:
                    while True:
                        try:
                            hapus_apa = int(input('\nCategory ke berapa yang ingin anda hapus? '))
                            if hapus_apa == 1:
                                del pilihan[0]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                            elif hapus_apa == 2:
                                del pilihan[1]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                            elif hapus_apa == 3:
                                del pilihan[2]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                            elif hapus_apa == 4:
                                del pilihan[3]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                            elif hapus_apa == 5:
                                del pilihan[4]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                        except:
                            print('Input tidak ada dalam pilihan')
                elif hapus == 2:
                    break
                else:
                    print('Input tidak ada dalam pilihan')
                    continue                   
            except:
                print('Input tidak ada dalam pilihan')
        
        makan = self.keperluan * 0.51
        Transportasi = self.keperluan * 0.25
        Token_Listrik = self.keperluan *0.06
        pulsa = self.keperluan * 0.08
        laundry = self.keperluan * 0.03

        print('\nList budget yang anda pilih:')

        for i in (pilihan):
            if i == 'Makan':
                print('Budget {} : {} '.format(i,makan))
                break
    
        for i in (pilihan):
            if i == 'Transportasi':
                print('Budget {} : {} '.format(i,Transportasi))
                break
        
        for i in (pilihan):
            if i == 'Token Listrik':
                print('Budget {} : {} '.format(i,Token_Listrik))
                break

        for i in (pilihan):
            if i == 'Pulsa':
                print('Budget {} : {} '.format(i,pulsa))
                break
        
        for i in (pilihan):
            if i == 'Laundry':
                print('Budget {} : {} '.format(i,laundry))
                break

        print('\n------------PROGRAM INI SELESAI------------')

        while True:
            terakhir = int(input('\nPilih opsi berikut ini:\n1) Kembali ke main menu\n2) Kembali melihat budget anda\n'))
            if terakhir == 1:
                os.system('cls')
                self.__init__()
                break
            elif terakhir == 2:
                os.system('cls')
                self.calculator()
                break
            break
        
    def detail_lifestyle(self):
        os.system('cls')
        print('-------------CATEGORY-------------\n')
        category = ['Fun Expanse/Jajan','Pakaian','Make Up & Skincare','Hobi']
        print("Pilih opsi berikut ini(Ketik SELESAI jika sudah cukup):")
        for i in range(len(category)):
            print(f'{i+1}) {category[i]}')
        wadah = []
        while True:
            try:
                choice = input("Your choice: ")
                if choice == "SELESAI":
                    print(wadah)
                    break
                elif choice == '0' or int(choice) > len(category):
                    print('Input tidak ada dalam pilihan')
                else:
                    if category[int(choice)-1] not in wadah:
                        wadah.append(category[int(choice)-1])
                        print('\nAnda telah memilih : {}'.format(wadah))
                    else:
                        print('Kamu sudah memilih nomor itu.')
                        continue
            except:
                print('Input tidak ada dalam pilihan')
        
        os.system('cls')
        print('------------DETAIL KEPERLUAN------------\n')
        print('Pilihan category anda:')
        def pilihan_anda():
            for i in range(len(wadah)):
                print(f'{i+1}) {wadah[i]}')
        pilihan_anda()
        while True:
            try:
                hapus = int(input('\nApakah anda ingin menghapus salah satu category?\n1) Yes\n2) No\n'))
                if hapus == 1:
                    while True:
                        try:
                            hapus_apa = int(input('\nCategory ke berapa yang ingin anda hapus? '))
                            if hapus_apa == 1:
                                del wadah[0]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                            elif hapus_apa == 2:
                                del wadah[1]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                            elif hapus_apa == 3:
                                del wadah[2]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                            elif hapus_apa == 4:
                                del wadah[3]
                                print('\ncategorymu sekarang : ')
                                pilihan_anda()
                                break
                        except:
                            print('Input tidak ada dalam pilihan')
                elif hapus == 2:
                    break
                else:
                    print('Input tidak ada dalam pilihan')
                    continue                   
            except:
                print('Input tidak ada dalam pilihan')
        
        fun = self.lifestyle * 0.5
        baju = self.lifestyle * 0.12
        skin_care = self.lifestyle * 0.07
        hobi = self.lifestyle * 0.16

        print('\nList budget yang anda pilih:')

        for i in (wadah):
            if i == 'Fun Expanse/Jajan':
                print('Budget {} : {} '.format(i,fun))
                break
    
        for i in (wadah):
            if i == 'Pakaian':
                print('Budget {} : {} '.format(i,baju))
                break
        
        for i in (wadah):
            if i == 'Make Up & Skincare':
                print('Budget {} : {} '.format(i,skin_care))
                break

        for i in (wadah):
            if i == 'Hobi':
                print('Budget {} : {} '.format(i,hobi))
                break
        
        print('\n------------PROGRAM INI SELESAI------------')
    
        while True:
            terakhir = int(input('\nPilih opsi berikut ini:\n1) Kembali ke main menu\n2) Kembali melihat budget anda\n'))
            if terakhir == 1:
                os.system('cls')
                self.__init__()
                break
            elif terakhir == 2:
                os.system('cls')
                self.calculator()
                break 
            break
Budgeting()