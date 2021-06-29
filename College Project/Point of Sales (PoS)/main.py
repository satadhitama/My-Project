# PROGRAM POINT OF SALES (POS)
# UAS ALGORITMA PEMROGRAMAN KELAS
# KELAS            : INFORMATIKA-I
# KELOMPOK         : 5
# ANGGOTA KELOMPOK :
#         1. CHRISTIELLA ABINOSY SETIAWAN   (5200411525)
#         2. SATRIYA ADHITAMA               (5200411545)
#         3. ALIF QIMAN                     (5200411565)
# DOSEN PENGAMPU   : CANGGIH PUSPO WIBOWO, S.T, M.Eng.

import _sqlite3 as sq
import datetime as dt
import random


# Fungsi Untuk Barang #

def generate_id_barang(key_kategori):
    # Membuat ID barang secara otomatis berdasarkan kategori barang dan urutan penambahan barang
    conn = sq.connect('barang.db')
    list_id_barang = conn.execute('''
    SELECT id_barang FROM dataBarang
    ORDER BY id_barang ASC;
    ''').fetchall()
    i = 0
    list_id_number = []
    while i != len(list_id_barang):
        if key_kategori == list_id_barang[i][0][:len(list_id_barang[i][0])-4]:
            list_id_number.append(int(list_id_barang[i][0][-3:]))
            i += 1
        else:
            i += 1
    if len(list_id_number) == 0:
        return key_kategori + "-" + "1".zfill(3)
    else:
        missing_number = []
        range_id = range(1, list_id_number[-1:][0] + 1)
        j = 0
        k = 0
        while j != len(range_id):
            if list_id_number[k] == range_id[j]:
                j += 1
                k += 1
            else:
                missing_number.append(range_id[j])
                j += 1
        if len(missing_number) == 0:
            return key_kategori + "-" + str(list_id_number[-1:][0]+1).zfill(3)
        else:
            return key_kategori + "-" + str(missing_number[0]).zfill(3)


def check_id_barang(id_barang):
    # Mengecek ID Barang pada database Barang
    conn = sq.connect('barang.db')
    data_id_barang = conn.execute(f'''
    SELECT id_barang FROM dataBarang
    ORDER BY id_barang ASC;
    ''').fetchall()
    i = 0
    while i != len(data_id_barang):
        if id_barang == data_id_barang[i][0]:
            return True
        else:
            i += 1
    return False


def tambah_barang(database, table):
    # Menambahkan barang pada database barang
    ulang = True
    while ulang:
        while True:
            nama_barang = input("           Nama Barang  : ")
            while True:
                key_kategori = input("           Key kategori : ").upper()
                if check_kategori(key_kategori) is True:
                    break
                elif key_kategori == "":
                    return menu_kategori()
                else:
                    print('           Key Kategori Tidak Ditemukan!')
                    print('           Kosongkan Untuk Kembali (ENTER)')
                    continue
            harga_beli = input("           Harga Beli   : Rp")
            harga_jual = input("           Harga Jual   : Rp")
            if harga_beli.isalpha() or harga_jual.isalpha():
                print('           Input Harga Harus Berupa Angka')
                continue
            elif nama_barang == "" or harga_beli == "" or harga_jual == "":
                print('           Input Wajib Diisikan')
                continue
            else:
                break
        diskon = input("           Diskon (%)   : ")
        produsen = input("           Produsen     : ")
        supplier = input("           Supplier     : ")
        print(f'           ID Barang    : {generate_id_barang(key_kategori)}')
        checked_list = [generate_id_barang(key_kategori), nama_barang, key_kategori,
                        harga_beli, harga_jual, diskon, produsen, supplier]
        i = 0
        while i < len(checked_list):
            if checked_list[i] == '':
                checked_list[i] = "NULL"
                i += 1
            else:
                i += 1
        database.execute(f'''
        INSERT INTO {table} (id_barang,nama_barang,key_kategori,harga_beli,
                             harga_jual,diskon,produsen,supplier,stok,barang_terjual)
        VALUES ('{checked_list[0]}','{checked_list[1]}','{checked_list[2]}','{checked_list[3]}',
                '{checked_list[4]}','{checked_list[5]}','{checked_list[6]}','{checked_list[7]}',
                '0','0');
        ''')
        database.commit()
        print('           Data Barang Berhasil Ditambahkan!\n')
        while True:
            pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
            if pilihan == "Y":
                ulang = True
                break
            elif pilihan == "N":
                ulang = False
                break
            else:
                print("           Input Invalid!")
                continue


def hapus_barang(database, table):
    # Menghapus barang pada database barang menggunakan ID barang
    ulang = True
    while ulang:
        while True:
            id_barang = input("           Masukkan ID Barang : ").upper()
            if check_id_barang(id_barang) is True:
                break
            elif id_barang == "":
                return barang()
            else:
                print('           ID Barang Tidak Ditemukan!')
                print('           Kosongkan Untuk Kembali (ENTER)')
        database.execute(f'''
        DELETE FROM {table}
        WHERE id_barang='{id_barang}';
        ''')
        database.commit()
        print('           Data Barang Berhasil Dihapus!\n')
        while True:
            pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
            if pilihan == "Y":
                ulang = True
                break
            elif pilihan == "N":
                ulang = False
                break
            else:
                print("           Input Invalid!")
                continue


