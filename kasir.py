import os

cart = []
if len(cart) == 0:
    print('keranjang kosong')
    cont = 0
    while True:
        data = input('masukan keranjang: ')
        cont+=1
        if cont >= 10:
            print('barang di tambahkan')
            break
    cart.append(data)
    print('----------MENU----------')
    print('|1.Bayar               |')
    print('|2.Kembalikan barang   |')
    print('|3.Support Author      |')
    print('------------------------')
    print('Author:Sanggam Sidabutar')
    print('Github:github.com/sidabutar1337')   
    try:
        def sanggam1():
            menu = int(input('Pilih: '))
            if menu == 1:
                cart.clear()
                for sanggam in range(10):
                    harga = float(input(f'harga barang{sanggam+1}: '))
                    cart.append(harga)
                
                def tambah(a,b,c,d,e,f,g,h,i,j):
                    rumus = a+b+c+d+e+f+g+h+i+j
                    return rumus
                def kurang(a,b):
                    rumus = a-b
                    return rumus
                total = tambah(*cart)
                nominal = float(input('uang di terima: '))
                if total >= nominal:
                    print('uang tidak cukup')
                    print('harap berikan uang yang cukup')
                elif total <= nominal:
                    bayar = kurang(nominal,total)
                    print(f'kembalian anda {bayar}')
                    thanks1 = f'Terima kasih telah berbelanja di tempat kami,Total belanja:{total} Kembalian:{bayar}'
                    print(thanks1)
                    with open('buktibayar.txt','w') as bukti:
                        bukti.write(thanks1)
                elif total == nominal:
                    print('uang anda pas')
                    thanks2 = f'Terima kasih telah berbelanja di tempat kami,Total belanja:{total}'
                    with open('buktibayar.txt','w') as bukti:
                        bukti.write(thanks2)
                else:
                    print('Opps Ada Kesalahan')
            elif menu == 2:
                print('Terima kasih telah berkunjung')
                chat = input('chat: ')
                send = os.system(f'xdg-open https://wa.me/+6285275797174?text={chat}')
                print(send)
            elif menu == 3:
                facebook = os.system('xdg-open https://facebook.com/zeussec1337')
                print(facebook)   
            else:
                print('pilihan tidak ada')
        mulai = sanggam1()
        print(mulai)         
    except ValueError:
        print('Harap gunakan bilang angka pecahan dalam memasukan harga dan gunakan bilangan bulat ingin memilih menu')
        ulang = sanggam1()
        print(ulang)
    

     

                            