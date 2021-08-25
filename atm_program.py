import random
import datetime
import os
from customer import Customer

customer = Customer(id)
os.system('cls')
while True:
    id = int(input('Masukkan nomer pin: '))
    trial = 1
    os.system('cls')
    
    while customer.checkPin() != id and trial < 3:
        id = int(input('Pin anda salah, masukkan kembali pin anda: '))
        os.system('cls')
        trial += 1
        if trial == 3:
            print('Maaf anda telah memasukkan pin yang salah sebanyak 3 kali. Program selesai.')
            exit()

    while customer.checkPin() == id:
        print('Selamat datang!')
        print('===============')
        print('      Menu     ')
        print('===============')
        print('1. Cek Saldo   ')
        print('2. Debet       ')
        print('3. Simpan      ')
        print('4. Ganti PIN   ')
        print('5. Keluar      ')
        selectmenu = int(input('Pilih menu: '))

        if selectmenu == 1:
            os.system('cls')
            print('Total saldo kamu: Rp '+str(customer.checkBalance())+'\n')

        elif selectmenu == 2:
            totalWithdraw = int(input('Masukkan saldo yang akan diambil: '))
            verify_withdraw = input('Apakah anda yakin untuk melakukan debet sebesar Rp '+str(totalWithdraw)+'? (y/n)')
            if verify_withdraw =='y':
                if customer.checkBalance() >= totalWithdraw:
                    customer.withdrawMoney(totalWithdraw)
                    os.system('cls')
                    print('Saldo kamu berhasil ditarik.')
                    print('Total saldo kamu sekarang: Rp '+str(customer.checkBalance())+'\n')
                else:
                    os.system('cls')
                    print('Maaf saldo anda tidak cukup untuk melakukan debet sebanyak Rp '+ str(totalWithdraw))
                    print('Total saldo kamu sekarang: Rp '+str(customer.checkBalance())+'\n')
            else:
                os.system('cls')
                print('Debit dibatalkan \n')

        elif selectmenu == 3:
            totalDeposit = int(input('Masukkan saldo yang akan ditambahkan: '))
            verify_deposit = input('Apakah anda yakin untuk melakukan deposit sebesar Rp '+str(totalDeposit)+'? (y/n)')
            os.system('cls')
            if verify_deposit =='y':
                customer.depositMoney(totalDeposit)
                print('Saldo kamu berhasil ditambahkan.')
                print('Total saldo kamu sekarang: Rp '+str(customer.checkBalance())+'\n')
            else:
                print('Deposit dibatalkan \n')

        elif selectmenu == 4:
            verify_pin = int(input('Masukkan pin yang sekarang: '))
            if verify_pin == customer.checkPin():
                os.system('cls')
                inputNewPin = int(input('Masukkan pin baru: '))
                verify_new_pin = (int(input('Masukkan ulang pin baru: ')))
                os.system('cls')
                if inputNewPin == verify_new_pin:
                    customer.changePin(inputNewPin)
                    print('Pin kamu berhasil diganti.')
                    print('Silahkan masuk kembali.')
                else:
                    print('Verifikasi penggantian pin gagal karena kamu salah memasukkan ulang pin baru \n')
            else:
                os.system('cls')
                print('Pin yang anda masukkan salah')

        elif selectmenu == 5:
            os.system('cls')
            print("Resi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini sebagai bukti transaksi anda.")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", customer.checkBalance())
            print('Terima kasih telah menggunakan ATM kami, silahkan ambil kartu anda.')
            exit()

        else:
            print('Tidak ada menu yang kamu pilih.')