def edit_barang(database, table):
    # Mengedit barang pada database barang menggunakan ID barang
    ulang = True
    while ulang:
        while True:
            id_barang = input("           Masukkan ID Barang : ").upper()
            if check_id_barang(id_barang) is True:
                break
            elif id_barang == "":
                return barang()
            else:
                print('           ID Barang Tidak Ditemukan!')
                print('           Kosongkan Untuk Kembali (ENTER)')
        print("           Current Data")
        current_data = database.execute(f'''                 
        SELECT * FROM {table}                                
        WHERE id_barang="{id_barang}"                          
        ''').fetchall()
        for data in current_data:
            print(f'           Nama Barang : {data[1]}')
            print(f'           Kategori    : {show_kategori(data[2])}')
            print(f'           Harga Beli  : Rp{data[3]}')
            print(f'           Harga Jual  : Rp{data[4]}')
            print(f'           Diskon (%)  : {data[5]}')
            print(f'           Produsen    : {data[6]}')
            print(f'           Supplier    : {data[7]}\n')
        print("           Masukkan Data Baru!")
        nama_barang = input("           Nama Barang  : ")
        harga_beli = input("           Harga Beli   : Rp")
        harga_jual = input("           Harga Jual   : Rp")
        diskon = input("           Diskon  (%)  : ")
        produsen = input("           Produsen     : ")
        supplier = input("           Supplier     : ")
        checked_list = [id_barang, nama_barang, harga_beli, harga_jual,
                        diskon, produsen, supplier]
        i = 0
        while i < len(checked_list):
            if checked_list[i] == '':
                checked_list[i] = "NULL"
                i += 1
            else:
                i += 1

        database.execute(f'''
        UPDATE {table}
        SET nama_barang='{checked_list[1]}',harga_beli='{checked_list[2]}',harga_jual='{checked_list[3]}',
            diskon='{checked_list[4]}',produsen='{checked_list[5]}',supplier='{checked_list[6]}'
        WHERE id_barang="{checked_list[0]}";
        ''')
        database.commit()
        print('           Data Barang Berhasil Diedit!\n')
        while True:
            pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
            if pilihan == "Y":
                ulang = True
                break
            elif pilihan == "N":
                ulang = False
                break
            else:
                print("           Input Invalid!")
                continue


def display_info_barang(list_barang):
    # Menampilkan informasi barang
    i = 0
    while i != len(list_barang):
        print(f'           ID Barang   : {list_barang[i][0]}')
        print(f'           Nama Barang : {list_barang[i][1]}')
        print(f'           Kategori    : {show_kategori(list_barang[i][2])}')
        print(f'           Harga Beli  : {list_barang[i][3]}')
        print(f'           Harga Jual  : {list_barang[i][4]}')
        print(f'           Diskon      : {list_barang[i][5]}')
        print(f'           Produsen    : {list_barang[i][6]}')
        print(f'           Supplier    : {list_barang[i][7]}')
        print(f'           Stok        : {list_barang[i][8]}')
        print(f'           Terjual     : {list_barang[i][9]}\n')
        i += 1


def display_barang(database, table):
    # Menampilkan informasi barang pada database barang
    # Menampilkan semua barang atau salah satu barang (dengan ID barang)
    print('''        ||=========== DISPLAY ============||
            1.    Tampilkan Semua
            2.    Cari Barang (ID)
            3.    Cari Barang (Kategori)
            0.    Back
                ''')
    while True:
        pilihan = input("           Masukkan Pilihan Anda : ")
        print()
        if pilihan == "1":
            info_barang = database.execute(f'''
            SELECT * FROM {table}
            ORDER BY id_barang ASC;
            ''').fetchall()
            display_info_barang(info_barang)
            return display_barang(database, table)
        elif pilihan == "2":
            ulang = True
            while ulang:
                while True:
                    id_barang = input("           ID Barang   : ").upper()
                    if check_id_barang(id_barang) is True:
                        print()
                        break
                    elif id_barang == "":
                        return display_barang(database, table)
                    else:
                        print('           ID Barang Tidak Ditemukan!')
                        print('           Kosongkan Untuk Kembali (ENTER)')
                        continue
                info_barang = database.execute(f'''
                SELECT * FROM {table}
                WHERE id_barang = "{id_barang}";
                ''').fetchall()
                display_info_barang(info_barang)
                while True:
                    pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
                    if pilihan == "Y":
                        ulang = True
                        break
                    elif pilihan == "N":
                        ulang = False
                        break
                    else:
                        print("           Input Invalid!")
                        continue
            return display_barang(database, table)
        elif pilihan == "3":
            ulang = True
            while ulang:
                while True:
                    key_kategori = input("           Key Kategori  : ").upper()
                    if check_kategori(key_kategori) is True:
                        print()
                        break
                    elif key_kategori == "":
                        return display_barang(database, table)
                    else:
                        print('           Key Kategori Tidak Ditemukan!')
                        print('           Kosongkan Untuk Kembali (ENTER)')
                        continue
                info_barang = database.execute(f'''
                SELECT * FROM {table}
                ORDER BY id_barang ASC;
                ''').fetchall()
                list_by_kategori = []
                i = 0
                while i != len(info_barang):
                    if key_kategori in info_barang[i][0]:
                        list_by_kategori.append(info_barang[i])
                        i += 1
                    else:
                        i += 1
                display_info_barang(list_by_kategori)
                while True:
                    pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
                    print()
                    if pilihan == "Y":
                        ulang = True
                        break
                    elif pilihan == "N":
                        ulang = False
                        break
                    else:
                        print("           Input Invalid!")
                        continue
            return display_barang(database, table)
        elif pilihan == "0":
            print()
            barang()
            break
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")


def show_nama_barang(id_barang):
    # Return nama barang menggunakan ID barang
    conn = sq.connect('barang.db')
    nama_barang = conn.execute(f'''
    SELECT nama_barang FROM dataBarang
    WHERE id_barang="{id_barang}"
    ''').fetchall()
    conn.close()
    return nama_barang[0][0]


def show_harga_beli(id_barang):
    # Return harga beli barang menggunakan ID barang
    conn = sq.connect('barang.db')
    harga_beli = conn.execute(f'''
    SELECT harga_beli FROM dataBarang
    WHERE id_barang='{id_barang}';
    ''').fetchall()
    return harga_beli[0][0]


# Fungsi Untuk Kategori #

def check_kategori(key_kategori):
    # Mengecek bahwa kategori yang dimasukkan terdapat di database kategori
    conn = sq.connect('kategori.db')
    list_kategori = conn.execute(f'''
    SELECT * FROM dataKategori;
    ''').fetchall()
    conn.close()
    i = 0
    while i != len(list_kategori):
        if key_kategori == list_kategori[i][0]:
            return True
        else:
            i += 1
    return False


