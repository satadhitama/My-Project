# Point of Sales (PoS)

## User Guides

1. Buka script pemrograman python
     - create table.py
     - main.py
2. Membuat tabel database
     - Run create table.py
3. Menjalankan Program Utama
     - Run main.py
4. Menambahkan Kategori Barang
     Menu Barang > Kategori > Tambah Kategori
     - Masukkan kategori barang
       Exp: Jeans
     - Masukkan Key Kategori (maksimal 3 karakter)
       Exp: JN
5. Menambahkan data Barang
     Menu Barang > Barang > Tambah Barang
     - Mengisi Informasi barang
     - Diskon, produsen, dan supplier boleh dikosongi
6. Menambahkan uang kas
    User dapat menambahkan uang kas jika diperlukan. Uang kas digunakan untuk membeli stok barang pada menu stok barang
     Menu Keuangan > Tambah Kas
7. Menambahkan Stok Barang
     Menu Barang > Stok Barang > Beli Stok Barang
     Stok barang hanya bisa ditambahkan jika uang kas tersedia sesuai dengan harga beli barang dan jumlah stok.
8. Melakukan Transaksi
     Menu Transaksi > Transaksi
9. Database telah terisi data-data yang diperlukan, user dapat mengakses fitur-ftur lain pada program Point of Sales (PoS)

##  Fitur Program :

1. Menu Transaksi
    Melakukan Transaksi
2. Menu Barang
       2.1. Barang
	2.1.1. Tambah data barang
	2.1.2. Hapus data barang
	2.1.3. Edit data barang
	2.1.4. Lihat data barang
		2.1.4.1. Tampilkan Semua
		2.1.4.2. Cari Barang (ID)
		2.1.4.3. Cari Barang (Kategori)
       2.2. Kategori
	2.2.1. Tambah Kategori
	2.2.2. Hapus Kategori
	2.2.3. Edit Kategori
	2.2.4. Lihat Kategori
		2.2.4.1. Tampilkan Semua
		2.2.4.2. Cari Kategori (Key)
       2.3. Stok Barang 
	2.3.1 Tambah Stok Barang
3. Penjualan
       3.1. Sales Report 
       3.2. Sales Summary 
       3.3. Cari Penjualan
       3.4. Lihat Struk
4. Keuangan 
       4.1. Keuangan Saat Ini
       4.2. Lihat Keuangan (MM-YYYY)
       4.3. Tambah Kas

## About this project

This project was made due to the final project for my "Algoritma Pemrograman" class in 1st semester. 

This project was made from scratch with some functionality of PoS system. Because the objective of this project is to test the fundamental of programming algorithm using python (implementation of Point of Sales Program), the program was made to run on terminal.