def show_kategori(key_kategori):
    # Return kategori menggunakan key kategori
    conn = sq.connect('kategori.db')
    kategori = conn.execute(f'''
    SELECT * FROM dataKategori
    WHERE key_kategori='{key_kategori}';
    ''').fetchall()
    conn.close()
    return kategori[0][1]


def tambah_kategori(database, table):
    # Menambahkan kategori pada database kategori
    ulang = True
    while ulang:
        kategori = input('''           Masukkan Kategori Barang : 
           ''')
        print("           Key Kategori Maksimal 3 Karakter")
        key_kategori = input("           Masukkan Key Kategori : ").upper()
        while True:
            if check_kategori(key_kategori) is True:
                print("           Key Kategori Sudah Ada!")
                continue
            elif 1 <= len(key_kategori) <= 3:
                break
            elif key_kategori == "":
                return menu_kategori()
            else:
                print("           Input Invalid!")
                print('           Kosongkan Untuk Kembali (ENTER)')
                continue
        database.execute(f'''
        INSERT INTO {table} (key_kategori, kategori)
        VALUES ('{key_kategori}','{kategori}');
        ''')
        database.commit()
        print('           Kategori Berhasil Ditambahkan!')
        while True:
            pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
            if pilihan == "Y":
                ulang = True
                break
            elif pilihan == "N":
                ulang = False
                break
            else:
                print("           Input Invalid!")
                continue


def hapus_kategori(database, table):
    # Menghapus kategori menggunakan key kategori
    ulang = True
    while ulang:
        while True:
            key_kategori = input("           Key Kategori  : ").upper()
            if check_kategori(key_kategori) is True:
                break
            elif key_kategori == "":
                return menu_kategori()
            else:
                print('           Key Kategori Tidak Ditemukan!')
                print('           Kosongkan Untuk Kembali (ENTER)')
                continue
        database.execute(f'''
        DELETE FROM {table}
        WHERE key_kategori='{key_kategori}';
        ''')
        database.commit()
        print('           Kategori Berhasil Dihapus!')
        while True:
            pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
            if pilihan == "Y":
                ulang = True
                break
            elif pilihan == "N":
                ulang = False
                break
            else:
                print("           Input Invalid!")
                continue


def edit_kategori(database, table):
    # Mengedit kategori menggunakan key kategori
    ulang = True
    while ulang:
        while True:
            key_kategori = input("           Key Kategori     : ").upper()
            if check_kategori(key_kategori) is True:
                break
            elif key_kategori == "":
                return menu_kategori()
            else:
                print('           Key Kategori Tidak Ditemukan!')
                print('           Kosongkan Untuk Kembali (ENTER)')
                continue
        data_kategori = database.execute(f'''
        SELECT * FROM {table}
        WHERE key_kategori='{key_kategori}';
        ''').fetchall()
        print(f"           Kategori Barang : {str(data_kategori[0][1]).capitalize()}")
        database.execute(f'''
        DELETE FROM {table}
        WHERE key_kategori='{key_kategori}';
        ''')
        database.commit()
        new_key_kategori = input("           Key Kategori Baru : ").upper()
        new_kategori = input('''           Masukkan Kategori Barang Baru : 
           ''').lower()
        database.execute(f'''
        INSERT INTO {table}
        VALUES ('{new_key_kategori}','{new_kategori}');
        ''')
        database.commit()
        print('           Kategori Berhasil Diedit!')
        while True:
            pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
            if pilihan == "Y":
                ulang = True
                break
            elif pilihan == "N":
                ulang = False
                break
            else:
                print("           Input Invalid!")
                continue


def display_kategori(database, table):
    # Menampilkan informasi kategori pada database kategori
    # Menampilkan semua kategori atau salah satu kategori (dengan key kategori)
    print('''        ||=========== DISPLAY ============||
                1.    Tampilkan Semua
                2.    Cari Kategori (Key)
                0.    Back
                    ''')
    pilihan = input("           Masukkan Pilihan Anda : ")
    print()
    if pilihan == "1":
        info_kategori = database.execute(f'''
        SELECT * FROM {table}
        ORDER BY key_kategori ASC;
        ''').fetchall()
        for data in info_kategori:
            print(f'           Key Kategori   : {data[0]}')
            print(f'           Kategori       : {data[1]}\n')
        display_kategori(database, table)
    elif pilihan == "2":
        ulang = True
        while ulang:
            while True:
                key_kategori = input("           Key Kategori  : ").upper()
                if check_kategori(key_kategori) is True:
                    break
                elif key_kategori == "":
                    return menu_kategori()
                else:
                    print('           Key Kategori Tidak Ditemukan!')
                    print('           Kosongkan Untuk Kembali (ENTER)')
                    continue
            info_kategori = database.execute(f'''
            SELECT * FROM {table}
            WHERE key_kategori="{key_kategori}";
            ''').fetchall()
            if len(info_kategori) != 0:
                for data in info_kategori:
                    print(f'           Kategori   : {data[1]}\n')
            else:
                print(f'           Key Kategori Salah!\n')
            while True:
                pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
                if pilihan == "Y":
                    ulang = True
                    break
                elif pilihan == "N":
                    ulang = False
                    break
                else:
                    print("           Input Invalid!")
                    continue
    elif pilihan == "0":
        print()
        return menu_kategori()
    else:
        print("           Pilihan Tidak Tersedia")
        print("        ||===============<>===============||")


# Fungsi Untuk stok dan jumlah barang terjual #

def tambah_stok(id_barang,count):
    # Menambahkan stok barang dan mengurangi uang kas sebagai pembelian stok barang
    conn1 = sq.connect('barang.db')
    data_barang = conn1.execute(f'''
    SELECT * FROM dataBarang
    WHERE id_barang='{id_barang}';
    ''').fetchall()
    update_stok = data_barang[0][8] + count
    conn1.execute(f'''
    UPDATE dataBarang 
    SET stok='{update_stok}'
    WHERE id_barang='{id_barang}';
    ''')
    conn1.commit()
    pengeluaran = data_barang[0][3] * count
    tambah_uang_kas(-pengeluaran)
    tambah_pengeluaran(pengeluaran)
    update_keuntungan()
    conn1.close()


def kurang_stok(id_barang, count):
    # Mengurangi stok barang ketika terjadi transaksi
    conn = sq.connect('barang.db')
    stok = conn.execute(f'''
    SELECT stok FROM dataBarang
    WHERE id_barang="{id_barang}";
    ''').fetchall()
    update_stok = stok[0][0] - count
    conn.execute(f'''
    UPDATE dataBarang 
    SET stok="{update_stok}"
    WHERE id_barang="{id_barang}";
    ''')
    conn.commit()
    conn.close()


def tambah_barang_terjual(id_barang, count):
    # Menambah barang yang terjual setelah terjadi transaksi
    conn = sq.connect('barang.db')
    barang_terjual = conn.execute(f'''
    SELECT barang_terjual FROM dataBarang
    WHERE id_barang="{id_barang}";
    ''').fetchall()
    update_barang_terjual = barang_terjual[0][0] + count
    conn.execute(f'''
    UPDATE dataBarang 
    SET barang_terjual="{update_barang_terjual}"
    WHERE id_barang="{id_barang}";
    ''')
    conn.commit()
    conn.close()


def show_stok(id_barang):
    # Mengecek Stok Barang pada database barang apakah tersedia sesuai dengan permintaan
    conn = sq.connect('barang.db')
    stok = conn.execute(f'''
    SELECT stok FROM dataBarang
    WHERE id_barang="{id_barang}";
    ''').fetchall()
    return stok[0][0]


# Fungsi Untuk Transaksi #

def generate_id_penjualan():
    # Membuat ID penjualan secara otomatis berdasarkan urutan penambahan, random alphabet, dan tanggal transaksi
    conn = sq.connect('transaksi.db')
    data_rows = conn.execute('''
    SELECT * FROM dataTransaksi
    ORDER BY tanggal_transaksi ASC;
    ''').fetchall()
    conn.close()

    date = dt.datetime.now()
    mid_id1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    mid_id2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if len(data_rows) == 0:
        return "1".zfill(3) + mid_id1 + mid_id2 + date.strftime("%d%m%Y")
    else:
        first_id = data_rows[-1][0][0:3]
        last_id = data_rows[-1][0][-8:len(data_rows[-1][-1])]
        if last_id == date.strftime("%d%m%Y"):
            first_id = str(int(first_id) + 1).zfill(3)
            return first_id + mid_id1 + mid_id2 + last_id
        else:
            return "1".zfill(3) + mid_id1 + mid_id2 + date.strftime("%d%m%Y")


def check_id_penjualan(id_penjualan):
    # Mengecek ID Penjualan pada database Penjualan
    conn = sq.connect('penjualan.db')
    data_id_penjualan = conn.execute('''
    SELECT id_penjualan FROM dataPenjualan
    ORDER BY id_penjualan ASC;
    ''').fetchall()
    i = 0
    while i != len(data_id_penjualan):
        if id_penjualan == data_id_penjualan[i][0]:
            return True
        else:
            i += 1
    return False


def transaksi(database, table):
    # Transaksi barang
    checkout = []
    nama_pembeli = input("           Masukkan Nama Pembeli : ")
    print()
    ulang = True
    while ulang:
        while True:
            id_barang = input("           Masukkan ID Barang : ").upper()
            if check_id_barang(id_barang) is True:
                break
            elif id_barang == "":
                return menu_transaksi()
            elif id_barang:
                print(f'           ID Barang Tidak Ditemukan!')
                print('           Kosongkan Untuk Kembali (ENTER)')
                continue
        data_barang = database.execute(f'''
        SELECT * FROM {table}
        WHERE id_barang = "{id_barang}"        
        ''').fetchall()

        print(f"           Nama Barang   : {data_barang[0][1]}")
        print(f"           Harga Barang  : Rp{data_barang[0][4]}")
        while True:
            count = input("           Jumlah Barang : ")
            if int(count) <= show_stok(id_barang):
                break
            elif count == "":
                return menu_transaksi()
            else:
                print(f'           {data_barang[0][1]} hanya tersisa {data_barang[0][8]}!')
                print('           Kosongkan Untuk Kembali (ENTER)')
                continue
        count = int(count)
        print()
        discount = 0
        if data_barang[0][5] is None:
            discount += 0
        else:
            discount += int(data_barang[0][5])
        checkout.append((data_barang[0][0], data_barang[0][3] * count, data_barang[0][4],
                         data_barang[0][4] * (discount / 100) * count,
                         count, data_barang[0][4] * count))
        print("           y/Y Untuk Checkout")
        print("           n/N Untuk Tambahkan Barang")
        while True:
            pilihan = input("           Ingin Checkout? ").upper()
            if pilihan == "Y":
                ulang = False
                break
            elif pilihan == "N":
                ulang = True
                break
            else:
                print("           Input Invalid!")
                continue
    for data in checkout:
        kurang_stok(data[0],data[4])
        tambah_barang_terjual(data[0],data[4])
    checkout_bill = 0
    checkout_discount = 0
    checkout_cost = 0
    for data in checkout:
        checkout_bill += data[5]
        checkout_discount += data[3]
        checkout_cost += data[1]

    total_checkout = checkout_bill - checkout_discount
    print(f"           Total Checkout : Rp{int(total_checkout)}")
    while True:
        pembayaran = int(input("           Pembayaran     : Rp"))
        print()
        kembalian_pembayaran = 0
        if pembayaran >= total_checkout:
            kembalian_pembayaran = pembayaran - total_checkout
            break
        else:
            print("           Uang Anda Kurang!")
            continue
    date = dt.datetime.now()
    tanggal_transaksi = date.strftime("%d-%m-%Y %H:%M:%S")
    id_penjualan = generate_id_penjualan()
    create_data_penjualan(id_penjualan, nama_pembeli, total_checkout, checkout_cost)
    create_data_transaksi(id_penjualan, nama_pembeli, checkout, checkout_bill, checkout_discount,
                          total_checkout, pembayaran, kembalian_pembayaran, tanggal_transaksi)
    tambah_uang_kas(total_checkout)
    tambah_pemasukan(total_checkout)
    update_keuntungan()
    display_transaksi(id_penjualan)


def create_data_transaksi(id_penjualan, nama_pembeli, checkout, checkout_bill, checkout_discount,
                          total_checkout, pembayaran, kembalian_pembayaran, date):
    # Memasukkan data transaksi ke database transaksi
    conn = sq.connect('transaksi.db')
    table = "dataTransaksi"
    conn.execute(f'''
    INSERT INTO {table} (id_penjualan,nama_pembeli,checkout,checkout_bill,checkout_discount,
                      total_checkout,pembayaran,kembalian_pembayaran,tanggal_transaksi)
    VALUES ('{id_penjualan}','{nama_pembeli}',"{checkout}",'{checkout_bill}','{checkout_discount}',
            '{total_checkout}','{pembayaran}','{kembalian_pembayaran}','{date}');
    ''')
    conn.commit()
    conn.close()


def create_data_penjualan(id_penjualan, nama_pembeli, total_checkout, checkout_cost):
    # Memasukkan data penjualan ke database penjualan
    keuntungan = total_checkout - checkout_cost
    date = dt.datetime.now()
    conn = sq.connect("penjualan.db")
    table = "dataPenjualan"
    conn.execute(f'''
    INSERT INTO {table} (id_penjualan,nama_pembeli,total_checkout,cost,keuntungan,tanggal_penjualan)
    VALUES ('{id_penjualan}','{nama_pembeli}','{total_checkout}',
            '{checkout_cost}','{keuntungan}','{date.strftime('%d-%m-%Y')}');
    ''')
    conn.commit()
    conn.close()


def display_transaksi(id_penjualan):
    # Menampilkan struk pembayaran menggunakan ID penjualan
    # Mengambil dari database transaksi
    conn = sq.connect('transaksi.db')
    table = 'dataTransaksi'
    data_transaksi = conn.execute(f'''
    SELECT * FROM {table}
    WHERE id_penjualan = '{id_penjualan}'
    ''').fetchall()

    print(f'''        ||===============<>===============||
          Toko Jaya Maju Mundur
          Jl. Rongroad Utara, Kab. Sleman,
            DI Yogyakarta
        ------------------------------------
        No. Struk      : {data_transaksi[0][0]}
        Nama Pelanggan : {data_transaksi[0][1]}
        Tgl. {data_transaksi[0][8]}
        ------------------------------------''')

    raw_list1 = data_transaksi[0][2].split(",")
    raw_list2 = []
    for data in raw_list1:
        raw_list2.append(data.strip().lstrip('"[(').rstrip(')]').rstrip("'").lstrip("'"))

    checkout_list = []
    i = 0
    while i != len(raw_list2):
        checkout_list.append(tuple(raw_list2[i:i + 6]))
        i += 6

    for data in checkout_list:
        print(str(show_nama_barang(data[0])).rjust(21," "), str(data[4]).center(4),
              str(data[2]).center(6), str(data[5]).center(7))
    print("        ------------------------------------")
    print(f'''                   Harga Jual :    {data_transaksi[0][3]}
                       Diskon :    {int(data_transaksi[0][4])}
                  --------------------------  
                        Total :    {int(data_transaksi[0][5])}
                        Tunai :    {data_transaksi[0][6]}
                      Kembali :    {int(data_transaksi[0][7])}''')
    print("        ------------------------------------")
    print("            Terima Kasih Telah Berbelaja!")
    print("        ------------------------------------")


# Fungsi Untuk Menu Penjualan #

def display_sales_summary(database, table):
    # Menampilkan informasi penjualan secara keseluruhan
    data_penjualan = database.execute(f'''
    SELECT id_penjualan FROM {table};
    ''').fetchall()
    print("            Laporan per Hari : DD-MM-YYYY")
    print("           Laporan per Bulan : MM-YYYY")
    print("           Laporan per Tahun : YYYY")
    date = ''
    while True:
        sales_date = input("              Masukkan Waktu : ")
        if 8 <= len(sales_date) <= 10:
            d, mt, yr = [int(x) for x in sales_date.split('-')]
            date = dt.datetime(yr, mt, d).strftime("%d%m%Y")
            break
        elif 6 <= len(sales_date) <= 7:
            mt, yr = [int(x) for x in sales_date.split("-")]
            date = dt.datetime(yr, mt, 1).strftime("%m%Y")
            break
        elif len(sales_date) == 4:
            date = sales_date
            break
        elif sales_date == "":
            return menu_penjualan()
        else:
            print("           Input Invalid!")
            print('           Kosongkan Untuk Kembali (ENTER)')
            continue
    print()
    list_id_penjualan = []
    i = 0
    while i != len(data_penjualan):
        if date in data_penjualan[i][0]:
            list_id_penjualan.append(data_penjualan[i][0])
            i += 1
        else:
            i += 1
    for id_penjualan in list_id_penjualan:
        info_penjualan = database.execute(f'''
        SELECT * FROM {table}
        WHERE id_penjualan='{id_penjualan}';
        ''').fetchall()
        for data in info_penjualan:
            print(f"           ID Penjualan      : {data[0]}")
            print(f'           Nama Pembeli      : {data[1]}')
            print(f'           Pembayaran        : Rp{data[2]}')
            print(f'           Cost              : Rp{data[3]}')
            print(f'           Keuntungan        : Rp{data[4]}')
            print(f'           Tanggal Transaksi : {data[5]}\n')


def display_sales_id(database, table):
    # Menampilkan informasi penjualan menggunakan ID penjualan
    ulang = True
    while ulang:
        while True:
            id_penjualan = input("           Masukkan ID Penjualan : ").upper()
            if check_id_penjualan(id_penjualan) is True:
                break
            elif id_penjualan == "":
                return menu_penjualan()
            else:
                print('           ID Penjualan Tidak Ditemukan!')
                print('           Kosongkan Untuk Kembali (ENTER)')
                continue
        data_penjualan = database.execute(f'''
        SELECT * FROM {table}
        WHERE id_penjualan='{id_penjualan}'
        ''').fetchall()
        for data in data_penjualan:
            print(f'           Nama Pembeli      : {data[1]}')
            print(f'           Pembayaran        : Rp{data[2]}')
            print(f'           Cost              : Rp{data[3]}')
            print(f'           Keuntungan        : Rp{data[4]}')
            print(f'           Tanggal Transaksi : {data[5]}\n')

        while True:
            pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
            if pilihan == "Y":
                ulang = True
                break
            elif pilihan == "N":
                ulang = False
                break
            else:
                print("           Input Invalid!")
                continue


def sales_report(database, table):
    # Menampilkan laporan penjualan
    sales = database.execute(f'''
    SELECT * FROM {table};
    ''').fetchall()
    print("            Laporan per Hari : DD-MM-YYYY")
    print("           Laporan per Bulan : MM-YYYY")
    print("           Laporan per Tahun : YYYY")
    date = ''
    while True:
        sales_date = input("              Masukkan Waktu : ")
        if 8 <= len(sales_date) <= 10:
            d, mt, yr = [int(x) for x in sales_date.split('-')]
            date = dt.datetime(yr, mt, d).strftime("%d%m%Y")
            break
        elif 6 <= len(sales_date) <= 7:
            mt, yr = [int(x) for x in sales_date.split("-")]
            date = dt.datetime(yr, mt, 1).strftime("%m%Y")
            break
        elif len(sales_date) == 4:
            date = sales_date
            break
        elif sales_date == "":
            return menu_penjualan()
        else:
            print("           Input Invalid!")
            print('           Kosongkan Untuk Kembali (ENTER)')
            continue
    total_sales = 0
    total_revenue = 0
    total_cost = 0
    total_profit = 0
    for sale in sales:
        if date in sale[0]:
            total_sales += 1
            total_revenue += sale[2]
            total_cost += sale[3]
            total_profit += sale[4]
    display_date = ''
    if len(date) == 8:
        d, mt, yr = [int(x) for x in sales_date.split('-')]
        display_date += dt.datetime(yr, mt, d).strftime("%d %B %Y")
    elif len(date) == 6:
        mt, yr = [int(x) for x in sales_date.split("-")]
        display_date += dt.datetime(yr, mt, 1).strftime("%m %Y")
    else:
        display_date += sales_date

    print(f'''        ||===============<>===============||
          Toko Jaya Maju Mundur
          Jl. Rongroad Utara, Kab. Sleman,
            DI Yogyakarta
        ------------------------------------
          Waktu : {display_date}
          Total Transaksi : {total_sales}
        ------------------------------------
          Pemasukan     :    Rp{total_revenue}
          Pengeluaran   :    Rp{total_cost}   
          Keuntungan    :    Rp{total_profit}''')
    conn = sq.connect('transaksi.db')
    data_trasaksi = conn.execute('''
    SELECT id_penjualan, checkout FROM dataTransaksi
    ''').fetchall()
    i = 0
    raw_data_checkout = []
    while i != len(data_trasaksi):
        if date in data_trasaksi[i][0]:
            raw_list1 = data_trasaksi[i][1].split(",")
            raw_list2 = []
            for data in raw_list1:
                raw_list2.append(data.strip().lstrip('"[(').rstrip(')]').rstrip("'").lstrip("'"))
            n = 0
            m = 0
            checkout_list = []
            while n != len(raw_list2):
                checkout_list.append(tuple(raw_list2[n:n + 6]))
                raw_data_checkout.append((checkout_list[m][0],int(checkout_list[m][4])))
                n += 6
                m += 1
            i += 1
        else:
            i += 1
    list_id = []
    updated_list = []
    for data in raw_data_checkout:
        list_id.append(data[0])
    for id_barang in list_id:
        if [id_barang,0] not in updated_list:
            updated_list.append([id_barang,0])
    n = 0
    while n != len(updated_list):
        i = 0
        while i != len(raw_data_checkout):
            if updated_list[n][0] == raw_data_checkout[i][0]:
                updated_list[n][1] += raw_data_checkout[i][1]
                i += 1
            else:
                i += 1
        n += 1
    print("        ------------------------------------")
    print("           Nama Barang           Terjual")
    for data in updated_list:
        print(str(show_nama_barang(data[0])).center(33), str(data[1]).ljust(0," "))
    print("        ------------------------------------")


# Fungsi Untuk Keuangan #


def tambah_uang_kas(jumlah_uang):
    # Update uang kas pada database Keuangan dengan menambahkan nilainya
    date = dt.datetime.now().strftime("%m-%Y")
    conn = sq.connect('keuangan.db')
    uang_kas = conn.execute(f'''
    SELECT uang_kas FROM dataKeuangan;
    ''').fetchall()
    update_kas = uang_kas[0][0] + jumlah_uang
    conn.execute(f'''
    UPDATE dataKeuangan
    SET uang_kas='{update_kas}'
    WHERE date='{date}';
    ''')
    conn.commit()
    conn.close()


def show_uang_kas():
    # Return Uang Kas terbaru dari database Keuangan
    date = dt.datetime.now().strftime("%m-%Y")
    conn = sq.connect('keuangan.db')
    uang_kas = conn.execute(f'''
    SELECT uang_kas FROM dataKeuangan
    WHERE date='{date}';
    ''').fetchall()
    conn.close()
    return uang_kas[0][0]


def tambah_pemasukan(jumlah_uang):
    # Update pemasukan pada database Keuangan dengan menambahkan nilainya
    date = dt.datetime.now().strftime("%m-%Y")
    conn = sq.connect('keuangan.db')
    pemasukan = conn.execute(f'''
    SELECT pemasukan FROM dataKeuangan;
    ''').fetchall()
    update_pemasukan = pemasukan[0][0] + jumlah_uang
    conn.execute(f'''
    UPDATE dataKeuangan
    SET pemasukan='{update_pemasukan}'
    WHERE date='{date}';
    ''')
    conn.commit()
    conn.close()


def tambah_pengeluaran(jumlah_uang):
    # Update pengeluaran pada database Keuangan dengan menambahkan nilainya
    date = dt.datetime.now().strftime("%m-%Y")
    conn = sq.connect('keuangan.db')
    pengeluaran = conn.execute(f'''
    SELECT pengeluaran FROM dataKeuangan
    WHERE date='{date}';
    ''').fetchall()
    update_pengeluaran = pengeluaran[0][0] + jumlah_uang
    conn.execute(f'''
    UPDATE dataKeuangan
    SET pengeluaran='{update_pengeluaran}'
    WHERE date='{date}';
    ''')
    conn.commit()
    conn.close()


def update_keuntungan():
    # Update keuntungan pada database Keuangan
    # Diperoleh dari pengurangan Pemasukan dengan Pengeluaran
    date = dt.datetime.now().strftime("%m-%Y")
    conn = sq.connect('keuangan.db')
    data_keuangan = conn.execute(f'''
    SELECT pemasukan,pengeluaran FROM dataKeuangan;
    ''').fetchall()
    keuntungan = data_keuangan[0][0] - data_keuangan[0][1]
    conn.execute(f'''
    UPDATE dataKeuangan
    SET keuntungan='{keuntungan}'
    WHERE date='{date}';
    ''')
    conn.commit()
    conn.close()


def check_date_keuangan(date):
    # Mengecek tanggal tanggal pada database keuangan
    conn = sq.connect('keuangan.db')
    date_keuangan = conn.execute(f'''
    SELECT date FROM dataKeuangan
    ORDER BY date ASC;
    ''').fetchall()
    conn.close()
    i = 0
    while i != len(date_keuangan):
        if date == date_keuangan[i][0]:
            return True
        else:
            i += 1
    return False


def display_keuangan(date):
    # Menampilkan keuangan sesuai dengan Bulan dan Tahun (MM-YYYY)
    conn = sq.connect("keuangan.db")
    data_keuangan = conn.execute(f'''
    SELECT * FROM dataKeuangan
    WHERE date="{date}";
    ''').fetchall()
    for data in data_keuangan:
        print(f'           Kas         : Rp{data[1]}')
        print(f'           Pemasukan   : Rp{data[2]}')
        print(f'           Pengeluaran : Rp{data[3]}')
        print(f'           Keuntungan  : Rp{data[4]}')


def show_keuangan():
    # Menu untuk menginput bulan dan tahun, kemudian menampilkan data keuangan
    ulang = True
    while ulang:
        while True:
            while True:
                date = input("           MM-YYYY     : ").upper()
                if 6 <= len(date) <= 7:
                    break
                elif date == "":
                    return keuangan()
                else:
                    print("           Input Invalid!")
                    print('           Kosongkan Untuk Kembali (ENTER)')
                    continue
            mt, yr = [int(x) for x in date.split("-")]
            date = dt.datetime(yr, mt, 1).strftime("%m-%Y")
            if check_date_keuangan(date) is True:
                break
            else:
                print("           Input Waktu Tidak Ditemukan!")
                continue
        display_keuangan(date)
        while True:
            print()
            pilihan = input("           y/Y (Lanjut), n/N (Berhenti): ").upper()
            if pilihan == "Y":
                ulang = True
                break
            elif pilihan == "N":
                ulang = False
                break
            else:
                print("           Input Invalid!")
                continue


def check_rows_keuangan():
    # Mengecek Date pada database Keuangan
    # Membuat tabel baru jika bulan berganti dengan
    # Mengambil nilai uang kas di bulan sebelumnya dan mereset values lainnya menjadi 0
    date = dt.datetime.now().strftime("%m-%Y")
    conn = sq.connect('keuangan.db')
    data_keuangan = conn.execute('''
    SELECT * FROM dataKeuangan
    ORDER BY date ASC;
    ''').fetchall()
    check = True
    i = 0
    while check:
        if len(data_keuangan) == 0:
            conn.execute(f'''
             INSERT INTO dataKeuangan (date,uang_kas,pemasukan,pengeluaran,keuntungan)
             VALUES ('{date}','0','0','0','0');
             ''')
            conn.commit()
        else:
            while i != len(data_keuangan):
                if date == data_keuangan[i][0]:
                    check = False
                    break
                else:
                    i += 1
            if check is True:
                conn.execute(f'''
                INSERT INTO dataKeuangan (date,uang_kas,pemasukan,pengeluaran,keuntungan)
                VALUES ('{date}',{data_keuangan[len(data_keuangan)-1][1]},'0','0','0');
                ''')
                conn.commit()
                break
            break
        break
    conn.close()


# Fungsi Untuk Menu #

def main_menu():
    # Menu Utama
    print('''        ||============= MENU =============|| 
            1.    Transaksi
            2.    Barang
            3.    Penjualan
            4.    Keuangan
                 
           Insert Q to Quit''')

    while True:
        pilihan = input("           Masukkan Pilihan Anda : ").upper()
        if pilihan == "1":
            menu_transaksi()
            break
        elif pilihan == "2":
            menu_barang()
            break
        elif pilihan == "3":
            menu_penjualan()
            break
        elif pilihan == "4":
            keuangan()
        elif pilihan == "Q":
            print("        ||=========== SELESAI ============||")
            quit()
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")
            continue


def menu_transaksi():
    # Menu Transaksi
    print('''        ||========== TRANSAKSI ===========||
            1.    Transaksi
            0.    Back
                ''')

    conn = sq.connect("barang.db")
    table = "dataBarang"
    while True:
        pilihan = input("           Masukkan Pilihan Anda : ")
        if pilihan == "1":
            print("        ||========== Transaksi ===========||")
            transaksi(conn, table)
            break
        elif pilihan == "0":
            return main_menu()
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")
            continue
    conn.close()
    return menu_transaksi()


def menu_barang():
    # Menu Barang
    print('''        ||============ BARANG ============||                        
            1.    Barang
            2.    Kategori
            3.    Stok Barang
            0.    Back
                ''')

    while True:
        pilihan = input("           Masukkan Pilihan Anda : ")
        if pilihan == "1":
            barang()
            break
        elif pilihan == "2":
            menu_kategori()
            break
        elif pilihan == "3":
            menu_stok()
            break
        elif pilihan == "0":
            main_menu()
            break
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")
            continue
    return menu_barang()


def barang():
    # Sub Menu Barang : barang
    print('''        ||============ Barang ============||                        
            1.    Tambah Barang
            2.    Hapus Barang
            3.    Edit Barang
            4.    Lihat Barang
            0.    Back
                ''')

    conn = sq.connect("barang.db")
    table = "dataBarang"
    while True:
        pilihan = input("           Masukkan Pilihan Anda : ")
        if pilihan == "1":
            print("        ||======== Tambah Barang =========||")
            tambah_barang(conn, table)
            break
        elif pilihan == "2":
            print("        ||========= Hapus Barang =========||")
            hapus_barang(conn, table)
            break
        elif pilihan == "3":
            print("        ||========== Edit Barang =========||")
            edit_barang(conn, table)
            break
        elif pilihan == "4":
            display_barang(conn, table)
            break
        elif pilihan == "0":
            menu_barang()
            break
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")
            continue
    conn.close()
    return barang()


def menu_kategori():
    # Sub Menu Barang : Kateoori
    print('''        ||=========== Kategori ===========||                        
            1.    Tambah Kategori
            2.    Hapus Kategori
            3.    Edit Kategori
            4.    Lihat Kategori
            0.    Back
                    ''')

    conn = sq.connect("kategori.db")
    table = "dataKategori"
    while True:
        pilihan = input("           Masukkan Pilihan Anda : ")
        if pilihan == "1":
            print("        ||======= Tambah Kategori ========||")
            tambah_kategori(conn, table)
            break
        elif pilihan == "2":
            print("        ||======== Hapus Kategori ========||")
            hapus_kategori(conn, table)
            break
        elif pilihan == "3":
            print("        ||========= Edit Kategori ========||")
            edit_kategori(conn, table)
            break
        elif pilihan == "4":
            display_kategori(conn, table)
            break
        elif pilihan == "0":
            menu_barang()
            break
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")
            continue
    conn.close()
    return menu_kategori()


def menu_stok():
    # Menu Stok
    print('''        ||============= Stok =============||                 
            1.    Beli Stok Barang
            0.    Back
                    ''')
    while True:
        pilihan = input("           Masukkan Pilihan Anda : ")
        if pilihan == "1":
            ulang = True
            while ulang:
                id_barang = input("           Masukkan ID Barang : ").upper()
                if check_id_barang(id_barang) is True:
                    print(f'           Nama Barang        : {show_nama_barang(id_barang)}')
                    print(f'           Harga Beli         : Rp{show_harga_beli(id_barang)}')
                    count = input("           Jumlah Barang      : ")
                    if count.isdigit():
                        if show_harga_beli(id_barang)*int(count) <= show_uang_kas():
                            tambah_stok(id_barang,int(count))
                            print(f'           {show_nama_barang(id_barang)} ditambahkan {count}!')
                            print(f'           Anda Menggunakan Rp{show_harga_beli(id_barang)*int(count)}')
                            print(f'           Stok Terbaru       : {show_stok(id_barang)}')
                            ulang = False
                        else:
                            print('           Uang Kas Tidak Cukup!')
                            print(f'           Uang Kurang Rp{show_harga_beli(id_barang)*int(count) - show_uang_kas()}')
                    elif id_barang == "":
                        return menu_stok()
                    else:
                        print('           Input Invalid!')
                elif id_barang == "":
                    return menu_stok()
                else:
                    print('           ID Barang Tidak Ditemukan!')
                    print('           Kosongkan Untuk Kembali (ENTER)')
            menu_stok()
            break
        elif pilihan == "0":
            return menu_barang()
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")
            continue
    return menu_stok()


def menu_penjualan():
    # Menu Penjualan
    print('''        ||=========== PENJUALAN ==========||
            1.    Sales Report
            2.    Sales Summary
            3.    Cari Penjualan
            4.    Lihat Struk Transaksi
            0.    Back
                ''')

    conn = sq.connect('penjualan.db')
    table = "dataPenjualan"
    while True:
        pilihan = input("           Masukkan Pilihan Anda : ")
        if pilihan == "1":
            print("        ||========= Sales Report =========||")
            sales_report(conn, table)
            break
        elif pilihan == "2":
            print("        ||======== Sales Summary =========||")
            display_sales_summary(conn, table)
            break
        elif pilihan == "3":
            print("        ||======== Cari Penjualan ========||")
            display_sales_id(conn, table)
            break
        elif pilihan == "4":
            print("        ||===== Lihat Struk Transaksi ====||")
            id_penjualan = input("           ID Penjualan      : ")
            display_transaksi(id_penjualan)
            break
        elif pilihan == "0":
            return main_menu()
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")
            continue
    conn.close()
    return menu_penjualan()


def keuangan():
    # Menu Keuangan
    print('''        ||=========== KEUANGAN ===========||
            1.    Keuangan Saat Ini
            2.    Lihat Keuangan (MM-YYYY)
            3.    Tambah Kas
            0.    Back
                ''')

    while True:
        pilihan = input("           Masukkan Pilihan Anda : ")
        if pilihan == "1":
            print("        ||======= Keuangan Saat Ini ======||")
            date = dt.datetime.now()
            display_keuangan(date.strftime("%m-%Y"))
            break
        elif pilihan == "2":
            print("        ||======== Lihat Keuangan ========||")
            show_keuangan()
            break
        elif pilihan == "3":
            print("        ||========== Tambah Kas ==========||")
            while True:
                jumlah_uang = input("           Masukkan Nominal   : Rp")
                if jumlah_uang.isdigit():
                    jumlah_uang = int(jumlah_uang)
                    break
                elif jumlah_uang == "":
                    return keuangan()
                else:
                    print('           Input Invalid!')
                    print('           Kosongkan Untuk Kembali (ENTER)')
                    continue
            tambah_uang_kas(jumlah_uang)
            print('           Uang Kas Berhasil Ditambahkan!')
            break
        elif pilihan == "0":
            return main_menu()
        else:
            print("           Pilihan Tidak Tersedia")
            print("        ||===============<>===============||")
            continue
    return keuangan()


print('''
        ||===============<>===============||
        ||==== PROGRAM POINT OF SALES ====||''')
check_rows_keuangan()
main_menu()
